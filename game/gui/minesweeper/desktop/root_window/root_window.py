from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from ...common import Counter
from ..field_config import FieldConfig
from ..statistics import Statistics
from ..achievements import Achievements
from ..game_field import GameField
from .menu_bar_button import MenuBarButton, MenuButton


class RootWindow(BoxLayout):
    configs: MenuBarButton = ObjectProperty()
    mines_counter: Counter = ObjectProperty()
    status_button: Button = ObjectProperty()
    time_counter: Counter = ObjectProperty()
    game_field: GameField = ObjectProperty()

    def config_field(self, _instance: MenuButton):
        FieldConfig(self).open()

    @classmethod
    def statistics(cls, _instance: MenuButton):
        Statistics().open()

    @classmethod
    def achievements(cls, _instance: MenuButton):
        Achievements().open()

    def restart(self):
        self.game_field.build_game()
        del self.status_button.status
