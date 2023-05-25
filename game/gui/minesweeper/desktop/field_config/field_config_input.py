from kivy.properties import NumericProperty

from ...common import DefaultTextInput


class FieldConfigInput(DefaultTextInput):
    min_value: int = NumericProperty()
    max_value: int = NumericProperty()
