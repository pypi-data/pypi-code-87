#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

from epyk.core.html import Html
from epyk.core.html.options import OptSliders
from epyk.core.html.options import OptList

from epyk.core.html.entities import EntHtml4

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlJqueryUI
from epyk.core.js.html import JsHtmlList
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsQueryUi
from epyk.core.js.packages import JsComponents

# The list of CSS classes
from epyk.core.css.styles import GrpClsJqueryUI


class ProgressBar(Html.Html):
  requirements = ('jqueryui', )
  name = 'Progress Bar'
  _option_cls = OptSliders.OptionsProgBar

  def __init__(self, report, number, total, width, height, helper, options, html_code, profile):
    options['max'] = total
    super(ProgressBar, self).__init__(report, number, html_code=html_code, profile=profile, options=options,
                                      css_attrs={"width": width, "height": height, 'box-sizing': 'border-box'})
    self.add_helper(helper)
    self.options.background = self._report.theme.success[1]

  @property
  def options(self):
    """
    Description:
    -----------
    The progress bar is designed to display the current percent complete for a process.
    The bar is coded to be flexibly sized through CSS and will scale to fit inside its parent container by default.

    Related Pages:

      https://api.jqueryui.com/progressbar

    :rtype: OptSliders.OptionsProgBar
    """
    return super().options

  def to(self, number, timer=10):
    """
    Description:
    ------------
    Move the progress bar to a defined level in a specific amount of time in millisecond.

    Attributes:
    ----------
    :param number: Number. The final state for the progress bar.
    :param timer: Integer. Optional. the appended of the increase in millisecond.
    """
    self._report.body.onReady([
      self._report.js.objects.number(self.val, varName="%s_counter" % self.htmlCode, setVar=True),
      self._report.js.window.setInterval([
        self._report.js.if_(
          self._report.js.objects.number.get("window.%s_counter" % self.htmlCode) < number, [
            self._report.js.objects.number(
              self._report.js.objects.number.get("window.%s_counter" % self.htmlCode) + 1,
              varName="window.%s_counter" % self.htmlCode, setVar=True),
            self.build(self._report.js.objects.number.get("window.%s_counter" % self.htmlCode))
          ]).else_(self._report.js.window.clearInterval("%s_interval" % self.htmlCode))
      ], "%s_interval" % self.htmlCode, timer)
    ])
    return self

  _js__builder__ = '''
      options.value = parseFloat(data);
      %(jqId)s.progressbar(options).find('div').attr("data-toggle", "tooltip").attr("title", ""+ (parseFloat(data) / options.max * 100).toFixed(2) +"%% ("+ parseFloat(data) +" / "+ options.max +")").css(options.css);
      ''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

  @property
  def js(self):
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Related Pages:

      https://api.jqueryui.com/progressbar

    :return: A Javascript Dom object

    :rtype: JsQueryUi.ProgressBar
    """
    if self._js is None:
      self._js = JsQueryUi.ProgressBar(self, report=self._report)
    return self._js

  @property
  def dom(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlProgressBar
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlProgressBar(self, report=self._report)
    return self._dom

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<div %s></div>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)


class Menu(Html.Html):
  requirements = ('jqueryui', )
  name = 'Menu'
  _option_cls = OptSliders.OptionsMenu

  def __init__(self, report, records, width, height, helper, options, html_code, profile):
    super(Menu, self).__init__(report, records, html_code=html_code, profile=profile, options=options,
                               css_attrs={"width": width, "height": height})
    self.add_helper(helper)
    self.style.css.display = 'block'
    self.style.css.position = 'relative'

  @property
  def style(self):
    """
    Description:
    -----------
    Property to the CSS Style of the component.

    :rtype: rpClsJqueryUI.ClassMenu
    """
    if self._styleObj is None:
      self._styleObj = GrpClsJqueryUI.ClassMenu(self)
    return self._styleObj

  @property
  def options(self):
    """
    Description:
    -----------
    Property to the comments component options.
    Optional can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    Related Pages:

      https://api.jqueryui.com/menu

    :rtype: OptSliders.OptionsMenu
    """
    return super().options

  _js__builder__ = '''
      var jqHtmlObj = jQuery(htmlObj); if (options.clearDropDown) {jqHtmlObj.empty()};
      var isRoot =  options.isRoot; if(typeof isRoot === 'undefined'){isRoot = true}
      data.forEach(function(rec){
        if (rec.items != undefined) {
          var li = $('<li></li>'); var div = $('<div>'+ rec.value +'</div>');
          li.append(div); var ul = $('<ul aria-hidden="true"></ul>'); 
          options.clearDropDown = false; options.isRoot = false;
          options.builder(ul, rec.items, options); li.append(ul); jqHtmlObj.append(li);
        } else {
          var div = $('<div>'+ rec.value +'</div>').css({"width": '150px'}); var li = $('<li></li>');
          li.append(div); jqHtmlObj.append(li)};
      }); if(isRoot){jqHtmlObj.menu(options)}'''

  @property
  def js(self):
    """
    Description:
    -----------
    The Javascript functions defined for this component.
    Those can be specific ones for the module or generic ones from the language.

    Related Pages:

      https://api.jqueryui.com/menu

    :return: A Javascript Dom object

    :rtype: JsQueryUi.Menu
    """
    if self._js is None:
      self._js = JsQueryUi.Menu(self, report=self._report)
    return self._js

  @property
  def dom(self):
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlProgressBar
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlProgressBar(self, report=self._report)
    return self._dom

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<ul %s></ul>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)


class Dialog(Html.Html):
  requirements = ('jqueryui', )
  name = 'Menu'
  _option_cls = OptSliders.OptionDialog

  def __init__(self, report, text, width, height, helper, options, html_code, profile):
    super(Dialog, self).__init__(report, text, css_attrs={"width": width, "height": height}, html_code=html_code,
                                 profile=profile, options=options)
    self.add_helper(helper)
    if hasattr(text, "options"):
      self.components[text.htmlCode] = text
      text.options.managed = False
      self.options.empty = False
      self._vals = ""

  @property
  def options(self):
    """
    Description:
    -----------
    Property to the comments component options.
    Optional can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    Related Pages:

      https://jqueryui.com/dialog/

    :rtype: OptSliders.OptionDialog
    """
    return super().options

  _js__builder__ = '''
    if(options.empty){%(jqId)s.empty()}; 
    %(jqId)s.append('<p>'+ data +'</p>'); %(jqId)s.dialog(options)''' % {
    "jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

  @property
  def js(self):
    """
    Description:
    -----------
    Open content in an interactive overlay.

    Related Pages:

      https://jqueryui.com/dialog/

    :return: A Javascript Dom object

    :rtype: JsQueryUi.Dialog
    """
    if self._js is None:
      self._js = JsQueryUi.Dialog(self, report=self.page)
    return self._js

  @property
  def dom(self):
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlProgressBar
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlProgressBar(self, report=self._report)
    return self._dom

  def __str__(self):
    static_content = []
    for component in self.components.values():
      static_content.append(str(component))
    # TODO Find a fix for this
    if self.options.verbose and "bootstrap" in self.page.jsImports:
      logging.warning("JqueryUI Dialog:")
      logging.warning("This component might have some conflicts with Bootstrap")
      logging.warning(
        "More details https://stackoverflow.com/questions/8681707/jqueryui-modal-dialog-does-not-show-close-button-x")
    self.page.properties.js.add_builders(self.refresh())
    return '<div %s>%s%s</div>' % (
      self.get_attrs(pyClassNames=self.style.get_classes()), "".join(static_content), self.helper)


class Slider(Html.Html):
  requirements = ('jqueryui', )
  name = 'Slider'
  _option_cls = OptSliders.OptionsSlider

  def __init__(self, report, number, min_val, max_val, width, height, helper, options, html_code, profile):
    options.update({'max': max_val, 'min': min_val})
    super(Slider, self).__init__(report, number, html_code=html_code, profile=profile, options=options,
                                 css_attrs={"width": width, "height": height})
    self.style.css.padding = "0 10px"
    self.style.css.margin = "15px 0"
    self.add_helper(helper)

  @property
  def options(self):
    """
    Description:
    ------------
    Property to the comments component options.
    Optional can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptSliders.OptionsSlider
    """
    return super().options

  @property
  def style(self):
    """
    Description:
    ------------
    Property to the CSS Style of the component.

    :rtype: GrpClsJqueryUI.ClassSlider
    """
    if self._styleObj is None:
      self._styleObj = GrpClsJqueryUI.ClassSlider(self)
    return self._styleObj

  @property
  def js(self):
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Related Pages:

      https://api.jqueryui.com/slider

    :return: A Javascript Dom object

    :rtype: JsQueryUi.Slider
    """
    if self._js is None:
      self._js = JsQueryUi.Slider(self, report=self._report)
    return self._js

  def change(self, js_funcs, profile=None, on_ready=False):
    """
    Description:
    -----------
    Triggered after the user slides a handle, if the value has changed;
    or if the value is changed programmatically via the value method.

    Related Pages:

      https://api.jqueryui.com/slider/#event-change

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | String. Optional. A flag to set the component performance storage.
    :param on_ready: Boolean. Optional. Trigger the change event when page is ready.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.options.change("function(event, ui){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))
    return self

  def start(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Triggered when the user starts sliding.

    Related Pages:

      https://api.jqueryui.com/slider/#event-start

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | String. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._jsStyles["start"] = "function(event, ui){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return self

  def slide(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Triggered when the user starts sliding.

    Related Pages:

      https://api.jqueryui.com/slider/#event-slide

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | String. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._jsStyles["slide"] = "function(event, ui){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return self

  def stop(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Triggered after the user slides a handle.

    Related Pages:

      https://api.jqueryui.com/slider/#event-stop

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | String. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._jsStyles["stop"] = "function(event, ui){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return self

  @property
  def dom(self):
    """
    Description:
    -----------
    The Javascript Dom object.

    :rtype: JsHtmlJqueryUI.JsHtmlSlider
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlSlider(self, report=self._report)
    return self._dom

  _js__builder__ = '''options.value = data; %(jqId)s.slider(options).css(options.css)
      ''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '''
      <div %(strAttr)s>
        <div style="width:100%%;height:20px">
          <span style="float:left;display:inline-block">%(min)s</span>
          <span style="float:right;display:inline-block">%(max)s</span>
        </div>
        <div id="%(htmlCode)s"></div>
      </div>%(helper)s''' % {"strAttr": self.get_attrs(withId=False), "min": self.options.min,
                             "htmlCode": self.htmlCode, "max": self.options.max, "helper": self.helper}


class Range(Slider):
  name = "Slider Range"

  _js__builder__ = '''options.values = [Math.min(...data), Math.max(...data)]; %(jqId)s.slider(options).css(options.css)
        ''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}


class SliderDate(Slider):
  name = "Slider Date"

  def __init__(self, report, number, min_val, max_val, width, height, helper, options, html_code, profile):
    super(SliderDate, self).__init__(report, number, min_val, max_val, width, height, helper, options, html_code,
                                     profile)
    self.options.min, self.options.max, self.options.step = min_val, max_val, 86400

  _js__builder__ = '''
      const minDt = new Date(options.min).getTime() / 1000;
      const maxDt = new Date(options.max).getTime() / 1000;      
      options.min = minDt; options.max = maxDt;
      options.value = new Date(data).getTime() / 1000;
      %(jqId)s.slider(options).css(options.css)
      ''' % {"jqId": JsQuery.decorate_var("jQuery(htmlObj)", convert_var=False)}

  @property
  def dom(self):
    """
    Description:
    -----------
    The Javascript Dom object.

    :rtype: JsHtmlJqueryUI.JsHtmlSliderDate
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlSliderDate(self, report=self._report)
    return self._dom


class SliderDates(SliderDate):

  _js__builder__ = '''
      const minDt = new Date(options.min).getTime() / 1000;
      const maxDt = new Date(options.max).getTime() / 1000;
      options.min = minDt; options.max = maxDt;
      options.values = [new Date(data[0]).getTime() / 1000, new Date(data[1]).getTime() / 1000];
      %(jqId)s.slider(options).css(options.css)
      ''' % {"jqId": JsQuery.decorate_var("jQuery(htmlObj)", convert_var=False)}

  @property
  def dom(self):
    """
    Description:
    -----------
    The Javascript Dom object.

    :rtype: JsHtmlJqueryUI.JsHtmlSliderDates
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlSliderDates(self, report=self._report)
    return self._dom


class SkillBar(Html.Html):
  name = 'Skill Bars'
  _option_cls = OptSliders.OptionsSkillbars

  def __init__(self, report, data, y_column, x_axis, title, width, height, html_code, options, profile):
    super(SkillBar, self).__init__(report, "", html_code=html_code, profile=profile, options=options,
                                   css_attrs={"width": width, "height": height})
    self.add_title(title, options={'content_table': False})
    self.innerPyHTML = report.ui.layouts.table(options={"header": False})
    self.innerPyHTML.options.managed = False
    for rec in data:
      value = report.ui.div(EntHtml4.NO_BREAK_SPACE).css(
        {"width": '%s%s' % (rec[y_column], options.get("unit", '%')), 'margin-left': "2px",
         "background": options.get("background", report.theme.success[0])})
      value.options.managed = False
      if options.get("values", False):
        self.innerPyHTML += [rec[x_axis], value, "%s%s" % (int(rec[y_column]), options.get("unit", 'px'))]
        self.innerPyHTML[-1][2].style.css.padding = "0 5px"
      else:
        self.innerPyHTML += [rec[x_axis], value]
      self.innerPyHTML[-1][1].attr["align"] = 'left'
      self.innerPyHTML[-1][0].style.css.padding = "0 5px"
      self.innerPyHTML[-1][1].style.css.width = "100%"
      if options.get("borders", False):
        self.innerPyHTML[-1][1].style.css.border = "1px solid %s" % report.theme.greys[4]
        self.innerPyHTML[-1][1][0].style.css.margin_left = 0
    self.innerPyHTML.style.clear()
    self.css({"margin": '5px 0'})
    self.options.set_thresholds()

  @property
  def options(self):
    """
    Description:
    ------------
    Property to the comments component options.
    Optional can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptSliders.OptionsSkillbars
    """
    return super().options

  @property
  def js(self):
    """
    Description:
    -----------
    The JavaScript predefined functions for this component.

    :return: A Javascript object

    :rtype: JsComponents.SkillBar
    """
    if self._js is None:
      self._js = JsComponents.SkillBar(self, varName=self.dom.varName, report=self.page)
    return self._js

  _js__builder__ = ''' 
      var table = htmlObj.querySelector("table"); table.innerHTML = "";
      var thead = document.createElement("thead"); var tbody = document.createElement("tbody");
      tbody.style["box-sizing"] = "border-box";
      table.appendChild(thead); table.appendChild(tbody);
      data.forEach(function(rec, i){
        var tooltip = "";
        if (typeof rec.tooltip !== "undefined"){var tooltip = rec.tooltip};
        if (typeof rec.url !== "undefined") {
          var content = document.createElement("a"); content.href =  rec.url} 
        else {
          var content = document.createElement("span")};
        content.innerHTML = rec.value.toFixed(2) + "%";
        content.style.whiteSpace = "nowrap";
        var tr = document.createElement("tr");
        tr.style.width = options.width + "px"; tr.title = tooltip;
        var col = document.createElement("td");
        col.style.textAlign = "right"; col.style.padding = "0 5px";
        var p = document.createElement("span"); p.innerHTML = rec.label;
        col.appendChild(p); tr.appendChild(col);
        var row = document.createElement("td");
        row.style["box-sizing"] = "border-box";
        row.style.width = "100%";
        var div = document.createElement("div");
        div.style.width = rec.value.toFixed(2) + "%";
        if( rec.value.toFixed(2) > options.thresholds[1]){ div.style.backgroundColor = options.success}
        else if(rec.value.toFixed(2) > options.thresholds[0]) {div.style.backgroundColor = options.warning}
        else {div.style.backgroundColor = options.danger}
        div.style.fontSize = "10px";
        div.style.lineHeight = "20px";
        div.style.verticalAlign = "middle%";
        div.style.display = "block";
        div.style.paddingLeft = "5px";
        if (options.percentage){ div.appendChild(content)} 
        else { div.innerHTML = "&nbsp;"; div.title = rec.value.toFixed(2) + "%" }
        row.appendChild(div); tr.appendChild(row);
        tbody.appendChild(tr)
      })'''

  def __str__(self):
    for row in self.innerPyHTML:
      percent = int(float(row[1][0].css("width")[:-1]))
      if percent > self.options.thresholds[1]:
        row[1][0].style.css.background = self.options.success
      elif percent > self.options.thresholds[0]:
        row[1][0].style.css.background = self.options.warning
      else:
        row[1][0].style.css.background = self.options.danger
      row[1][0].style.css.line_height = 20
      row[1][0].style.css.font_factor(-4)
      if self.options.percentage:
        row[1][0]._vals = [row[1][0].css("width")]
        row[1][0].style.css.padding_left = 5
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.content)


class OptionsBar(Html.Html):
  requirements = ('font-awesome', )
  name = 'Options'
  _option_cls = OptSliders.OptionBar

  def __init__(self, report, records, width, height, color, options, profile):
    super(OptionsBar, self).__init__(report, [], css_attrs={"width": width, 'height': height},
                                     profile=profile, options=options)
    self.css({'padding': '0', 'display': 'block', 'text-align': 'middle', 'color': color, 'margin-left': '5px',
              'background': self._report.theme.greys[0]})
    for rec in records:
      self += rec
    if self.options.draggable:
      self.draggable()

  @property
  def options(self):
    """
    Description:
    ------------
    Property to the comments component options.
    Optional can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptSliders.OptionBar
    """
    return super().options

  def __add__(self, icon):
    """ Add items to a container """
    icon = self._report.ui.icon(icon)
    icon.style.css.margin = "5px"
    super(OptionsBar, self).__add__(icon)
    return self

  def draggable(self, options=None):
    self.css({'border-radius': '5px', "border": "1px dotted %s" % self._report.theme.success[1]})
    self.page.properties.js.add_builders(self.dom.jquery_ui.draggable(options).toStr())
    return self

  def __str__(self):
    str_html = "".join([v.html() for v in self.val])
    return '<div %(attrs)s>%(icons)s</div>' % {
      'attrs': self.get_attrs(pyClassNames=self.style.get_classes()), 'icons': str_html}


class SignIn(Html.Html):
  requirements = ('font-awesome', )
  name = 'SignIn'

  def __init__(self, report, text, size, icon):
    super(SignIn, self).__init__(report, text, css_attrs={"width": size, 'height': size})
    self.size, self.icon = "%s%s" % (size[0]-8, size[1]), icon
    self.css({"text-align": "center", "padding": 0, 'color': self._report.theme.colors[3],
              "margin": 0, "border-radius": "%s%s" % (size[0], size[1]),
              "border": "1px solid %s" % self._report.theme.colors[3], 'cursor': 'pointer'})

  def __str__(self):
    if not hasattr(self._report, 'user') or self._report.user == 'local':
      self.attr["class"].add(self.icon or "fas fa-user-tie")
      self.style.css.font_family = "Font Awesome 5 Free"
      self.style.css.padding = "2px"
      self.style.css.font_size = self.size
      return '<i title="Guest Mode" %(attrs)s></i>' % {
        'size': self.size, 'attrs': self.get_attrs(pyClassNames=self.style.get_classes())}

    return '''
      <div title="%(user)s" %(attrs)s>
        <p style="font-size:%(size)s;margin-top:-2px">%(letter)s</p>
      </div> ''' % {'size': self.size, 'letter': self._report.user[0].upper(), 'user': self._report.user,
                    'attrs': self.get_attrs(pyClassNames=self.style.get_classes())}


class Filters(Html.Html):
  name = 'Filters'
  requirements = ('font-awesome', )
  _option_cls = OptList.OptionsTagItems

  def __init__(self, report, items, width, height, html_code, helper, options, profile):
    super(Filters, self).__init__(report, items, html_code=html_code, profile=profile, options=options,
                                  css_attrs={"width": width, "min-height": height})
    self.input = self._report.ui.input()
    self.input.style.css.text_align = 'left'
    self.input.style.css.padding = '0 5px'
    self.input.options.managed = False
    self.selections = self._report.ui.div()
    self.selections.options.managed = False
    self.selections.attr["name"] = "panel"
    self.selections.css({'min-height': '30px', 'padding': '5px 2px'})
    self.add_helper(helper)
    self.__enter_def = False

  @property
  def options(self):
    """
    Description:
    -----------
    Property to the comments component options.
    Optional can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptList.OptionsTagItems
    """
    return super().options

  _js__builder__ = '''
      var panel = htmlObj.querySelector('[name=panel]'); panel.innerHTML = '';
      if (typeof data !== 'undefined'){
      data.forEach(function(val){
        if(typeof val === 'string'){
          val = {name: options.category, category: options.category, value: val, disabled: false, fixed: false} }
        else{
          if(val.category === undefined){ 
            if(val.name === undefined) {val.category = options.category} else {val.category = val.name}}
          if(val.name === undefined){ val.name = val.category}};
        chipAdd(panel, val, options)})}
        '''

  def enter(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Javascript event triggered by the enter key.

    Attributes:
    ----------
    :param js_funcs: List | String. The JavaScript events.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self.__enter_def = True
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.keydown.enter([JsUtils.jsConvertFncs(js_funcs, toStr=True),
                        self.dom.add(self.dom.input)] + js_funcs + [self.input.dom.empty()], profile)
    return self

  def drop(self, js_funcs, prevent_default=True, profile=None):
    """
    Description:
    -----------


    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions.
    :param prevent_default:
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    self.style.css.border = "1px dashed black"
    self.tooltip("Drag and drop values here")
    return super(Filters, self).drop(js_funcs, prevent_default, profile)

  def delete(self, js_funcs, profile=None):
    """
    Description:
    -----------


    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if self.__enter_def:
      raise Exception("delete on chip must be triggered before enter")

    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._jsStyles['delete'] = JsUtils.jsConvertFncs(
      ["this.parentNode.remove()"] + js_funcs, toStr=True, profile=profile)
    return self

  def append(self, value, category=None, name=None, disabled=False, fixed=False):
    """
    Description:
    -----------


    Attributes:
    ----------
    :param value:
    :param category:
    :param name:
    :param disabled:
    :param fixed:
    """
    rec = {"value": value, 'disabled': disabled, 'fixed': fixed, 'category': category, 'name': name}
    if category is None:
      rec['category'] = name or self.options.category
    rec['name'] = name or rec['category']
    self._vals.append(rec)

  def draggable(self, js_funcs=None, options=None, profile=None, source_event=None):
    """
    Description:
    ------------


    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    """
    js_funcs = js_funcs or []
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    js_funcs.append('event.dataTransfer.setData("text", value)')
    self._jsStyles['draggable'] = "function(event, value){%s} " % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile)
    return self

  @property
  def dom(self):
    """
    Description:
    -----------
    The Javascript Dom object.

    :rtype: JsHtmlList.Tags
    """
    if self._dom is None:
      self._dom = JsHtmlList.Tags(self, report=self._report)
    return self._dom

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    self.page.properties.js.add_constructor('ChipAdd', '''function chipAdd(panel, record, options){
        if(typeof(record.category !== "undefined")){options.category = record.category}
        var div = document.createElement("div"); 
        for (var key in options.item_css){div.style[key] = options.item_css[key]};
        div.setAttribute('data-category', record.category);
        var content = document.createElement("span"); 
        for (var key in options.value_css){ content.style[key] = options.value_css[key]};
        content.setAttribute('name', 'chip_value'); content.innerHTML = record.value; 
        if(options.visible){
          var p = document.createElement("p"); 
          for (var key in options.category_css){p.style[key] = options.category_css[key]};
          p.innerHTML = record.name; div.appendChild(p)}
        div.appendChild(content);
        if(!record.fixed && options.delete){
          var icon = document.createElement("i"); 
          for (var key in options.icon_css){icon.style[key] = options.icon_css[key] };
          icon.classList.add('fas'); icon.classList.add('fa-times'); 
          icon.addEventListener('click', function(){eval(options.delete)});
          div.appendChild(icon)}
        if(typeof options.draggable !== 'undefined'){
          div.setAttribute('draggable', true);
          div.style.cursor = 'grab';
          div.ondragstart = function(event){ var value = this.innerHTML; options.draggable(event, value) }
        }
        panel.appendChild(div);
        
        const maxHeight = options.max_height;
        if(maxHeight > 0){
          panel.style.maxHeight = ""+ maxHeight + "px";
          panel.style.overflow = "hidden"; panel.style.position = "relative";
          var div = document.createElement("div"); div.style.color = "#3366BB";
          div.innerHTML = "Show all"; div.style.position = "absolute"; 
          div.style.bottom = 0; div.style.cursor = "pointer";
          div.addEventListener("click", function(event){ 
            var targetElement = event.target || event.srcElement;
            if (targetElement.innerHTML != "reduce"){panel.style.maxHeight = null; targetElement.innerHTML = "reduce"} 
            else {panel.style.maxHeight = ""+ maxHeight + "px"; targetElement.innerHTML = "Show all"}});
          div.style.right = "5px"; panel.appendChild(div)
        }
    }''')
    if not self.options.visible:
      self.input.style.css.display = False
    return '''<div %(attrs)s>%(input)s%(selections)s</div>%(helper)s''' % {
      'attrs': self.get_attrs(pyClassNames=self.style.get_classes()),
      'input': self.input.html(), 'selections': self.selections.html(),  'helper': self.helper}
