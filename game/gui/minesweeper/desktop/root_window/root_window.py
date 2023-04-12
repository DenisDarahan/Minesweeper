from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from ..game_field import GameField


class RootWindow(BoxLayout):
    status: Button = ObjectProperty()
    game_field: GameField = ObjectProperty()

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

    # def _start_game(self):
    #     self.game_field = GameField(width, height, mines_amount)

    # def on_kv_post(self, base_widget):
    #     self.game_field.build_game()

    def fail(self):
        # self.status.canvas.before
        pass

    def restart(self):
        self.game_field.build_game()
