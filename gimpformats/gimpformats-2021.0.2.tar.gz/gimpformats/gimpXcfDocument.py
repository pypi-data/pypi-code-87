#!/usr/bin/env python3
"""Pure python implementation of the gimp xcf file format.

Currently supports:
	Loading xcf files
	Getting image hierarchy and info
	Getting image for each layer (PIL image)
Currently not supporting:
	Saving
	Programatically alter documents (add layer, etc)
	Rendering a final, compositied image
"""
from __future__ import annotations

import copy
from io import BytesIO, FileIO

import PIL.ImageGrab
from binaryiotools import IO
from blendmodes.blend import BlendType, blendLayers
from blendmodes.imagetools import rasterImageOffset
from PIL import Image

from .GimpChannel import GimpChannel
from .GimpImageHierarchy import GimpImageHierarchy
from .GimpIOBase import GimpIOBase
from .GimpLayer import GimpLayer
from .GimpPrecision import Precision


class GimpDocument(GimpIOBase):
	"""Pure python implementation of the gimp file format.

	Has a series of attributes including the following:
	self._layers = None
	self._layerPtr = []
	self._channels = []
	self._channelPtr = []
	self.version = None
	self.width = 0
	self.height = 0
	self.baseColorMode = 0
	self.precision = None # Precision object
	self._data = None

	See:
		https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/xcf.txt
	"""

	def __init__(self, fileName=None):
		"""Pure python implementation of the gimp file format.

		Has a series of attributes including the following:
		self._layers = None
		self._layerPtr = []
		self._channels = []
		self._channelPtr = []
		self.version = None
		self.width = 0
		self.height = 0
		self.baseColorMode = 0
		self.precision = None # Precision object
		self._data = None

		See:
			https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/xcf.txt
		"""
		GimpIOBase.__init__(self, self)
		self._layers = []
		self._layerPtr = []
		self._channels = []
		self._channelPtr = []
		self.version = 11  # This is the most recent version
		self.width = 0
		self.height = 0
		self.baseColorMode = 0
		self.precision = None  # Precision object
		self._data = None
		self.fileName = None
		if fileName is not None:
			self.load(fileName)

	def load(self, fileName: BytesIO | str):
		"""Load a gimp xcf and decode the file. See decode for more on this process.

		:param fileName: can be a file name or a file-like object
		"""
		if isinstance(fileName, str):
			self.fileName = fileName
			file = open(fileName, "rb")
		else:
			self.fileName = fileName.name
			file = fileName
		data = file.read()
		file.close()
		self.decode(data)

	def decode(self, data: bytes, index: int = 0) -> int:
		"""Decode a byte buffer.

		Steps:
		Create a new IO buffer (array of binary values)
		Check that the file is a valid gimp xcf
		Grab the file version
		Grab other attributes as outlined in the spec
		Get precision data using the class and ioBuf buffer
		List of properties
		Get the layers and add the pointers to them
		Get the channels and add the pointers to them
		Return the offset

		Args:
			data (bytes): data buffer to decode
			index (int, optional): index within the buffer to start at]. Defaults to 0.

		Raises:
			Exception: "Not a valid GIMP file"

		Returns:
			int: offset
		"""
		# Create a new IO buffer (array of binary values)
		ioBuf = IO(data, index)
		# Check that the file is a valid gimp xcf
		if ioBuf.getBytes(9) != b"gimp xcf ":
			raise Exception("Not a valid GIMP file")
		# Grab the file version
		version = ioBuf.cString
		if version == "file":
			self.version = 0
		else:
			self.version = int(version[1:])
		# Grab other attributes as outlined in the spec
		self.width = ioBuf.u32
		self.height = ioBuf.u32
		self.baseColorMode = ioBuf.u32
		# Get precision data using the class and ioBuf buffer
		self.precision = Precision()
		self.precision.decode(self.version, ioBuf)
		# List of properties
		self._propertiesDecode(ioBuf)
		self._layerPtr = []
		self._layers = []
		# Get the layers and add the pointers to them
		while True:
			ptr = self._pointerDecode(ioBuf)
			if ptr == 0:
				break
			self._layerPtr.append(ptr)
			layer = GimpLayer(self)
			layer.decode(ioBuf.data, ptr)
			self._layers.append(layer)
		# Get the channels and add the pointers to them
		self._channelPtr = []
		self._channels = []
		while True:
			ptr = self._pointerDecode(ioBuf)
			if ptr == 0:
				break
			self._channelPtr.append(ptr)
			chnl = GimpChannel(self)
			chnl.decode(ioBuf.data, ptr)
			self._channels.append(chnl)
		# Return the offset
		return ioBuf.index

	def encode(self):
		"""Encode to a byte array.

		Steps:
		Create a new IO buffer (array of binary values)
		The file is a valid gimp xcf
		Set the file version
		Set other attributes as outlined in the spec
		Set precision data using the class and ioBuf buffer
		List of properties
		Set the layers and add the pointers to them
		Set the channels and add the pointers to them
		Return the data

		"""
		# Create a new IO buffer (array of binary values)
		ioBuf = IO()
		# The file is a valid gimp xcf
		ioBuf.addBytes("gimp xcf ")
		# Set the file version
		ioBuf.addBytes(f"v{self.version:03d}" + "\0")
		# Set other attributes as outlined in the spec
		ioBuf.u32 = self.width
		ioBuf.u32 = self.height
		ioBuf.u32 = self.baseColorMode
		# Set precision data using the class and ioBuf buffer
		if self.precision is None:
			self.precision = Precision()
		self.precision.encode(self.version, ioBuf)
		# List of properties
		ioBuf.addBytes(self._propertiesEncode())
		dataAreaIdx = ioBuf.index + self.POINTER_SIZE * (len(self.layers) + len(self._channels))
		dataAreaIO = IO()
		# Set the layers and add the pointers to them
		for layer in self.layers:
			ioBuf.index = dataAreaIdx + dataAreaIO.index
			dataAreaIO.addBytes(layer.encode())
		# Set the channels and add the pointers to them
		for channel in self._channels:
			ioBuf.index = dataAreaIdx + dataAreaIO.index
			dataAreaIO.addBytes(channel.encode())
		ioBuf.addBytes(dataAreaIO)
		# Return the data
		return ioBuf.data

	def forceFullyLoaded(self):
		"""Make sure everything is fully loaded from the file."""
		for layer in self.layers:
			layer.forceFullyLoaded()
		for channel in self._channels:
			channel.forceFullyLoaded()
		# no longer try to get the data from file
		self._layerPtr = None
		self._channelPtr = None
		self._data = None

	@property
	def layers(self):
		"""Decode the image's layers if necessary.

		TODO: need to do the same thing with self.Channels
		"""
		if len(self._layers) == 0:
			self._layers = []
			for ptr in self._layerPtr:
				layer = GimpLayer(self)
				layer.decode(self._data, ptr)
				self._layers.append(layer)
			# add a reference back to this object so it doesn't go away while array is in use
			self._layers.parent = self
			# override some internal methods so we can do more with them
			self._layers._actualDelitem_ = self._layers.__delitem__
			self._layers.__delitem__ = self.deleteLayer
			self._layers._actualSetitem_ = self._layers.__setitem__
			self._layers.__setitem__ = self.setLayer
		return self._layers

	def getLayer(self, index: int):
		"""Return a given layer."""
		return self.layers[index]

	def setLayer(self, index, layer):
		"""Assign to a given layer."""
		self.forceFullyLoaded()
		self._layerPtr = None  # no longer try to use the pointers to get data
		self.layers._actualSetitem_(index, layer)

	def newLayer(self, name: str, image: Image.Image, index: int = -1) -> GimpLayer:
		"""Create a new layer based on a PIL image.

		Args:
			name (str): a name for the new layer
			image (Image.Image): pil image
			index (int, optional): where to insert the new layer (default=top). Defaults to -1.

		Returns:
			GimpLayer: newly created GimpLayer object
		"""
		layer = GimpLayer(self, name, image)
		layer.imageHierarchy = GimpImageHierarchy(self, image=image)
		self.insertLayer(layer, index)
		return layer

	def newLayerFromClipboard(self, name: str = "pasted", index: int = -1) -> GimpLayer | None:
		"""Create a new image from the system clipboard.

		NOTE: requires pillow PIL implementation
		NOTE: only works on OSX and Windows

		Args:
			name (str): a name for the new layer
			index (int, optional): where to insert the new layer (default=top). Defaults to -1.

		Returns:
			GimpLayer: newly created GimpLayer object
		"""
		image = PIL.ImageGrab.grabclipboard()
		if isinstance(image, Image.Image):
			return self.newLayer(name, image, index)

	def addLayer(self, layer: GimpLayer):
		"""Append a layer object to the document.

		:param layer: the new layer to append
		"""
		self.insertLayer(layer, -1)

	def appendLayer(self, layer: GimpLayer):
		"""Append a layer object to the document.

		:param layer: the new layer to append
		"""
		self.insertLayer(layer, -1)

	def insertLayer(self, layer: GimpLayer, index: int = -1):
		"""Insert a layer object at a specific position.

		:param layer: the new layer to insert
		:param index: where to insert the new layer (default=top)
		"""
		self._layers.insert(index, layer)

	def deleteLayer(self, index: int) -> None:
		"""Delete a layer."""
		self.__delitem__(index)

	# make this class act like this class is an array of layers
	def __len__(self) -> int:
		"""Make this class act like this class is an array of layers...

		Get the len.
		"""
		return len(self.layers)

	def __getitem__(self, index: int) -> GimpLayer:
		"""Make this class act like this class is an array of layers...

		Get the layer at an index.
		"""
		return self.layers[index]

	def __setitem__(self, index: int, layer) -> None:
		"""Make this class act like this class is an array of layers...

		Set a layer at an index.
		"""
		self.setLayer(index, layer)

	def __delitem__(self, index: int) -> None:
		"""Make this class act like this class is an array of layers...

		Delete a layer at an index.
		"""
		self.deleteLayer(index)

	def __inc__(self, amt) -> GimpDocument:
		self.appendLayer(amt)
		return self

	@property
	def image(self):
		"""Get a final, compiled image."""
		# We need to preprocess the layers to sort them into a list of layers
		# and groups. Where a group is a list of layers

		# Example Layers [layer, layer, group, layer]
		# Example Group [Layer(Group), [layer, layer, ...]]
		layers = self.layers[:]  # Copy the attribute rather than write to it
		layersOut = []
		index = 0
		while index < len(layers):
			layerOrGroup = layers[index]
			if layerOrGroup.isGroup:
				elem = [layerOrGroup, []]
				index += 1
				while layers[index].itemPath is not None:
					layerCopy = copy.deepcopy(layers[index])
					layerCopy.xOffset -= layerOrGroup.xOffset
					layerCopy.yOffset -= layerOrGroup.yOffset
					elem[1].append(layerCopy)
					layers.pop(index)
				layersOut.append(elem)
			else:
				layersOut.append(layerOrGroup)
				index += 1
		return flattenAll(layersOut, (self.width, self.height))

	def save(self, filename: str | FileIO = None):
		"""Save this gimp image to a file."""
		self.forceFullyLoaded()
		if filename is None:
			filename = self.fileName
		if isinstance(filename, str):
			file = open(filename, "wb")
		else:
			file = filename
		file.write(self.encode())
		file.close()

	def saveNew(self, filename=None):
		"""Save a new gimp image to a file."""
		if filename is None:
			filename = self.fileName
		if isinstance(filename, str):
			file = open(filename, "wb")
		else:
			file = filename
		file.write(self.encode())
		file.close()

	def __repr__(self, indent="") -> str:
		"""Get a textual representation of this object."""
		del indent
		ret = []
		if self.fileName is not None:
			ret.append("fileName: " + self.fileName)
		ret.append("Version: " + str(self.version))
		ret.append("Size: " + str(self.width) + " x " + str(self.height))
		ret.append("Base Color Mode: " + self.COLOR_MODES[self.baseColorMode])
		ret.append("Precision: " + str(self.precision))
		ret.append(GimpIOBase.__repr__(self))
		if self._layerPtr:
			ret.append("Layers: ")
			for layer in self.layers:
				ret.append(layer.__repr__("\t"))
		if self._channelPtr:
			ret.append("Channels: ")
			for channel in self._channels:
				ret.append(channel.__repr__("\t"))
		return "\n".join(ret)


def blendModeLookup(
	blendmode: int, blendLookup: dict[int, BlendType], default: BlendType = BlendType.NORMAL
):
	"""Get the blendmode from a lookup table."""
	if blendmode not in blendLookup:
		print("WARNING " + str(blendmode) + " is not currently supported!")
		return default
	return blendLookup[blendmode]


def flattenLayerOrGroup(
	layerOrGroup: list[GimpLayer] | GimpLayer,
	imageDimensions: tuple[int, int],
	flattenedSoFar: Image.Image | None = None,
	ignoreHidden: bool = True,
) -> Image.Image:
	"""Flatten a layer or group on to an image of what has already been	flattened.

	Args:
		layerOrGroup (Layer,Group): A layer or a group of layers
		imageDimensions (tuple[int, int]): size of the image
		flattenedSoFar (PIL.Image, optional): the image of what has already
		been flattened. Defaults to None.
		ignoreHidden (bool, optional): ignore layers that are hidden. Defaults
		to True.

	Returns:
		PIL.Image: Flattened image
	"""
	blendLookup = {
		0: BlendType.NORMAL,
		3: BlendType.MULTIPLY,
		4: BlendType.SCREEN,
		5: BlendType.OVERLAY,
		6: BlendType.DIFFERENCE,
		7: BlendType.ADDITIVE,
		8: BlendType.NEGATION,
		9: BlendType.DARKEN,
		10: BlendType.LIGHTEN,
		11: BlendType.HUE,
		12: BlendType.SATURATION,
		13: BlendType.COLOUR,
		14: BlendType.LUMINOSITY,
		15: BlendType.DIVIDE,
		16: BlendType.COLOURDODGE,
		17: BlendType.COLOURBURN,
		18: BlendType.HARDLIGHT,
		19: BlendType.SOFTLIGHT,
		20: BlendType.GRAINEXTRACT,
		21: BlendType.GRAINMERGE,
		23: BlendType.OVERLAY,
		24: BlendType.HUE,
		25: BlendType.SATURATION,
		26: BlendType.COLOUR,
		27: BlendType.LUMINOSITY,
		28: BlendType.NORMAL,
		30: BlendType.MULTIPLY,
		31: BlendType.SCREEN,
		32: BlendType.DIFFERENCE,
		33: BlendType.ADDITIVE,
		34: BlendType.NEGATION,
		35: BlendType.DARKEN,
		36: BlendType.LIGHTEN,
		37: BlendType.HUE,
		38: BlendType.SATURATION,
		39: BlendType.COLOUR,
		40: BlendType.LUMINOSITY,
		41: BlendType.DIVIDE,
		42: BlendType.COLOURDODGE,
		43: BlendType.COLOURBURN,
		44: BlendType.HARDLIGHT,
		45: BlendType.SOFTLIGHT,
		46: BlendType.GRAINEXTRACT,
		47: BlendType.GRAINMERGE,
		48: BlendType.VIVIDLIGHT,
		49: BlendType.PINLIGHT,
		52: BlendType.EXCLUSION,
	}

	if isinstance(layerOrGroup, list):
		if ignoreHidden and not layerOrGroup[0].visible:
			foregroundRender = Image.new("RGBA", imageDimensions)
		else:  # A group is a list of layers
			# (see flattenAll)
			foregroundRender = rasterImageOffset(
				flattenAll(layerOrGroup[1], imageDimensions, ignoreHidden),
				imageDimensions,
				(layerOrGroup[0].xOffset, layerOrGroup[0].yOffset),
			)
		if flattenedSoFar is None:
			return foregroundRender
		return blendLayers(
			flattenedSoFar,
			foregroundRender,
			blendModeLookup(layerOrGroup[0].blendMode, blendLookup),
			layerOrGroup[0].opacity,
		)

	if ignoreHidden and not layerOrGroup.visible:
		foregroundRender = Image.new("RGBA", imageDimensions)
	else:
		# Get a raster image and apply blending
		foregroundRender = rasterImageOffset(
			layerOrGroup.image, imageDimensions, (layerOrGroup.xOffset, layerOrGroup.yOffset)
		)
	if flattenedSoFar is None:
		return foregroundRender
	return blendLayers(
		flattenedSoFar,
		foregroundRender,
		blendModeLookup(layerOrGroup.blendMode, blendLookup),
		layerOrGroup.opacity,
	)


def flattenAll(
	layers: list[GimpLayer], imageDimensions: tuple[int, int], ignoreHidden: bool = True
) -> Image.Image:
	"""Flatten a list of layers and groups.

	Note the bottom layer is at the end of the list

	Args:
		layers (list[GimpLayer]): A list of layers and groups
		imageDimensions (tuple[int, int]): size of the image been flattened. Defaults to None.
		ignoreHidden (bool, optional): ignore layers that are hidden. Defaults
		to True.

	Returns:
		PIL.Image: Flattened image
	"""
	end = len(layers) - 1
	flattenedSoFar = flattenLayerOrGroup(layers[end], imageDimensions, ignoreHidden=ignoreHidden)
	for layer in range(end - 1, -1, -1):
		flattenedSoFar = flattenLayerOrGroup(
			layers[layer], imageDimensions, flattenedSoFar=flattenedSoFar, ignoreHidden=ignoreHidden
		)
	return flattenedSoFar
