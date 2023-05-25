from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.context import get_current_context
from kivy.properties import ObjectProperty

from ...common import BasePopup
from .field_config_input import FieldConfigInput


class FieldConfig(BasePopup):
    title: Label = ObjectProperty()
    fast_config_label: Label = ObjectProperty()
    fast_config: Spinner = ObjectProperty()
    width_config_label: Label = ObjectProperty()
    width_config: FieldConfigInput = ObjectProperty()
    height_config_label: Label = ObjectProperty()
    height_config: FieldConfigInput = ObjectProperty()
    mines_config_label: Label = ObjectProperty()
    mines_config: FieldConfigInput = ObjectProperty()
    accept: Button = ObjectProperty()

    root_window: BoxLayout

    FAST_CONFIG: dict[str, dict] = {
        'Beginner': {'width': 10, 'height': 10, 'mines_amount': 10},
        'Intermediate': {'width': 20, 'height': 20, 'mines_amount': 40},
        'Expert': {'width': 30, 'height': 20, 'mines_amount': 100}
    }
    MIN_WIDTH: int = 10
    MIN_HEIGHT: int = 10
    MIN_MINES_AMOUNT: int = 10
    MAX_WIDTH: int = 30
    MAX_HEIGHT: int = 30
    MAX_MINES_AMOUNT: int = 450

    def __init__(self, root_window: BoxLayout, **kwargs):
        super().__init__(**kwargs)
        self.root_window = root_window

    def _preset_config(self, config: dict):
        self.width_config.text = str(config['width'])
        self.height_config.text = str(config['height'])
        self.mines_config.text = str(config['mines_amount'])

    def on_pre_open(self):
        self.fast_config.text = 'Beginner'
        self.update_config()

    def update_config(self):
        self._preset_config(self.FAST_CONFIG[self.fast_config.text])

    def accept_config(self):
        config = {'width': int(self.width_config.text or 0), 'height': int(self.height_config.text or 0),
                  'mines_amount': int(self.mines_config.text or 0)}

        if not self.MIN_WIDTH <= config['width'] <= self.MAX_WIDTH:
            self.width_config.focus = True
            return
        if not self.MIN_HEIGHT <= config['height'] <= self.MAX_HEIGHT:
            self.height_config.focus = True
            return
        if not self.MIN_MINES_AMOUNT <= config['mines_amount'] <= self.MAX_MINES_AMOUNT:
            self.mines_config.focus = True
            return

        get_current_context()['field'] = config
        self.root_window.restart()
        self.dismiss()
