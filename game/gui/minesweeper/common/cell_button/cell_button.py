from kivy.uix.boxlayout import BoxLayout
from kivy.input.motionevent import MotionEvent
from kivy.properties import NumericProperty

from game.core import Cell
from ..default_button import DefaultButton
from ..long_press_button import LongPressButton


class CellButton(DefaultButton, LongPressButton):
    flag = NumericProperty(0)

    def on_flag(self, _instance, value: int):
        self.cell.flag = bool(value)
        self.game_field.root_window.mines_counter.number = \
            self.game_field.root_window.mines_counter.number + (-1) ** value

    game_field: BoxLayout
    cell: Cell
    last_touch_id: str = ''  # prevents from firing on_long_press or on_release

    def __init__(self, game_field: BoxLayout, cell: Cell, **kwargs):
        super().__init__(**kwargs)

        self.game_field = game_field
        self.cell = cell

    def display_mine(self, user_pressed: bool = False):
        self.background_normal = self.background_down = \
            f'resources/mine_button_{"down" if user_pressed else "normal"}.png'

    def display_cell_value(self):
        self.background_normal = self.background_down = f'resources/opened_cell_button_{self.cell.value}.png'

    def on_touch_down(self, touch: MotionEvent):
        if self.collide_point(*touch.pos):
            if self.game_field.game_status == 'ended':
                return True

            if self.game_field.game_status == 'new':
                self.game_field.game_status = 'started'

            if touch.button == 'right':
                self.last_touch_id = touch.id
                self.change_flag()

        super().on_touch_down(touch)

    def change_flag_long_press(self):
        if self.last_touch and self.last_touch_id == self.last_touch.id:
            return

        self.last_touch_id = self.last_touch.id
        self.change_flag()

    def change_flag(self):
        if self.cell.opened:
            return
        self.flag = 0 ** self.flag

    def open(self):
        if self.cell.opened or self.last_touch_id == self.last_touch.id:
            return

        if self.flag:
            self.change_flag()
            return

        _opened_cells = self.cell.open()

        if self.cell.is_mine:
            self.display_mine(True)
            self.game_field.fail()
            return

        self.display_cell_value()
        self.game_field.open_cells()
