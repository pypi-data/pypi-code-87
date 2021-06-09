
from epyk.core.css.styles.attributes import Attrs


class AttrInput(Attrs):
  """
  CSS pre defined properties for the Input.

  CSS Properties:

    font-size: Normal (the value defined by the framework)
    font-family: Default coming from the framework
    box-sizing: border-box
  """

  def __init__(self, component):
    super(AttrInput, self).__init__(component)
    self.font_size = component.page.body.style.globals.font.normal()
    self.font_family = component.page.body.style.globals.font.family
    self.box_sizing = 'border-box'
