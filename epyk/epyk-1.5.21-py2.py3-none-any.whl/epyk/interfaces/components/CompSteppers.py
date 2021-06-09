#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.interfaces import Arguments


class Steppers:

  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def stepper(self, records, width=("auto", ''), height=(70, 'px'), color=None, options=None, profile=False):
    """
    Description:
    ------------
    Entry point for the stepper object.

    Usage::

      page.ui.stepper([
        {"value": 'test 1', "status": 'success', 'label': 'test'},
        {"value": 'test 2', "status": 'error'},
        {"value": 'test 3', "status": 'pending'}])

    Attributes:
    ----------
    :param records: List. A list with the different steps defined in the workflow.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param color: String. Optional. The text color code.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dft_options = {"line": True}
    if options is not None:
      dft_options.update(options)
    st = html.HtmlStepper.Stepper(self.page, records, width, height, color, dft_options, profile)
    st.style.add_classes.div.stepper()
    if dft_options.get("media", True):
      st.style.css_class.media({
        '.cssdivstepper li': {"float": None, 'width': '100%'},
        '.cssdivstepper li line': {'stroke-width': 0},
        '.cssdivstepper li [name=label]': {'width': '100%!IMPORTANT'}}, 'only', 'screen',
        {"and": [{'max-width': '600px'}]})
    return st

  @html.Html.css_skin()
  def arrow(self, records, width=("auto", ''), height=(70, 'px'), color=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param records: List. A list with the different steps defined in the workflow.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param color: String. Optional. The text color code.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    dft_options = {"shape": 'arrow'}
    if options is not None:
      dft_options.update(options)
    return self.stepper(records, width, height, color, dft_options, profile)

  @html.Html.css_skin()
  def rectangle(self, records, width=("auto", ''), height=(70, 'px'), color=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param records: List. A list with the different steps defined in the workflow.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param color: String. Optional. The text color code.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    dft_options = {"shape": 'rectangle'}
    if options is not None:
      dft_options.update(options)
    return self.stepper(records, width, height, color, dft_options, profile)

  @html.Html.css_skin()
  def triangle(self, records, width=("auto", ''), height=(70, 'px'), color=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param records: List. A list with the different steps defined in the workflow.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param color: String. Optional. The text color code.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    dft_options = {"shape": 'triangle'}
    if options is not None:
      dft_options.update(options)
    return self.stepper(records, width, height, color, dft_options, profile)

  @html.Html.css_skin()
  def vertical(self, records, shape='circle', width=("auto", ''), height=(70, 'px'), color=None, options=None,
               profile=None):
    """
    Description:
    ------------
    Entry point for the stepper object.

    Usage::

      page.ui.stepper([
        {"value": 'test 1', "status": 'success', 'label': 'test'},
        {"value": 'test 2', "status": 'error'},
        {"value": 'test 3', "status": 'pending'}])

    Attributes:
    ----------
    :param records: List. A list with the different steps defined in the workflow.
    :param shape: String. Optional. The steppers shape.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param color: String. Optional. The text color code.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dft_options = {"line": False, "shape": shape}
    if options is not None:
      dft_options.update(options)
    st = html.HtmlStepper.Stepper(self.page, records, width, height, color, dft_options, profile)
    return st
