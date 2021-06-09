#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.html.options import OptPanel


class Popup(Html.Html):
  name = 'Popup Container'

  def __init__(self, report, components, width, height, options, profile):
    super(Popup, self).__init__(report, [], css_attrs={"width": width, "height": height}, profile=profile)
    self.__options = OptPanel.OptionPopup(self, options)
    if self.options.background:
      self.css({'width': '100%', 'position': 'fixed', 'height': '100%', 'background-color': 'rgba(0,0,0,0.4)',
                'left': 0, 'top': 0})
      self.css({'display': 'none', 'z-index': self.options.z_index, 'text-align': 'center'})
    else:
      self.css({'position': 'absolute', 'margin': 0, 'padding': 0, 'display': 'none', 'z-index': self.options.z_index})
    self.set_attrs(name="name", value="report_popup")
    self.window = self._report.ui.div(width="auto")
    self.window.options.managed = False
    self.window.style.css.padding = 10
    self.window.style.css.border = "3px solid %s" % report.theme.greys[3]
    self.window.style.css.top = "200px"
    self.window.style.css.min_width = "300px"
    self.window.style.css.left = "50%"
    self.window.style.css.transform = "translate(-50%, -50%)"
    self.window.style.css.position = "fixed"
    self.window.style.css.background = "white"
    self.container = report.ui.div(components, width=(100, '%'), height=(100, '%'))
    self.container.options.managed = False
    self.container.style.css.position = 'relative'
    self.container.style.css.overflow = "auto"
    self.container.style.css.padding = "auto"
    self.container.style.css.vertical_align = "middle"
    self.window.add(self.container)
    if not self.options.background and self.options.draggable:
      report.body.onReady([self.window.dom.jquery_ui.draggable()])

  def add(self, component):
    """
    Description:
    ------------
    Add a component to the popup.
    If this is a list then they will be added in a row.

    Attributes:
    ----------
    :param component: HTML Component | List. The component to be added to the underlying list.
    """
    return self.container.add(component)

  def extend(self, components):
    """
    Description:
    ------------
    Append list of component to the popup.

    Attributes:
    ----------
    :param components: HTML Component | List. The component to be added to the underlying list.
    """
    return self.container.extend(components)

  def insert(self, n, component):
    """
    Description:
    ------------
    Insert a component to the popup at a specific place.

    Attributes:
    ----------
    :param n: Integer. The position in the popup.
    :param component: HTML Component | List. The component to be added to the underlying list.
    """
    return self.container.insert(n, component)

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button.

    :rtype: OptPanel.OptionPopup
    """
    return self.__options

  def add_title(self, text, align='center', level=None, css=None, position="before", options=None):
    """
    Description:
    ------------
    Add a title to the popup.

    Attributes:
    ----------
    :param text: String. The value to be displayed to the component.
    :param align: String. Optional. The text-align property within this component.
    :param level: Integer. Optional.
    :param css: Dictionary. Optional. The CSS attributes to be added to the HTML component
    :param position: String. Optional. The position compared to the main component tag.
    :param options: Specific Python options available for this component.
    """
    if not hasattr(text, 'options'):
      title = self._report.ui.title(text, align=align, level=level, options=options)
      title.style.css.margin_top = -3
    else:
      title = text
    self.container.insert(0, title)
    return self

  def __str__(self):
    if self.options.background:
      self.style.css.padding_top = self.options.top
    if self.options.closure:
      self.close.style.css.font_factor(3)
      self.close.style.css.background_color = self._report.theme.greys[0]
      self.close.style.css.border_radius = 20
      self.close.style.css.top = 5
      self.close.style.css.z_index = self.options.z_index + 10
      self.close.style.css.right = 5
      self.close.style.css.position = 'absolute'
      self.close.click([self.dom.hide()])
      self.window.add(self.close)
    return '''<div %s>%s</div>''' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.window.html())
