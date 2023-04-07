from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from ..game_field import GameField
# from game.core import


class RootWindow(BoxLayout):
    game_field: GameField = ObjectProperty()

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

    # def _start_game(self):
    #     self.game_field = GameField(width, height, mines_amount)

    # def on_kv_post(self, base_widget):
    #     self.game_field.build_game()
