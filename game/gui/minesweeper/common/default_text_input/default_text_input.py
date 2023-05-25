from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ListProperty
from kivy.clock import Clock


class WarningLabel(Label):

    def __init__(self, warning: str, **kwargs):
        super().__init__(**kwargs)
        self.text = f'[i][u]{warning}[/u][/i]'

    def on_parent(self, _self_instance, _parent_instance):
        Clock.schedule_once(lambda _dt: self._set_pos())

    def _set_pos(self):
        if self.parent is not None:
            self.right = self.parent.right
            self.center_y = self.parent.center_y


class DefaultTextInput(TextInput, RelativeLayout):
    input_highlight = ListProperty([])

    def warning(self, text: str):
        warning_label = WarningLabel(text)
        self.add_widget(warning_label)
        Clock.schedule_once(lambda _dt: self.remove_widget(warning_label), 2)
