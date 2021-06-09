
import json

from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage

# All the predefined variable types
from epyk.core.js.fncs import JsFncs


JQUERY_ALIAS = "$"


def decorate_var(var_name, convert_var=True):
  """
  Return the String Jquery variable reference for a given component id

  :param var_name: String. The variable name
  :param convert_var: Boolean.

  :return: The decorated Jquery reference
  """
  if not convert_var:
    return '%s(%s)' % (JQUERY_ALIAS, var_name)

  return '%s(%s)' % (JQUERY_ALIAS, JsUtils.jsConvertData(var_name, None))


class Jsjqxhr:

  def __init__(self, ajax):
    self.__ajax = {'request': ajax}
    self.profile = False

  def done(self, jsFncs):
    """
    AJAX Function

    An alternative construct to the success callback option, refer to deferred.done() for implementation details

    Related Pages:

      https://api.jquery.com/jQuery.ajax/#jqXHR

    :param jsFncs: The Javascript Functions

    :return:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__ajax.setdefault("done", []).extend(jsFncs)
    return self

  def fail(self, jsFncs):
    """
    AJAX Function

    An alternative construct to the error callback option, the .fail() method replaces the deprecated .error() method

    Related Pages:

      https://api.jquery.com/jQuery.ajax/#jqXHR

    :param jsFncs: The Javascript Functions

    :return:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__ajax.setdefault("fail", []).extend(jsFncs)
    return self

  def always(self, jsFncs):
    """
    AJAX Function

    An alternative construct to the complete callback option

    Related Pages:

      https://api.jquery.com/jQuery.ajax/#jqXHR

    :param jsFncs: The Javascript Functions

    :return:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__ajax.setdefault("always", []).extend(jsFncs)
    return self

  def toStr(self):
    """
    Javascript representation

    :return: Return the Javascript String
    """
    reqResult = [self.__ajax['request']]
    for rType in ["done", "fail", "always"]:
      if self.__ajax.get(rType) is not None:
        reqResult.append("%s(function(){%s})" % (
          rType, JsUtils.jsConvertFncs(self.__ajax[rType], toStr=True, profile=self.profile)))
    return ".".join(map(lambda x: str(x), reqResult))


class JQuery(JsPackage):
  """
  Jquery wrapper.
  for more details about the different available functions go on the website: https://jquery.com/
  In order to avoid conflict with any other libraries the $ will not be used in this framework.
  Any JQuery reference will be done using the proper name of the library jQuery()

  Documentation:
    - https://www.w3schools.com/jquery/
    - https://www.w3schools.com/jquery/jquery_noconflict.asp
    - https://www.w3schools.com/jquery/jquery_ref_ajax.asp

  """
  lib_alias = {"js": 'jquery'}
  lib_selector = 'jQuery("body")'

  def this(self, reference=None):
    """
    Description:
    -----------
    Force the selector to be this or a specific reference.
    This feature can be useful in functions.

    Attributes:
    ----------
    :param reference: The Jquery reference to be used instead example #MyId

    :return: The Jquery Python object
    """
    if len(self._js) > 0:
      raise Exception("Selector can only be changed first")

    if reference is None:
      self._selector = "jQuery(this)"
    else:
      self._selector = "jQuery('%s')" % reference
    return self

  def new(self, tag=None, reference=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param tag:
    :param reference:
    """
    if len(self._js) > 0:
      raise Exception("Selector can only be changed first")

    if tag is None and reference is None:
      raise Exception("Tag or / and Reference must be defined")

    if tag is None and reference is not None:
      self._selector = "jQuery('%s')" % reference
    else:
      if reference is not None:
        self._selector = "jQuery('<%s id=\\'%s\\'></%s>')" % (tag, reference, tag)
      else:
        self._selector = "jQuery('<%s></%s>')" % (tag, tag)
    return self

  def parseHTML(self, text, context=None, keepScripts=False):
    """
    Description:
    -----------
    Parses a string into an array of DOM nodes.

      https://api.jquery.com/jquery.parsehtml/

    Attributes:
    ----------
    :param text: HTML string to be parsed.
    :param context: Document element to serve as the context in which the HTML fragment will be created.
    :param keepScripts: A Boolean indicating whether to include scripts passed in the HTML string.
    """
    text = JsUtils.jsConvertData(text, None)
    return "%s.parseHTML(%s)" % (JQUERY_ALIAS, text)

  def toggle(self, speed=None, easing=None, jsCallback=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param speed:
    :param easing:
    :param jsCallback:
    """
    return self.fnc("toggle()")

  def trigger(self, jsData, jsFnc=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsData:
    :param jsFnc:
    """
    jsData = JsUtils.jsConvertData(jsData, jsFnc)
    return self.fnc("trigger(%(jsData)s)" % {"jsData": jsData})

  def hide(self, speed=None, callback=None):
    """
    Description:
    -----------

    Related Pages:

      https//www.w3schools.com/jquery/jquery_hide_show.asp
      http://api.jquery.com/hide/

    Attributes:
    ----------
    :param speed:
    :param callback:
    """
    if speed is not None:
      if callback is not None:
        if not isinstance(callback, list):
          callback = [callback]
        jqFnc = "hide(%(speed)s, function(){%(callback)s})" % {'speed': speed,  'callback': ";".join(callback)}
      else:
        jqFnc = "hide(%(speed)s)" % {'speed': speed}
    else:
      jqFnc = "hide()"
    return self.fnc(jqFnc)

  def show(self, speed=None, callback=None):
    """
    Description:
    -----------

    Related Pages:

      https//www.w3schools.com/jquery/jquery_hide_show.asp
      http://api.jquery.com/show/

    Attributes:
    ----------
    :param speed:
    :param callback:
    """
    if speed is not None:
      if callback is not None:
        if not isinstance(callback, list):
          callback = [callback]
        jqFnc = "show(%(speed)s, function(){%(callback)s})" % {'speed': speed, 'callback': ";".join(callback)}
      else:
        jqFnc = "show(%(speed)s)" % {'speed': speed}
    else:
      jqFnc = "show()"
    return self.fnc(jqFnc)

  def fadeIn(self, speed=None, callback=None):
    """
    Description:
    -----------

    Related Pages:

      https//www.w3schools.com/jquery/jquery_fade.asp
      http://api.jquery.com/fadein/

    Attributes:
    ----------
    :param speed:
    :param callback:

    :return:
    """
    if speed is not None:
      if callback is not None:
        if not isinstance(callback, list):
          callback = [callback]
        jqFnc = "fadeIn(%(speed)s, function(){%(callback)s})" % {'speed': speed, 'callback': ";".join(callback)}
      else:
        jqFnc = "fadeIn(%(speed)s)" % {'speed': speed}
    else:
      jqFnc = "fadeIn()"
    return self.fnc(jqFnc)

  def fadeOut(self, speed=None, callback=None):
    """
    Description:
    -----------

    Related Pages:

      https//www.w3schools.com/jquery/jquery_fade.asp
      http://api.jquery.com/fadeout/

    Attributes:
    ----------
    :param speed:
    :param callback:
    """
    if speed is not None:
      if callback is not None:
        if not isinstance(callback, list):
          callback = [callback]
        jqFnc = "fadeOut(%(speed)s, function(){%(callback)s})" % {'speed': speed, 'callback': ";".join(callback)}
      else:
        jqFnc = "fadeOut(%(speed)s)" % {'speed': speed}
    else:
      jqFnc = "fadeOut()"
    return self.fnc(jqFnc)

  def fadeToggle(self, speed=None, callback=None):
    """
    Description:
    -----------

    Documentation:
      - https://www.w3schools.com/jquery/jquery_fade.asp

    Attributes:
    ----------
    :param speed:
    :param callback:
    """
    if speed is not None:
      if callback is not None:
        if not isinstance(callback, list):
          callback = [callback]
        jqFnc = "fadeToggle(%(speed)s, function(){%(callback)s})" % {'speed': speed, 'callback': ";".join(callback)}
      else:
        jqFnc = "fadeToggle(%(speed)s)" % {'speed': speed}
    else:
      jqFnc = "fadeToggle()"
    return self.fnc(jqFnc)

  def fadeTo(self, duration, opacity, easing=None, complete=None):
    """
    Description:
    -----------
    Adjust the opacity of the matched elements.

    Related Pages:

      https//www.w3schools.com/jquery/jquery_fade.asp
      https://api.jquery.com/fadeto/

    Attributes:
    ----------
    :param duration: A string or number determining how long the animation will run.
    :param opacity: A number between 0 and 1 denoting the target opacity.
    :param easing: A string indicating which easing function to use for the transition.
    :param complete: A function to call once the animation is complete.
    """
    if complete is not None:
      if not isinstance(complete, list):
        complete = [complete]
      complete = "function(){%s}" % ";".join(complete)
    if easing is not None:
      if complete is not None:
        jqFnc = "fadeTo(%(speed)s, %(opacity)s, %(easing)s, %(callback)s)" % {'speed': duration, 'opacity': opacity, 'easing': easing, 'callback': complete}
      else:
        jqFnc = "fadeTo(%(speed)s, %(opacity)s, %(easing)s)" % {'speed': duration, 'opacity': opacity, 'easing': easing}
    elif complete is not None:
      jqFnc = "fadeTo(%(speed)s, %(opacity)s, %(complete)s)" % {'speed': duration, 'opacity': opacity, 'complete': complete}
    else:
      jqFnc = "fadeTo(%(speed)s, %(opacity)s)" % {'speed': duration, 'opacity': opacity}
    return self.fnc(jqFnc)

  def slideDown(self, speed=None, callback=None):
    """
    Description:
    -----------
    Display the matched elements with a sliding motion.

    Related Pages:

      https//www.w3schools.com/jquery/jquery_slide.asp
      https://api.jquery.com/slideDown/#slideDown-duration-complete

    Attributes:
    ----------
    :param speed: A string or number determining how long the animation will run.
    :param callback: A string indicating which easing function to use for the transition.
    """
    if speed is not None:
      if callback is not None:
        if not isinstance(callback, list):
          callback = [callback]
        jqFnc = "slideDown(%(speed)s, function(){%(callback)s})" % {'speed': speed, 'callback': ";".join(callback)}
      else:
        jqFnc = "slideDown(%(speed)s)" % {'speed': speed}
    else:
      jqFnc = "slideDown()"
    return self.fnc(jqFnc)

  def slideUp(self, speed=None, callback=None):
    """
    Description:
    -----------
    Hide the matched elements with a sliding motion.

    Related Pages:

      https//www.w3schools.com/jquery/jquery_slide.asp
      https://api.jquery.com/slideUp/#slideUp-duration-complete

    Attributes:
    ----------
    :param speed: A string or number determining how long the animation will run.
    :param callback: A function to call once the animation is complete, called once per matched element
    """
    if speed is not None:
      if callback is not None:
        if not isinstance(callback, list):
          callback = [callback]
        jqFnc = "slideUp(%(speed)s, function(){%(callback)s})" % {'speed': speed, 'callback': ";".join(callback)}
      else:
        jqFnc = "slideUp(%(speed)s)" % {'speed': speed}
    else:
      jqFnc = "slideUp()"
    return self.fnc(jqFnc)

  def slideToggle(self, speed=None, callback=None):
    """
    Description:
    -----------
    Display or hide the matched elements with a sliding motion.

    Related Pages:

      https//www.w3schools.com/jquery/jquery_slide.asp
      https://api.jquery.com/slideToggle/#slideToggle-duration-complete

    Attributes:
    ----------
    :param speed: A string or number determining how long the animation will run.
    :param callback: A function to call once the animation is complete, called once per matched element.
    """
    if speed is not None:
      if callback is not None:
        if not isinstance(callback, list):
          callback = [callback]
        jqFnc = "slideToggle(%(speed)s, function(){%(callback)s})" % {'speed': speed, 'callback': ";".join(callback)}
      else:
        jqFnc = "slideToggle(%(speed)s)" % {'speed': speed}
    else:
      jqFnc = "slideToggle()"
    return self.fnc(jqFnc)

  def animate(self, params, speed=400, easing='swing', callback=None):
    """
    Description:
    -----------
    Perform a custom animation of a set of CSS properties.

    Usage::

      myObj.animate(0.25, "+=50")

    Related Pages:

      https://www.w3schools.com/jquery/jquery_animate.asp
      https://api.jquery.com/animate/#animate-properties-duration-easing-complete

    Attributes:
    ----------
    :param params: An object of CSS properties and values that the animation will move toward.
    :param speed: A string or number determining how long the animation will run.
    :param easing: A string indicating which easing function to use for the transition.
    :param callback: A function to call once the animation is complete, called once per matched element.
    """
    easing = JsUtils.jsConvertData(easing, None)
    if callback is not None:
      return self.fnc("animate(%s, %s, %s, %s)" % (params, speed, easing, callback))

    return self.fnc("animate(%s, %s, %s)" % (params, speed, easing))

  def stop(self, stopAll=False, goToEnd=False):
    """
    Description:
    -----------
    Stop the currently-running animation on the matched elements.

    Related Pages:

      https//www.w3schools.com/jquery/jquery_stop.asp
      https://api.jquery.com/stop/#stop-clearQueue-jumpToEnd

    Attributes:
    ----------
    :param stopAll: A Boolean indicating whether to remove queued animation as well
    :param goToEnd: A Boolean indicating whether to complete the current animation immediately
    """
    stopAll = JsUtils.jsConvertData(stopAll, None)
    goToEnd = JsUtils.jsConvertData(goToEnd, None)
    return self.fnc("stop(%(stopAll)s, %(goToEnd)s)" % {'stopAll': stopAll, 'goToEnd': goToEnd})

  def remove(self, selector=None):
    """
    Description:
    -----------
    Remove the set of matched elements from the DOM.

    Related Pages:

      https//www.w3schools.com/jquery/jquery_dom_remove.asp
      https://api.jquery.com/remove/#remove-selector

    Attributes:
    ----------
    :param selector: A selector expression that filters the set of matched elements to be removed.
    """
    if selector is not None:
      selector = JsUtils.jsConvertData(selector, None)
      return self.fnc("remove(%s)" % selector)

    return self.fnc("remove()")

  def empty(self):
    """
    Description:
    -----------
    Remove all child nodes of the set of matched elements from the DOM.

    Related Pages:

      https//www.w3schools.com/jquery/jquery_dom_remove.asp
      https://api.jquery.com/empty/#empty
    """
    return self.fnc("empty()")

  def siblings(self, selector=None):
    """
    Description:
    -----------
    Get the siblings of each element in the set of matched elements, optionally filtered by a selector.

    Related Pages:

      https//www.w3schools.com/jquery/jquery_traversing_siblings.asp
      https://api.jquery.com/siblings/#siblings-selector

    Attributes:
    ----------
    :param selector: A string containing a selector expression to match elements against.
    """
    if selector is not None:
      selector = JsUtils.jsConvertData(selector, None)
      return self.fnc("siblings(%s)" % selector)

    return self.fnc("siblings()")

  def next(self, selector=None):
    """
    Description:
    -----------
    Get the immediately following sibling of each element in the set of matched elements.
    If a selector is provided, it retrieves the next sibling only if it matches that selector.

    Related Pages:

      https//www.w3schools.com/jquery/jquery_traversing_siblings.asp
      https://api.jquery.com/next/#next-selector

    Attributes:
    ----------
    :param selector: A string containing a selector expression to match elements against.
    """
    if selector is not None:
      selector = JsUtils.jsConvertData(selector, None)
      return self.fnc("next(%s)" % selector)

    return self.fnc("next()")

  def prev(self, selector=None):
    """
    Description:
    -----------
    Get the immediately preceding sibling of each element in the set of matched elements.
    If a selector is provided, it retrieves the previous sibling only if it matches that selector.

    Related Pages:

      https//www.w3schools.com/jquery/jquery_traversing_siblings.asp
      https://api.jquery.com/prev/#prev-selector

    Attributes:
    ----------
    :param selector: A string containing a selector expression to match elements against.
    """
    if selector is not None:
      selector = JsUtils.jsConvertData(selector, None)
      return self.fnc("prev(%s)" % selector)

    return self.fnc("prev()")

  def first(self):
    """
    Description:
    -----------
    The first() method returns the first element of the specified elements.

    Related Pages:

      https//www.w3schools.com/jquery/jquery_traversing_filtering.asp
      https://api.jquery.com/first/#first
    """
    return self.fnc("first()")

  def children(self, selector=None):
    """
    The children() method returns all direct children of the selected element

    Related Pages:

      https//www.w3schools.com/jquery/traversing_children.asp

    Attributes:
    ----------
    :param selector: Optional. Specifies a selector expression to narrow down the search for children
    """
    if selector is None:
      return self.fnc("children()")

    return self.fnc("children(%s)" % selector)

  def last(self):
    """
    Description:
    -----------
    The last() method returns the last element of the specified element

    Related Pages:

      https//www.w3schools.com/jquery/jquery_traversing_filtering.asp
    """
    return self.fnc("last()")

  def appendTo(self, dstJqId, jsFnc=None):
    """
    Description:
    -----------
    Insert every element in the set of matched elements to the end of the target.

    Attributes:
    ----------
    :param dstJqId: A selector, element, HTML string, array of elements, or jQuery object; the matched set of elements will be inserted at the end of the element(s) specified by this parameter.
    :param jsFnc:

    :rtype: str
    """
    return self.fnc("appendTo(%(dstJqId)s)" % {'dstJqId': JsUtils.jsConvertData(dstJqId, jsFnc)})

  def append(self, dstJqId, jsFnc=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param dstJqId:
    :param jsFnc:

    :rtype: str
    """
    return self.fnc("append(%(dstJqId)s)" % {'dstJqId': JsUtils.jsConvertData(dstJqId, jsFnc)})

  def prepend(self, jsData, jsFnc=None):
    """
    Description:
    -----------
    Insert content, specified by the parameter, to the beginning of each element in the set of matched elements.

    Related Pages:

      https://api.jquery.com/prepend/#prepend-content-content

    Attributes:
    ----------
    :param jsData:
    :param jsFnc:
    """
    return self.fnc("prepend(%(data)s)" % {"data": JsUtils.jsConvertData(jsData, jsFnc)})

  def eq(self, i):
    """
    Description:
    -----------
    The eq() method returns an element with a specific index number of the selected elements.

    Documentation:

      - https://www.w3schools.com/jquery/jquery_traversing_filtering.asp

    Attributes:
    ----------
    :param i: The index numbers start at 0, so the first element will have the index number 0 and not 1
    """
    return self.fnc("eq(%(index)s)" % {'index': i})

  def filter(self, selector=None):
    """
    Description:
    -----------

    :return:
    """

  def _not(self):
    """
    Description:
    -----------

    """

  def find(self, criteria):
    """
    Description:
    -----------
    Get the descendants of each element in the current set of matched elements, filtered by a selector, jQuery object, or element.

    Related Pages:

      https://api.jquery.com/find/#entry-examples

    Attributes:
    ----------
    :param criteria: Selector or element An element or a jQuery object to match elements against.
    """
    criteria = JsUtils.jsConvertData(criteria, None)
    return self.fnc("find(%s)" % criteria)

  def each(self, jsFncs, profile=None):
    """
    Description:
    ------------
    Iterate over a jQuery object, executing a function for each matched element.

    Related Pages:

      https://api.jquery.com/each/#each-function

    Attributes:
    ----------
    :param jsFncs: A function to execute for each matched element.
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile)
    return self.fnc("each(function(index, data){%s})" % jsFncs)

  def css(self, key, value=None):
    """
    Description:
    ------------
    Hook directly into jQuery to override how particular CSS properties are retrieved or set, normalize CSS property
    naming, or create custom properties.

    Related Pages:

      https://api.jquery.com/jQuery.cssHooks/#jQuery-cssHooks1

    Attributes:
    ----------
    :param key:
    :param value:
    """
    if hasattr(self.src, "style"):
      self.src.style.css(key, value)
      return self

    else:
      if value is None:
        return self.fnc("css(%s)" % JsUtils.jsConvertData(key, None))

      return self.fnc("css('%s', %s)" % (key, JsUtils.jsConvertData(value, None)))

  def attr(self, key, value):
    """
    Description:
    ------------
    Get the value of an attribute for the first element in the set of matched elements.

    Related Pages:

      https://api.jquery.com/attr/#attr-attributeName

    Attributes:
    ----------
    :param key: The name of the attribute to get.
    :param value: A value to set for the attribute. If null, the specified attribute will be removed
    """
    if key.lower() in ["style", 'class']:
      raise Exception("Only the css() function can be used to change the style")

    self.src._attrs[key] = value
    return self.src

  def val(self, jsData=None, jsFnc=None):
    """
    Description:
    ------------
    Get the current value of the first element in the set of matched elements.

    Related Pages:

      https://api.jquery.com/val/#val

    Attributes:
    ----------
    :param jsData:
    :param jsFnc:
    """
    if jsData is None:
      return self.fnc("val()")

    return self.fnc("val(%s)" % JsUtils.jsConvertData(jsData, jsFnc))

  def text(self, jsData, jsFnc=None):
    """
    Description:
    ------------
    Get the combined text contents of each element in the set of matched elements, including their descendants, or set the text contents of the matched elements.

    Related Pages:

      https://api.jquery.com/text/#text

    Attributes:
    ----------
    :param jsData:
    :param jsFnc:
    """
    if jsData is None:
      return self.fnc("text()")

    jsData = JsUtils.jsConvertData(jsData, jsFnc)
    return self.fnc("text(%s)" % jsData)

  def html(self, jsData=None, jsFnc=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsData:
    :param jsFnc:
    """
    if jsData is None:
      return self.fnc("html()")

    return self.fnc("html(%s)" % JsUtils.jsConvertData(jsData, jsFnc))

  def toggleClass(self, clsName, propagate=False):
    """
    Description:
    ------------

    Attributes:
    ----------


    :rtype: str
    """
    if propagate:
      self.fnc_closure('parentNode.childNodes.forEach(function(e){e.classList.remove("%(data)s")})' % {'data': clsName})
    return self.fnc('toggleClass("%(data)s")' % {'data': clsName})

  def addClass(self, clsName, attrs=None, eventAttrs=None):
    """
    Description:
    ------------
    Adds the specified class(es) to each element in the set of matched elements.

    This function can either use an existing class or create one if the attrs or eventAttrs are defined

    Attributes:
    ----------
    :param clsName: The Css classname
    :param attrs: A python dictionary with the css attributes
    :param eventAttrs: A nested python dictionary with the css attributes for each events
    """
    if attrs is not None or eventAttrs is not None:
      clsName = self.src.style.cssName(clsName)
      self.src.style.cssCls(clsName, attrs, eventAttrs, False)
    return self.fnc('addClass("%s")' % clsName)

  def getJSON(self, url, jsData, success, dataType='json', jsDataKey=None, isPyData=True, jsFnc=None, profile=None):
    """
    Description:
    ------------
    Load JSON-encoded data from the server using a GET HTTP request.

    Related Pages:

      https//api.jquery.com/jQuery.getJSON/#jQuery-getJSON-url-data-success

    Attributes:
    ----------
    """
    success = JsUtils.jsConvertFncs(success, toStr=True, profile=profile)
    jsData = JsUtils.jsConvert(jsData, jsDataKey, isPyData, jsFnc)
    return Jsjqxhr("jQuery.getJSON('%s', {data: JSON.stringify(%s)}, function(data) {%s}, '%s')" % (
      url, jsData, success, dataType))

  def getJsScript(self, url, jsData, success, dataType='json', jsDataKey=None, isPyData=True, jsFnc=None, profile=None):
    """
    Description:
    ------------
    Load a JavaScript file from the server using a GET HTTP request, then execute it.

    Related Pages:

      https//api.jquery.com/jQuery.getScript/

    Attributes:
    ----------
    :param url:
    :param jsData:
    :param success:
    :param dataType:
    :param jsDataKey:
    :param isPyData:
    :param jsFnc:
    """
    success = JsUtils.jsConvertFncs(success, toStr=True, profile=profile)
    jsData = JsUtils.jsConvert(jsData, jsDataKey, isPyData, jsFnc)
    return Jsjqxhr("jQuery.getScript('%s', {data: JSON.stringify(%s)}, function(data, textStatus, jqxhr) {%s}, '%s')" % (
      url, jsData, success, dataType))

  def getPyScript(self, script, data=None, successFncs=None, options=None, timeout=None, props=None):
    """
    Description:
    ------------

    Related Pages:

      https//api.jquery.com/jQuery.getJSON/#jQuery-getJSON-url-data-success

    Attributes:
    ----------
    :param script:
    :param jsData:
    :param success:
    :param dataType:
    :param jsDataKey:
    :param isPyData:
    :param jsFnc:
    """

    if not hasattr(self.src, "aresObj"):
      if not hasattr(self.src, "run"):
        raise Exception("Cannot work without a proper rptObj")

      else:
        rptObj = self.src
    else:
      rptObj = self.src._report
    if data is None:
      data = {}
    qParams = self.getParams('%s/data/%s/%s' % (
      rptObj._urlsApp['report'], rptObj.run.report_name, script.replace(".py", "")), data, successFncs, None, options,
                             timeout, props)
    return Jsjqxhr("jQuery.post(%s)" % qParams)

  def load(self, url, jsData=None, successFncs=None, profile=None):
    """
    Description:
    ------------
    Load data from the server and place the returned HTML into the matched elements.

    Usage::

      div.dom.jquery.load(r"./report_list.html")

    Related Pages:

      https://api.jquery.com/load/#load-url-data-complete

    Attributes:
    ----------
    :param url: A string containing the URL to which the request is sent.
    :param jsData: A plain object or string that is sent to the server with the request.
    :param successFncs: A callback function that is executed when the request completes.
    """
    url = JsUtils.jsConvertData(url, None)
    if successFncs is None:
      if jsData is None:
        return "%s.load(%s)" % (self.varId, url)
      return "%s.load(%s, {data: JSON.stringify(%s)})" % (self.varId, url, jsData)

    str_fncs = JsUtils.jsConvertFncs(successFncs, toStr=True, profile=profile)
    if jsData is None:
      return "%s.load(%s, function(data) {%s})" % (self.varId, url, str_fncs)

    return "%s.load(%s, {data: JSON.stringify(%s)}, function(data) {%s})" % (self.varId, url, jsData, str_fncs)

  def ajaxError(self, jsFncs, profile=False):
    """
    Description:
    ------------

    Related Pages:

      https://api.jquery.com/ajaxError/

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile)
    return "jQuery(document).ajaxError(function(event, jqxhr, settings, thrownError) {%s})" % jsFncs

  def ajaxStart(self, jsFncs, profile=None):
    """
    Description:
    ------------
    Register a handler to be called when the first Ajax request begins. This is an Ajax Event.

    Related Pages:

      https://api.jquery.com/ajaxStart/

    Attributes:
    ----------
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile)
    return "jQuery(document).ajaxStart(function() {%s})" % jsFncs

  def ajaxStop(self, jsFncs, profile=None):
    """
    Description:
    ------------
    Register a handler to be called when all Ajax requests have completed. This is an Ajax Event.

    Related Pages:

      https://api.jquery.com/ajaxStop/

    Attributes:
    ----------
    :param jsFncs:
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile)
    return "jQuery(document).ajaxStop(function() {%s})" % jsFncs

  def ajaxSuccess(self, jsFncs, profile=None):
    """
    Description:
    ------------
    Attach a function to be executed whenever an Ajax request completes successfully. This is an Ajax Event.

    Related Pages:

      https://api.jquery.com/ajaxSuccess/

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile)
    return "jQuery(document).ajaxSuccess(function(event, xhr, settings) {%s})" % jsFncs

  def ajaxSend(self, jsFncs, profile=None):
    """
    Description:
    ------------

    Related Pages:

      https://api.jquery.com/ajaxSend/

    Attributes:
    ----------
    :param profile:
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile)
    return "jQuery(document).ajaxSend(function(event, jqxhr, settings) {%s})" % jsFncs

  def ajaxComplete(self, jsFncs, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile)
    return "jQuery(document).ajaxComplete(function() {%s})" % jsFncs

  def getParams(self, url, data, successFncs, errorFncs, options, timeout, props, profile=None):
    """

    Attributes:
    ----------

    :return:
    """
    ajaxData = []
    if props is not None:
      data["_system"] = props
    if options is not None:
      for k, v in options.items():
        ajaxData.append("%s: %s" % (k, json.dumps(v)))
    ajaxData.extend(["data: {data: JSON.stringify(%s)}" % data, "url: '%s'" % url])
    if timeout is not None:
      ajaxData.append("timeout: %s" % timeout)
    if successFncs is not None:
      ajaxData.append("success: function(result,status,xhr){%s}" % JsUtils.jsConvertFncs(
        successFncs, toStr=True, profile=profile))
    if errorFncs is not None:
      ajaxData.append("error: function(xhr, status, error){%s}" % JsUtils.jsConvertFncs(
        errorFncs, toStr=True, profile=profile))
    return "{%s}" % ", ".join(ajaxData)

  def get(self, url, data, successFncs=None, options=None, timeout=None, props=None):
    """
    Description:
    ------------
    Load data from the server using a HTTP GET request.

    Documentation:
      - https://www.w3schools.com/jquery/jquery_ajax_get_post.asp

    Attributes:
    ----------
    """
    return Jsjqxhr("jQuery.get(%s)" % self.getParams(url, data, successFncs, None, options, timeout, props))

  def post(self, url, data=None, successFncs=None, options=None, timeout=None, props=None):
    """
    Description:
    ------------
    Load data from the server using a HTTP POST request.

    Documentation:
      - https://www.w3schools.com/jquery/jquery_ajax_get_post.asp

    Attributes:
    ----------
    :rtype: Jsjqxhr

    :return:
    """
    data = data or {}
    return Jsjqxhr("jQuery.post(%s)" % self.getParams(url, data, successFncs, None, options, timeout, props))

  def ajax(self, type, url, data=None, successFncs=None, errorFncs=None, options=None, timeout=None, props=None):
    """
    Description:
    ------------
    The ajax() method is used to perform an AJAX (asynchronous HTTP) request.

    Example


    Related Pages:

      https//www.w3schools.com/jquery/ajax_ajax.asp

    Attributes:
    ----------
    :param type: Specifies the type of request. (GET or POST)
    :param url: Specifies the URL to send the request to. Default is the current page
    :param data: Specifies data to be sent to the server
    :param successFncs: A function to be run when the request succeeds
    :param errorFncs: A function to run if the request fails.
    :param options: The other parameters specifies one or more name/value pairs for the AJAX request
    :param timeout: The local timeout (in milliseconds) for the request
    """
    if type.upper() not in ['POST', 'GET']:
      raise Exception("Method %s not recognised" % url)

    data = data or {}
    return Jsjqxhr("jQuery.ajax(%s)" % self.getParams(url, data, successFncs, errorFncs, options, timeout, props))

  def click(self, jsFnc, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFnc:

    :return:
    """
    self.css("cursor", "pointer")
    return self.fnc("click(function(){%s})" % JsUtils.jsConvertFncs(jsFnc, toStr=True, profile=profile))
