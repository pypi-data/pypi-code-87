#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.core import html
from epyk.core.css import Defaults_css
from epyk.core.html import Defaults_html
from epyk.interfaces import Arguments


class Navigation:

  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def up(self, icon="fas fa-arrow-up", top=20, right=20, bottom=None, tooltip=None, width=(25, 'px'), height=(25, 'px'),
         options=None, profile=False):
    """
    Description:
    ------------
    Navigation button to go to the top of the page directly.

    :tags:
    :categories:

    Usage::

      page.ui.navigation.up()

    Attributes:
    ----------
    :param icon: String. Optional. The component icon content from font-awesome references. Default fas fa-arrow-up.
    :param top: Integer. Optional. The top property affects the vertical position of a positioned element.
    :param right: Integer. Optional. The right property affects the horizontal position of a positioned element.
    :param bottom: Integer. Optional. The top property affects the vertical position of a positioned element.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    du = self.page.ui.icon(icon, width=width, height=height, options=options, profile=profile).css(
      {"border": '1px solid black', "position": 'fixed', "width": 'none', "border-radius": '20px', "padding": '8px',
       "right": '%spx' % right})
    if top is not None:
      du.style.css.top = top
    else:
      du.style.css.bottom = bottom
    du.style.add_classes.div.background_hover()
    self.page.js.onReady(
      self.page.js.window.events.addScrollListener([
        self.page.js.if_(self.page.js.window.scrollY > 50, [du.dom.show()]).else_(du.dom.hide())
      ]))
    if tooltip is not None:
      du.tooltip(tooltip)
    du.click([
      self.page.js.window.scrollUp(),
      self.page.js.objects.this.hide()])
    return du

  @html.Html.css_skin()
  def down(self, icon="fas fa-arrow-down", top=20, right=20, bottom=None, tooltip=None, width=(25, 'px'),
           height=(25, 'px'), options=None, profile=False):
    """
    Description:
    ------------
    Navigation button to go to the bottom of the page directly.

    :tags:
    :categories:

    Usage::

      page.ui.navigation.down()

    Attributes:
    ----------
    :param icon: String. Optional. The component icon content from font-awesome references. Default fas fa-arrow-up.
    :param top: Integer. Optional. The top property affects the vertical position of a positioned element.
    :param right: Integer. Optional. The right property affects the horizontal position of a positioned element.
    :param bottom: Integer. Optional. The top property affects the vertical position of a positioned element.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    dd = self.page.ui.icon(icon, width=width, height=height, options=options, profile=profile).css(
      {"border": '1px solid black', "position": 'fixed', "width": 'none', "border-radius": '20px', "padding": '8px',
       "right": '%spx' % right})
    if bottom is not None:
      dd.style.css.bottom = bottom
    else:
      dd.style.css.top = top
    dd.style.add_classes.div.background_hover()
    self.page.js.onReady(
      self.page.js.window.events.addScrollListener([
        self.page.js.if_(
          self.page.js.window.scrollY < (self.page.js.window.scrollMaxY - 50), [dd.dom.show()]).else_(dd.dom.hide())
      ]))
    if tooltip is not None:
      dd.tooltip(tooltip)
    dd.click([
      self.page.js.window.scrollTo(),
      self.page.js.objects.this.hide()])
    return dd

  @html.Html.css_skin()
  def to(self, y, x=None, icon="fas fa-map-pin", top=20, right=20, bottom=None, tooltip=None, width=(25, 'px'),
         height=(25, 'px'), options=None, profile=False):
    """
    Description:
    ------------
    Navigation button to go to a specific point in the page directly.

    :tags:
    :categories:

    Usage::

      page.ui.navigation.to(100, tooltip="test")

    Attributes:
    ----------
    :param y: Integer. The y position on the page.
    :param x: Integer. Optional. The x position on the page.
    :param icon: String. Optional. The component icon content from font-awesome references. Default fas fa-arrow-up.
    :param top: Integer. Optional. The top property affects the vertical position of a positioned element.
    :param right: Integer. Optional. The right property affects the horizontal position of a positioned element.
    :param bottom: Integer. Optional. The top property affects the vertical position of a positioned element.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    dd = self.page.ui.icon(icon, width=width, height=height, options=options, profile=profile).css(
      {"border": '1px solid black', "position": 'fixed', "width": 'none', "border-radius": '20px', "padding": '8px',
       "right": '%spx' % right})
    if bottom is not None:
      dd.style.css.bottom = bottom
    else:
      dd.style.css.top = top
    dd.style.add_classes.div.background_hover()
    if tooltip is not None:
      dd.tooltip(tooltip)
    self.page.js.onReady(
      self.page.js.window.events.addScrollListener([
        self.page.js.if_(self.page.js.window.scrollY > y, [dd.dom.show()]).else_(dd.dom.hide())
      ]))
    dd.click([
      self.page.js.window.scrollTo(x=x, y=y),
      self.page.js.objects.this.hide()])
    return dd

  @html.Html.css_skin()
  def pin(self, text, url="#", icon="fas fa-map-pin", top=20, right=20, bottom=None, tooltip=None,
          width=(25, 'px'), height=(25, 'px'), options=None, profile=False):
    """
    Description:
    ------------
    Shortcut to a specific position in the page.

    :tags:
    :categories:

    Usage::

      page.ui.navigation.pin("anchor", tooltip="test", bottom=20)

    Attributes:
    ----------
    :param text: String. The shortcut name.
    :param url: String. Optional. The anchor name.
    :param icon: String. Optional. The component icon content from font-awesome references. Default fas fa-arrow-up.
    :param top: Integer. Optional. The top property affects the vertical position of a positioned element.
    :param right: Integer. Optional. The right property affects the horizontal position of a positioned element.
    :param bottom: Integer. Optional. The top property affects the vertical position of a positioned element.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    dd = self.page.ui.icon(icon, width=width, height=height, options=options, profile=profile)
    h_url = self.page.ui.link(text, url=url)
    div = self.page.ui.div([dd, h_url]).css(
      {"border": '1px solid black', "position": 'fixed', "width": 'none', "border-radius": '30px',
       "padding": '10px 15px', "right": '%spx' % right, "background-color": self.page.theme.greys[0]})
    if bottom is not None:
      div.style.css.bottom = bottom
    else:
      div.style.css.top = top
    div.attr['class'].add("CssDivOnHoverWidth")
    h_url.css({"display": 'none', "white-space": 'nowrap'})
    div.on("mouseover", [h_url.dom.css({"display": 'inline-block', "padding-left": "10px"})])
    div.on("mouseout", [h_url.dom.css({"display": 'none', "padding-left": "0px"})])
    if tooltip is not None:
      div.tooltip(tooltip)
    return div

  @html.Html.css_skin()
  def scroll(self, progress=0, height=(3, 'px'), options=None, profile=False):
    """
    Description:
    ------------
    Add a horizontal progressbar to display the status of the page scrollbar.

    :tags:
    :categories:

    Usage::

      page.ui.navigation.scroll()

    Attributes:
    ----------
    :param progress: Integer. Optional. The progression on the page.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    height = Arguments.size(height, unit="px")
    p = self.page.ui.sliders.progressbar(progress, height=height, options=options, profile=profile)
    self.page.js.onReady(
      self.page.js.window.events.addScrollListener([
        p.build(self.page.js.window.scrollPercentage)]))
    return p

  @html.Html.css_skin()
  def indices(self, count, selected=1, width=(100, '%'), height=(None, 'px'), html_code=None, options=None,
              profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.navigation.indices(10)

    Attributes:
    ----------
    :param count: Integer. Optional. The number of pages.
    :param selected: Integer. Optional. The selected index.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"div_css": {"display": "inline-block", "margin": "0 2px"}, "selected": selected}
    dflt_options.update(options or {})
    html_indices = html.HtmlContainer.Indices(self.page, count, width, height, html_code, dflt_options, profile)
    return html_indices

  @html.Html.css_skin()
  def points(self, count, selected=0, width=(100, '%'), height=(None, 'px'), html_code=None, options=None,
             profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      p = page.ui.navigation.points(10)
      for i, _ in enumerate(p):
        p.click_item(i, [])

    Attributes:
    ----------
    :param count: Integer. The number of pages.
    :param selected: Integer. Optional. The selected index.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"div_css": {"display": "inline-block", "margin": "0 2px"}, "selected": selected}
    dflt_options.update(options or {})
    html_points = html.HtmlContainer.Points(self.page, count, width, height, html_code, dflt_options, profile)
    return html_points

  @html.Html.css_skin()
  def dots(self, count, selected=1, position="right", width=(100, '%'), height=(None, 'px'), html_code=None,
           options=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      d = page.ui.navigation.dots(10)

    Attributes:
    ----------
    :param count: Integer. Optional. The number of pages.
    :param selected: Integer. Optional. The selected index.
    :param position: String. Optional. A string with the vertical position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"div_css": {"margin": "2px", "float": position}, "selected": selected}
    dflt_options.update(options or {})
    html_points = html.HtmlContainer.Points(self.page, count, width, height, html_code, dflt_options, profile)
    return html_points

  @html.Html.css_skin()
  def path(self, record, divider=None, width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      record = [{"text": "Lin 1", 'url': 'report_list.html'}, {"text": "Link 2"}]
      page.ui.navigation.path(record)

    Attributes:
    ----------
    :param record: Dictionary. Component input data.
    :param divider: String. Optional. A path delimiter.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if divider is None:
      divider = self.page.symbols.shapes.BLACK_RIGHT_POINTING_TRIANGLE
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile)
    for rec in record[:-1]:
      div += self.page.ui.link(rec['text'], url=rec.get('url', '#')).css({"display": 'inline-block'})
      div += self.page.ui.text(divider).css(
        {"display": 'inline-block', 'margin': '0 5px', 'font-size': self.page.body.style.globals.font.normal(-2)})
    div += self.page.ui.link(record[-1]['text'], url=record[-1].get('url', '#')).css(
      {"display": 'inline-block'})
    return div

  @html.Html.css_skin()
  def nav(self, logo=None, title=None, components=None, width=(100, '%'), height=(40, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::


    Attributes:
    ----------
    :param logo: String. Optional.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param components: List. Optional. The Components to be added to the navbar.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options:  Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    comp_id = 'page_nav_bar'
    if comp_id not in self.page.components:
      nav_bar = self.bar(logo, title, width, height, options, html_code=comp_id, profile=profile)
    else:
      nav_bar = self.page.components[comp_id]
    if components is not None:
      for component in components:
        nav_bar.add(component)
    return nav_bar

  @html.Html.css_skin()
  def bar(self, logo=None, title=None, width=(100, '%'), height=(40, 'px'), options=None, html_code=None,
          profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      nav = page.ui.navigation.bar(title="test")
      nav.add_text("Test text")
      nav + page.ui.button("Click")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMenu.HtmlNavBar`

    Attributes:
    ----------
    :param logo:
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    components = []
    options, scroll_height = options or {}, -5
    options['logo_height'] = tuple(height) if 'logo_height' not in options else Arguments.size(options['logo_height'], unit="px")
    options['logo_width'] = tuple(height) if 'logo_width' not in options else Arguments.size(options['logo_width'], unit="px")

    if logo is None:
      logo = self.page.ui.icons.epyk()
      components.append(logo)
    else:
      if not hasattr(logo, 'options'):    # if it is not an option it is considered as a path
        logo_url = logo
        logo = self.page.ui.div(height=options['logo_height'], width=options['logo_width'])
        if logo_url:
          logo.style.css.background_url(logo_url, size="auto %s%s" % (options['logo_height'][0], options['logo_height'][1]))
      components.append(logo)
    components[-1].style.css.margin_right = 20
    if title is not None:
      title = self.page.ui.div(title, height=(100, "%"))
      title.style.css.text_transform = "uppercase"
      title.style.css.margin_left = 5
      title.style.css.margin_right = 5
      title.style.css.bold()
      components.append(title)
    if options.get('status', False):
      scroll = self.page.ui.navigation.scroll()
      scroll_height = 5
      scroll.style.css.display = "block"
      scroll.options.managed = False
      scroll.style.css.height = scroll_height
    html_nav = html.HtmlMenu.HtmlNavBar(self.page, components, width=width, height=height, options=options,
                                        html_code=html_code, profile=profile)
    if options.get('status', False):
      html_nav.scroll = scroll
    html_nav.logo = logo
    html_nav.title = title
    html_nav.logo.style.css.display = "inline-block"
    html_nav.style.css.line_height = height[0]
    Defaults_css.BODY_CONTAINER = {"padding-top": height[0] + scroll_height}
    self.page.body.style.custom_class({
      "padding-top": '%spx' % (height[0] + 5 + scroll_height)}, "body", is_class=False)
    return html_nav

  @html.Html.css_skin()
  def banner(self, image, text, link, width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlImage.Image`
      - :class:`epyk.core.html.HtmlContainer.Col`
      - :class:`epyk.core.html.HtmlContainer.Row`
      - :class:`epyk.core.html.HtmlText.Text`
      - :class:`epyk.core.html.HtmlLinks.ExternalLink`

    Attributes:
    ----------
    :param image: String. Optional. The image full path.
    :param text: String. Optional. The value to be displayed to the component.
    :param link: String. Optional. The url link.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile)
    h_image = self.page.ui.img(image)
    h_text = self.page.ui.text(text)
    h_link = self.page.ui.links.button("click", link)
    h_row = self.page.ui.row(
      [h_image, self.page.ui.col([h_text, h_link])])
    div + h_row
    div.style.css.background_color = self.page.theme.colors[3]
    div.style.css.color = "white"
    div.style.css.font_size = self.page.body.style.globals.font.normal(5)
    div.style.css.text_align = 'center'
    div.style.css.padding = "5px 15px"
    return div

  @html.Html.css_skin()
  def footer(self, components=None, width=(100, '%'), height=(80, 'px'), fixed=False, options=None, profile=False):
    """
    Description:
    ------------

    Will create a footer object in the body of the report.

    :tags:
    :categories:

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMenu.HtmlFooter`

    Attributes:
    ----------
    :param components: list of html components.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param fixed: Boolean. Optional. Fix the component at the page bottom.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    footer = html.HtmlMenu.HtmlFooter(
      self.page, components, width=width, height=height, options=options, profile=profile)
    if fixed:
      self.page.body.style.css.padding_bottom = height[0]
    else:
      footer.style.css.position = None
    return footer

  @html.Html.css_skin()
  def side(self, components=None, anchor=None, size=262, position='right', options=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/contextmenu.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/st_news.py

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param anchor: Component. Optional. The panel button to show / hide.
    :param size: Integer. Optional. Panel's width in pixel.
    :param position: String. Optional. A string with the vertical position of the component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    position_type = "absolute" if self.page.body.template is None else 'fixed'
    d = self.page.ui.div(components, options=options, profile=profile)
    d.css({"background": self.page.theme.colors[2], "position": position_type, 'top': 0, 'height': '100%',
           'overflow-x': 'hidden', 'width': "%spx" % size, 'z-index': 20})
    if position == 'left':
      d.css({
        'left': 0, 'margin-left': "-%spx" % size,
        'border-right': '1px solid %s' % self.page.theme.notch(), 'padding': '5px'})
    else:
      d.css({
        'right': 0, 'margin-right': "-%spx" % size,
        'border-left': '1px solid %s' % self.page.theme.notch(), 'padding': '5px'})
    self.page.body.style.custom_class({
      "overflow-x": 'hidden', "position": 'relative', 'min-height': '100%'}, "html, body", is_class=False)

    def close():
      return d.dom.toggle_transition("margin-left", "0px", "-%spx" % size)
    d.close = close

    if Defaults_css.BODY_CONTAINER is not None:
      d.style.padding_top = Defaults_css.BODY_CONTAINER.get("padding-top", -10) + 10
    if anchor is None:
      if position == 'left':
        i = self.page.ui.icon("fas fa-bars").click([d.dom.toggle_transition("margin-left", "0px", "-%spx" % size)])
        i.style.css.float = 'right'
        if position_type == "fixed":
          i.style.css.position = "fixed"
          i.style.css.right = 10
          i.style.css.top = 5
      else:
        i = self.page.ui.icon("fas fa-bars").click([d.dom.toggle_transition("margin-right", "0px", "-%spx" % size)])
        if position_type == "fixed":
          i.style.css.position = "fixed"
          i.style.css.left = 10
          i.style.css.top = 10
      i.css({"padding": '5px'})
    else:
      if position == 'left':
        anchor.click([d.dom.toggle_transition("margin-left", "0px", "-%spx" % size)])
      else:
        anchor.click([d.dom.toggle_transition("margin-right", "0px", "-%spx" % size)])
    return d

  @html.Html.css_skin()
  def pilcrow(self, text="", html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    Add an anchor on the page and move to this when it is clicked.

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    p = self.page.ui.div("%s&#182" % text, html_code=html_code, options=options, profile=profile)
    p.style.css.font_size = self.page.body.style.globals.font.normal(5)
    p.style.css.cursor = "pointer"
    p.click([self.page.js.window.scrollTo(y=self.page.js.objects.this.offsetTop)])
    return p

  @html.Html.css_skin()
  def panel(self, width=(100, '%'), height=(100, '%'), options=None, profile=None, helper=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/bars.py

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param helper: String. Optional. A tooltip helper.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="%")
    dflt_options = {"position": 'top'}
    if options is not None:
      dflt_options.update(options)
    h_drawer = html.HtmlMenu.PanelsBar(self.page, width, height, dflt_options, helper, profile)
    return h_drawer

  @html.Html.css_skin()
  def shortcut(self, components=None, logo=None, size=(40, 'px'), options=None, profile=None, html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param logo:
    :param size: Integer. Optional. Panel's height in pixel.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    size = Arguments.size(size, unit="px")
    dflt_options = {"position": 'left'}
    if options is not None:
      dflt_options.update(options)
    if dflt_options["position"] in ['top', 'bottom']:
      width = (100, '%')
      height = size
    else:
      width = size
      height = (100, '%')
    h_drawer = html.HtmlMenu.Shortcut(
      self.page, components or [], logo, width, height, html_code, dflt_options, profile)
    h_drawer.style.css.padding = "5px 10px"
    return h_drawer


class Banners:

  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def top(self, data="", background=None, width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/banners.py

    Attributes:
    ----------
    :param data:
    :param background: String. Optional. Background color code.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(data, width=width, height=height, options=options, profile=profile)
    if div.style.css.height is None:
      div.style.css.min_height = Defaults_html.LINE_HEIGHT
    div.style.css.background_color = background or self.page.theme.colors[3]
    div.style.css.color = "white"
    div.style.css.position = "fixed"
    div.style.css.top = 0
    div.style.css.left = 0
    div.style.css.z_index = 500
    div.style.css.padding = "5px 15px"
    return div

  @html.Html.css_skin()
  def bottom(self, data="", background=None, align="center", width=(100, '%'), height=(None, 'px'), options=None,
             profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/banners.py

    Attributes:
    ----------
    :param data:
    :param background: String. Optional. Background color code.
    :param align: String. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(data, width=width, height=height, options=options, profile=profile)
    if div.style.css.height is None:
      div.style.css.min_height = Defaults_html.LINE_HEIGHT
    div.style.css.background_color = background or self.page.theme.greys[1]
    div.style.css.z_index = 110
    div.style.css.left = 0
    div.style.css.z_index = 500
    div.style.css.text_align = align
    div.style.css.position = "fixed"
    div.style.css.padding = "5px 15px"
    div.style.css.bottom = 0
    return div

  @html.Html.css_skin()
  def cookies(self, text, url, align="center", width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.banners.cookies("Test", "#")

    Attributes:
    ----------
    :param text: String. The value to be displayed to the component.
    :param url: String. The url link.
    :param align: String. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile:  Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    link = self.page.ui.link("Learn more", url=url).css({"margin-right": "10px"})
    link.style.css.margin_right = 10
    link.style.css.color = self.page.theme.greys[-1]
    button = self.page.ui.button("Ok")
    container = self.bottom([
      self.page.ui.div([
        text,
        self.page.ui.div([link, button], align="center")
      ])
    ], align=align, width=width, height=height, options=options, profile=profile)
    button.click([container.dom.hide()])
    container.button = button
    container.link = link
    return container

  @html.Html.css_skin()
  def corner(self, data="", background=None, position="bottom", width=(180, 'px'), height=(None, 'px'), options=None,
             profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/banners.py

    Attributes:
    ----------
    :param data:
    :param background: String. Optional. Background color code.
    :param position: String. Optional. A string with the vertical position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    options = options or {}
    div = self.page.ui.div(data, width=width, height=height, options=options, profile=profile)
    if div.style.css.height is None:
      div.style.css.min_height = Defaults_html.LINE_HEIGHT
    div.style.css.background_color = background or self.page.theme.colors[3]
    div.style.css.color = "white"
    div.style.css.z_index = options.get("z_index", 860)
    div.style.css.position = "fixed"
    div.style.css.padding = "5px 15px"
    div.style.css.text_align = "center"
    div.style.css.right = 0
    if position == 'bottom':
      div.style.css.bottom = 0
      div.style.css.transform = "rotate(-40deg)"
      div.style.css.margin = "0 -30px 15px 0"
    else:
      div.style.css.top = 0
      div.style.css.transform = "rotate(40deg)"
      div.style.css.margin = "20px -45px 0 0"
    return div

  @html.Html.css_skin()
  def info(self, data, icon="fas fa-info-circle", background=None, width=(100, '%'), height=(None, 'px'), options=None,
           profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param data:
    :param icon: String. Optional. The component icon content from font-awesome references. Default fas fa-info-circle
    :param background: String. Optional. Background color code.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile)
    if not hasattr(data, 'options'):
      data = self.page.ui.div(data, width=("auto", ""))
      data.style.css.font_size = "inline-block"
      data.style.css.font_size = self.page.body.style.globals.font.normal(4)
    if not hasattr(icon, 'options'):
      icon = self.page.ui.icons.awesome(icon)
      icon.style.css.font_size = "inline-block"
    div.add(icon)
    div.add(data)
    div.style.css.background_color = background or self.page.theme.greys[0]
    div.style.css.padding = "20px 15px"
    div.style.css.font_size = self.page.body.style.globals.font.normal(4)
    div.style.css.color = self.page.theme.greys[-1]
    div.style.css.top = 0
    return div

  @html.Html.css_skin()
  def text(self, data="", size_notch=0, background=None, width=(100, '%'), align="center", height=(None, 'px'),
           options=None, html_code=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param data:
    :param size_notch:
    :param background: String. Optional. Background color code.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    if not hasattr(data, 'options'):
      data = self.page.ui.div(self.page.py.encode_html(data), html_code=html_code, width=("auto", ""))
      data.style.css.display = "inline-block"
      data.style.css.text_align = align
      data.style.css.font_size = self.page.body.style.globals.font.normal(size_notch)
    div.add(data)
    if background is not None:
      div.style.css.background_color = background
    div.style.css.padding = "20px 15px"
    div.style.css.margin = "auto"
    div.style.css.font_size = self.page.body.style.globals.font.normal(size_notch)
    div.style.css.color = self.page.theme.greys[-1]
    div.style.css.top = 0
    return div

  @html.Html.css_skin()
  def title(self, title, content, size_notch=0, background=None, width=(100, '%'), align="center", height=(None, 'px'),
            options=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param title:  String. Optional. A panel title. This will be attached to the title property.
    :param content: String. Optional. The value to be displayed to the component.
    :param size_notch:
    :param background: String. Optional. Background color code.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    options = options or {}
    if not hasattr(title, 'options'):
      title = self.page.ui.titles.title(title)
      title.style.css.text_align = align
      title.style.css.font_weight = 800
      if 'title_color' in options:
        title.style.css.color = options['title_color']
      title.style.css.font_size = self.page.body.style.globals.font.normal(options.get("title_notch", 20) + size_notch)
    div.add(title)
    if not hasattr(content, 'options'):
      content = self.page.ui.div(content, width=("auto", ""))
      content.style.css.text_align = align
      content.style.css.font_size = "inline-block"
      content.style.css.font_size = self.page.body.style.globals.font.normal(size_notch)
    div.add(content)
    div.style.css.background_color = background or self.page.theme.greys[0]
    div.style.css.padding = "20px 15px"
    div.style.css.font_size = self.page.body.style.globals.font.normal(size_notch)
    div.style.css.color = self.page.theme.greys[-1]
    div.style.css.top = 0
    return div

  @html.Html.css_skin()
  def quote(self, content, author, avatar=None, background=None, size_notch=0, width=(100, '%'), align="center",
            height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param content: String. Optional. The value to be displayed to the component.
    :param author:
    :param avatar:
    :param background: String. Optional. Background color code.
    :param size_notch:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    if not hasattr(content, 'options'):
      content = self.page.ui.div('"%s"' % content, width=("auto", ""))
      content.style.css.display = "inline-block"
      content.style.css.text_align = align
      content.style.css.font_size = self.page.body.style.globals.font.normal(size_notch)
    div.add(content)
    div.style.css.background_color = background or self.page.theme.greys[0]
    div.style.css.padding = "20px 15px"
    div.style.css.margin = "auto"
    div.style.css.color = self.page.theme.greys[-1]
    div.style.css.top = 0
    line = self.page.ui.layouts.hr(width=(20, 'px'))
    line.style.css.margin_right = 10
    line.style.css.display = "inline-block"
    if not hasattr(author, 'options'):
      author = self.page.ui.div(author, width=("auto", ""))
      author.style.css.display = "inline-block"
    div.add(self.page.ui.div([line, author]))
    return div

  @html.Html.css_skin()
  def disclaimer(self, copyright=None, links=None, width=(100, '%'), height=("auto", ''), align="center", options=None,
                 profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param copyright:
    :param links:
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    now = datetime.datetime.now()
    copyright = self.page.py.encode_html(copyright or "© 2018 - %s, Epyk studio" % now.year)
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    if links is not None:
      for link in links:
        if not isinstance(link, dict):
          link = {"text": link}
        url = self.page.ui.link(text=link['text'], url=link.get("url", '#'))
        url.style.css.color = self.page.theme.greys[6]
        url.style.css.margin = "0 5px"
        div.add(url)
    text = self.page.ui.text(copyright)
    text.style.css.color = self.page.theme.greys[-1]
    div.add(text)
    div.style.css.background_color = self.page.theme.greys[3]
    div.style.css.color = self.page.theme.greys[6]
    div.style.css.padding = "5px 0"
    div.style.css.left = 0
    div.style.css.margin_top = 40
    div.style.css.position = "absolute"
    return div

  @html.Html.css_skin()
  def follow(self, text, width=(100, '%'), height=("auto", ''), align="left", options=None, profile=False,
             youtube=True, twitter=True, facebook=True, twitch=True, instagram=True, linkedIn=True):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param youtube: Boolean. Optional. Add the icon to the follow bar. Default True.
    :param twitter: Boolean. Optional. Add the icon to the follow bar. Default True.
    :param facebook: Boolean. Optional. Add the icon to the follow bar. Default True.
    :param twitch: Boolean. Optional. Add the icon to the follow bar. Default True.
    :param instagram: Boolean. Optional. Add the icon to the follow bar. Default True.
    :param linkedIn: Boolean. Optional. Add the icon to the follow bar. Default True.
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    div.style.css.padding = "10px 0"
    text = self.page.ui.text(text)
    div.add(text)

    icon_size = int(self.page.body.style.globals.font.normal(8)[:-2])
    if youtube:
      div.youtube = self.page.ui.icons.youtube(width=(icon_size, 'px'))
      div.youtube.style.css.margin = "0 2px"
      div.add(div.youtube)

    if twitter:
      div.twitter = self.page.ui.icons.twitter(width=(icon_size, 'px'))
      div.twitter.style.css.margin = "0 2px"
      div.add(div.twitter)

    if facebook:
      div.facebook = self.page.ui.icons.facebook(width=(icon_size, 'px'))
      div.facebook.style.css.margin = "0 2px"
      div.add(div.facebook)

    if twitch:
      div.twitch = self.page.ui.icons.twitch(width=(icon_size, 'px'))
      div.twitch.style.css.margin = "0 2px"
      div.add(div.twitch)

    if instagram:
      div.instagram = self.page.ui.icons.instagram(width=(icon_size, 'px'))
      div.instagram.style.css.margin = "0 2px"
      div.add(div.instagram)

    if linkedIn:
      div.linkedIn = self.page.ui.icons.linkedIn(width=(icon_size, 'px'))
      div.linkedIn.style.css.margin = "0 2px"
      div.add(div.linkedIn)

    if width != (100, "%"):
      div.style.css.margin = "auto"
      div.style.css.display = "block"
    else:
      div.style.css.background_color = self.page.theme.greys[2]
    return div

  @html.Html.css_skin()
  def row(self, headers, links, size_notch=0, background=None, width=(100, '%'), align="left", height=(None, 'px'),
          options=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param headers:
    :param links:
    :param size_notch:
    :param background: String. Optional. Background color code.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    row = []
    for i, header in enumerate(headers):
      col = self.page.ui.col([self.page.ui.subtitle(header)], position='top')
      for link in links[i]:
        html_link = self.page.ui.link(link)
        html_link.style.css.display = 'block'
        html_link.style.css.margin = "5px 0"
        col.add(html_link)
      row.append(col)
    div.add(self.page.ui.row(row))
    div.style.css.background_color = background or self.page.theme.greys[0]
    div.style.css.padding = "20px 15px"
    div.style.css.margin = "auto"
    div.style.css.font_size = self.page.body.style.globals.font.normal(size_notch)
    div.style.css.color = self.page.theme.greys[-1]
    div.style.css.top = 0
    return div

  @html.Html.css_skin()
  def contact_us(self, title="Contact Us", background=None, width=(100, '%'), align="left", height=(None, 'px'),
                 html_code="contactus", options=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param background: String. Optional. Background color code.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    div.style.css.padding = 5
    div.add(self.page.ui.title(title))
    row = self.page.ui.row([
      self.page.ui.input(
        placeholder="First Name", width=("calc(100% - 5px)", ""), html_code="%s_first_name" % html_code),
      self.page.ui.input(
        placeholder="Last Name", html_code="%s_last_name" % html_code)]).css({"padding-top": '5px', "margin": '5px',
                                                                              "width": "calc(100% - 10px)"})
    row.attr["class"].add("no-gutters")
    div.add(row)
    div.add(self.page.ui.input(placeholder="Email", html_code="%s_email" % html_code).css({
      "margin": '5px', "width": "calc(100% - 10px)"}))
    div.add(self.page.ui.input(placeholder="Subject", html_code="%s_subject" % html_code).css({
      "margin": '5px', "width": "calc(100% - 10px)"}))
    div.add(self.page.ui.textarea(placeholder="Leave us a message", html_code="%s_message" % html_code).css({
      "margin": '5px', "width": "calc(100% - 10px)"}))
    div.button = self.page.ui.button("Submit", align="center")
    div.add(div.button)
    div.style.css.background_color = background or self.page.theme.greys[0]
    div.style.css.margin_bottom = 10
    div._internal_components = ["%s_email" % html_code, "%s_first_name" % html_code, "%s_last_name" % html_code,
                                "%s_subject" % html_code, "%s_message" % html_code]
    return div

  @html.Html.css_skin()
  def sponsor(self, logos, title="Sponsors", content='', background=None, width=(100, '%'), height=("auto", ''),
              align="center", options=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param logos:
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param content:
    :param background: String. Optional. Background color code.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    if not hasattr(title, 'options'):
      div.title = self.page.ui.titles.title(title)
      div.title.style.css.text_align = align
      div.title.style.css.font_weight = 800
      div.title.style.css.font_size = self.page.body.style.globals.font.normal(15)
    else:
      div.title = title
    div.add(div.title)
    if not hasattr(content, 'options'):
      content = self.page.ui.div(content, width=("auto", ""))
      content.style.css.text_align = align
      content.style.css.font_size = "inline-block"
    div.add(content)

    div_logos = self.page.ui.div("", align=align)
    div.logos = []
    for logo in logos:
      img = self.page.ui.img(
        "%s?raw=true" % logo, path="https://github.com/epykure/ressources/blob/master/logos", width=("auto", ''))
      div.logos.append(img)
      img.style.css.display = 'inline-block'
      img.style.css.cursor = 'pointer'
      img.style.css.filter = 'grayscale(100%)'
      img.style.hover({'filter': 'grayscale(0%)'})
      img.style.css.margin = '0 5px'
      div_logos.add(img)
    div.add(div_logos)
    div.style.css.background_color = background or self.page.theme.greys[0]
    div.style.css.padding = "20px 15px"
    div.style.css.margin = "auto"
    div.style.css.color = self.page.theme.greys[-1]
    div.style.css.top = 0
    return div


class NavBars:

  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def fixed(self, logo=None, title=None, width=(100, '%'), height=(40, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param logo:
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    bar = self.page.ui.navbar(logo, title, width, height, options, profile)
    return bar

  @html.Html.css_skin()
  def top(self, logo=None, title=None, width=(100, '%'), height=(40, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param logo:
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    bar = self.page.ui.navbar(logo, title, width, height, options, profile)
    bar.style.css.position = False
    return bar

  @html.Html.css_skin()
  def transparent(self, logo=None, title=None, width=(100, '%'), height=(40, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param logo:
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    bar = self.page.ui.navbar(logo, title, width, height, options, profile)
    bar.style.css.position = "absolute"
    bar.style.css.top = 0
    bar.no_background()
    return bar

  @html.Html.css_skin()
  def dark(self, logo=None, title=None, width=(100, '%'), height=(40, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param logo:
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    bar = self.page.ui.navbar(logo, title, width, height, options, profile)
    bar.style.css.position = "absolute"
    bar.style.css.top = 0
    bar.no_background()
    bar.style.css.opacity = 0.5
    bar.style.css.background = 'black'
    return bar
