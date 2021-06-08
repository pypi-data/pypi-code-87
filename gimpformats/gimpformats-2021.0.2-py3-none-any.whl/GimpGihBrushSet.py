#!/usr/bin/env python3
"""Gimp Image Pipe Format.

The gih format is use to store a series of brushes, and some extra info
for how to use them.
"""
from __future__ import annotations

from io import BytesIO

from binaryiotools import IO

from .GimpGbrBrush import GimpGbrBrush


class GimpGihBrushSet:
	"""Gimp Image Pipe Format.

	The gih format is use to store a series of brushes, and some extra info
	for how to use them.

	See:
		https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/gih.txt
	"""

	def __init__(self, fileName: str = None):
		"""Gimp Image Pipe Format.

		Args:
			fileName (str, optional): filename. Defaults to None.
		"""
		self.fileName = None
		self.name = ""
		self.params = {}
		self.brushes = []
		if fileName is not None:
			self.load(fileName)

	def load(self, fileName: BytesIO | str):
		"""Load a gimp file.

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

		Args:
			data (bytes): data buffer to decode
			index (int, optional): index within the buffer to start at. Defaults to 0.

		Returns:
			int: offset
		"""
		ioBuf = IO(data, index)
		self.name = ioBuf.textLine
		secondLine = ioBuf.textLine.split(" ")
		self.params = {}
		numBrushes = int(secondLine[0])
		# everything that's left is a gimp-image-pipe-parameters parasite
		for i in range(1, len(secondLine)):
			param = secondLine[i].split(":", 1)
			self.params[param[0].strip()] = param[1].strip()
		self.brushes = []
		for _ in range(numBrushes):
			brush = GimpGbrBrush()
			ioBuf.index = brush.decode(
				ioBuf.data, ioBuf.index
			)  # TODO: broken.  For some reason there is extra data between brushes!
			self.brushes.append(brush)
		return ioBuf.index

	def encode(self):
		"""Encode this object to a byte array."""
		ioBuf = IO()
		ioBuf.textLine = self.name
		# add the second line of data
		secondLine = [str(len(self.brushes))]
		for key in self.params:
			secondLine.append(key + ":" + str(self.params[key]))
		ioBuf.textLine = " ".join(secondLine)
		# add the brushes
		for brush in self.brushes:
			ioBuf.addBytes(brush.encode())
		return ioBuf.data

	def save(self, tofileName: str):
		"""Save this gimp image to a file."""
		if hasattr(tofileName, "write"):
			file = tofileName
		else:
			file = open(tofileName, "wb")
		file.write(self.encode())
		file.close()

	def __repr__(self, indent=""):
		"""Get a textual representation of this object."""
		ret = []
		if self.fileName is not None:
			ret.append("fileName: " + self.fileName)
		ret.append("Name: " + str(self.name))
		for k, val in list(self.params.items()):
			ret.append(k + ": " + str(val))
		for i in range(len(self.brushes)):
			ret.append("Brush " + str(i))
			ret.append(self.brushes[i].__repr__(indent + "\t"))
		return ("\n" + indent).join(ret)
