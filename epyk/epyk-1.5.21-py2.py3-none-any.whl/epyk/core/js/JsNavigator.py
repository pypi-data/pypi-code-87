#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsBoolean


class JsGeolocation:

  def __init__(self, page):
    self.page = page

  def getPosition(self, jsData):
    """

    :param jsData:

    """
    jsData = JsUtils.jsConvertData(jsData, None)
    return JsObject.JsObject.get(
      "navigator.geolocation.getCurrentPosition(function(position){console.log(position); %s})" % (jsData))

  def getCurrentPosition(self, callbackFnc, errorFnc=None, options=None):
    """
    Description:
    ------------
    The getCurrentPosition() method is used to return the user's position.

    Related Pages:

      https://developer.mozilla.org/fr/docs/Web/API/Geolocation/getCurrentPosition
      https://www.w3schools.com/html/html5_geolocation.asp
      https://developer.kaiostech.com/api/geolocation/getposition

    Attributes:
    ----------
    :param callbackFnc: String. A callback function that takes a Position object as its sole input parameter.
    :param errorFnc: String. Optional. An callback func that takes a PositionError object as its sole input parameter.
    :param options: Dictionary. Optional. An optional PositionOptions object.
    """
    if errorFnc is None:
      return JsObject.JsObject.get("navigator.geolocation.getCurrentPosition(%s)" % callbackFnc)

    return JsObject.JsObject.get(
      "navigator.geolocation.getCurrentPosition(%s, %s)" % (callbackFnc, errorFnc))

  def watchPosition(self, callbackFnc, watchId, errorFnc=None, options=None):
    """
    Description:
    ------------
    Returns the current position of the user and continues to return updated position as the user moves.

    Usage::

      options = {"enableHighAccuracy": False, "timeout": 5000, "maximumAge": 0}

    Related Pages:

      https://www.w3schools.com/html/html5_geolocation.asp

    :param callbackFnc: String. A callback function that takes a Position object as an input parameter.
    :param watchId: The ID number returned by the Geolocation.watchPosition() method when installing the handler you wish to remove.
    :param errorFnc: Optional An optional callback function that takes a PositionError object as an input parameter.
    :param options: Optional An optional PositionOptions object that provides configuration options for the location watch.
    """
    return JsObject.JsObject.new(
      "navigator.geolocation.watchPosition(%s)" % callbackFnc, isPyData=False).setVar(watchId)

  def clearWatch(self, watchId):
    """
    Description:
    ------------
    Stops the watchPosition() method.

    Related Pages:

      https://www.w3schools.com/html/html5_geolocation.asp

    :param watchId: The ID number returned by the Geolocation.watchPosition() method when installing the handler you wish to remove.
    """
    watchId = JsUtils.jsConvertData(watchId, None)
    return JsObject.JsObject("navigator.geolocation.clearWatch(%s)" % watchId, isPyData=False)


class JsNavigator:

  def __init__(self, page):
    self.page = page

  @property
  def geolocation(self):
    """
    Description:
    ------------
    The HTML Geolocation API is used to locate a user's position.

    Related Pages:

      https://w3c.github.io/geolocation-api/#navi-geo
      https://www.w3schools.com/html/html5_geolocation.asp
    """
    return JsGeolocation(self.page)

  @property
  def language(self):
    """
    Description:
    ------------
    The language property returns the language version of the browser.

    Related Pages:

      https://www.w3schools.com/jsref/prop_nav_language.asp
    """
    return JsString.JsString("navigator.language", isPyData=False)

  @property
  def browserLanguage(self):
    """
    Description:
    ------------
    The language property returns the language version of the browser.
    For IE10 and earlier versions, you can use the browserLanguage property.

    Related Pages:

      https://www.w3schools.com/jsref/prop_nav_language.asp
    """
    return JsString.JsString("navigator.browserLanguage", isPyData=False)

  @property
  def appCodeName(self):
    """
    Description:
    ------------
    The appCodeName property returns the application code name of the browser.

    Related Pages:

      https://www.w3schools.com/js/js_window_navigator.asp
    """
    return JsString.JsString("navigator.appCodeName", isPyData=False)

  @property
  def appName(self):
    """
    Description:
    ------------
    The appName property returns the application name of the browser.

    Related Pages:

      https://www.w3schools.com/js/js_window_navigator.asp
    """
    return JsString.JsString("navigator.appName", isPyData=False)

  @property
  def product(self):
    """
    Description:
    ------------
    The product property returns the product name of the browser engine.

    Related Pages:

      https://www.w3schools.com/js/js_window_navigator.asp
    """
    return JsString.JsString("navigator.product", isPyData=False)

  @property
  def appVersion(self):
    """
    Description:
    ------------
    The appVersion property returns version information about the browser.

    Related Pages:

      https://www.w3schools.com/js/js_window_navigator.asp
    """
    return JsString.JsString("navigator.appVersion", isPyData=False)

  @property
  def cookieEnabled(self):
    """
    Description:
    ------------
    """
    return JsString.JsString("navigator.cookieEnabled", isPyData=False)

  @property
  def onLine(self):
    """
    Description:
    ------------
    The onLine property returns true if the browser is online.

    Related Pages:

      https://www.w3schools.com/js/js_window_navigator.asp
    """
    return JsBoolean.JsBoolean("navigator.onLine", isPyData=False)

  @property
  def platform(self):
    """
    Description:
    ------------
    The platform property returns the browser platform (operating system).

    Related Pages:

      https://www.w3schools.com/js/js_window_navigator.asp
    """
    return JsString.JsString("navigator.platform", isPyData=False)

  @property
  def userAgent(self):
    """
    Description:
    ------------
    The userAgent property returns the user-agent header sent by the browser to the server.

    Related Pages:

      https://www.w3schools.com/js/js_window_navigator.asp

    """
    return JsString.JsString("navigator.userAgent", isPyData=False)

  def javaEnabled(self):
    """
    Description:
    ------------
    The javaEnabled() method returns a Boolean value that specifies whether the browser has Java enabled.

    Related Pages:

      https://www.w3schools.com/jsref/met_nav_javaenabled.asp
    """
    return JsBoolean.JsBoolean("navigator.javaEnabled()", isPyData=False)
