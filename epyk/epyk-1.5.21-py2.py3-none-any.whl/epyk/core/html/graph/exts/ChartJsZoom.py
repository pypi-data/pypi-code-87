
from epyk.core.data.DataClass import DataClass

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class ZoomRange(DataClass):

  @property
  def x(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._attrs["x"]

  @x.setter
  def x(self, num):
    self._attrs["x"] = num

  @property
  def y(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._attrs["y"]

  @y.setter
  def y(self, num):
    self._attrs["y"] = num


class ZoomAttrs(DataClass):

  @property
  def enabled(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._attrs["enabled"]

  @enabled.setter
  def enabled(self, flag):
    self._attrs["enabled"] = flag

  @property
  def mode(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._attrs["mode"]

  @mode.setter
  def mode(self, value):
    self._attrs["mode"] = value

  @property
  def rangeMin(self):
    return self.sub_data("rangeMin", ZoomRange)

  @property
  def rangeMax(self):
    return self.sub_data("rangeMax", ZoomRange)

  @property
  def speed(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._attrs["speed"]

  @speed.setter
  def speed(self, num):
    self._attrs["speed"] = num

  @property
  def threshold(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._attrs["threshold"]

  @threshold.setter
  def threshold(self, num):
    self._attrs["threshold"] = num


class ZoomPan(ZoomAttrs):

  def onPan(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Function called while the user is zooming

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._attrs["onPan"] = JsObjects.JsVoid("function(data) { %s }" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile))

  def onPanComplete(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Function called while the user is zooming

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._attrs["onPanComplete"] = JsObjects.JsVoid("function(data) { %s }" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile))


class ZoomZoom(ZoomAttrs):

  @property
  def drag(self):
    """
    Description:
    -----------
    Enable drag-to-zoom behavior
    """
    return self._attrs["drag"]

  @drag.setter
  def drag(self, flag):
    self._attrs["drag"] = flag

  @property
  def sensitivity(self):
    """
    Related Pages:

      https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._attrs["sensitivity"]

  @sensitivity.setter
  def sensitivity(self, num):
    self._attrs["sensitivity"] = num

  def onZoom(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Function called while the user is zooming.

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._attrs["onZoom"] = JsObjects.JsVoid("function(data) { %s }" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile))

  def onZoomComplete(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Function called once zooming is completed.

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._attrs["onZoomComplete"] = JsObjects.JsVoid("function(data) { %s }" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile))


class Zoom(DataClass):

  def set_default(self, mode="xy"):
    """
    Description:
    ------------
    Set zoom default attributes.

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-zoom

    Attributes:
    ----------
    :param mode: String. Optional. Zooming directions.
    """
    self.pan.mode = mode
    self.pan.enabled = True
    self.zoom.enabled = True
    self.zoom.mode = mode

  @property
  def pan(self):
    return self.sub_data("pan", ZoomPan)

  @property
  def zoom(self):
    return self.sub_data("zoom", ZoomZoom)

