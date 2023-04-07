from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.recycleview import RecycleView, views
from kivy.graphics import Color, Rectangle, Line
from kivy.input.motionevent import MotionEvent
from kivy.properties import NumericProperty
from kivy.metrics import dp

from game.core import Cell
from ..default_button import DefaultButton
from ..long_press_button import LongPressButton


class CellButton(DefaultButton, LongPressButton):
    flag = NumericProperty(0)
    opened = NumericProperty(0)
    is_mine = NumericProperty(0)

    game_field: BoxLayout
    cell: Cell
    last_touch_id: str = ''  # prevents from firing on_long_press or on_release

    def __init__(self, game_field: BoxLayout, cell: Cell, **kwargs):
        super().__init__(**kwargs)

        self.game_field = game_field
        self.cell = cell
        self.is_mine = int(self.cell.is_mine())

    def create_widgets(self):
        pass

    def display_mine(self):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=(1, 0, 0, 1))
            Rectangle(size=self.size, pos=self.pos)

    def display_cell_value(self, value: int):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=(0.75, 0.75, 0.75, 1))
            Rectangle(size=self.size, pos=self.pos)
            Color(rgba=(0.52, 0.52, 0.52, 1))
            Line(width=dp(1), rectangle=(self.x, self.y, self.width, self.height))

        self.text = str(value or ' ')

    def on_flag(self, _instance, value: int):
        self.cell.flag = bool(value)

    def on_right_click(self, _instance: DefaultButton, touch: MotionEvent):
        if touch.button == 'right' and self.collide_point(*touch.pos):
            self.last_touch_id = touch.id
            self.change_flag()

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

        opened_cells = self.cell.open()

        if opened_cells[0].is_mine():
            self.display_mine()
            self.game_field.end_game()
            return

        self.display_cell_value(opened_cells[0].value)
        self.game_field.open_cells()
