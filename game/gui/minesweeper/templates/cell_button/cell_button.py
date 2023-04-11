import math

from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle, Line, RoundedRectangle
from kivy.input.motionevent import MotionEvent
from kivy.properties import NumericProperty
from kivy.metrics import dp

from game.core import Cell
from ..default_button import DefaultButton
from ..long_press_button import LongPressButton


class CellButton(DefaultButton, LongPressButton):
    flag = NumericProperty(0)

    game_field: BoxLayout
    cell: Cell
    last_touch_id: str = ''  # prevents from firing on_long_press or on_release

    def __init__(self, game_field: BoxLayout, cell: Cell, **kwargs):
        super().__init__(**kwargs)

        self.game_field = game_field
        self.cell = cell

    def display_mine(self, user_pressed: bool = False):
        self.canvas.before.clear()

        with self.canvas.before:
            Color(rgba=(0.52, 0.52, 0.52, 1))
            Line(width=dp(1), rectangle=(self.x, self.y, self.width, self.height))
            Color(rgba=(1, 0, 0, int(user_pressed)))
            Rectangle(size=(self.width + dp(2), self.height), pos=(self.x + dp(1), self.y - dp(1)))
            Color(rgba=(0, 0, 0, 1))
            Line(
                width=dp(1),
                cap='square',
                points=(self.x + self.width / 2, self.y + self.height * 0.15,
                        self.x + self.width / 2, self.y + self.height * 0.85)
            )
            Line(
                width=dp(1),
                cap='square',
                points=(self.x + self.width * 0.15, self.y + self.height / 2,
                        self.x + self.width * 0.85, self.y + self.height / 2)
            )
            Line(
                width=dp(1),
                cap='square',
                points=(
                    self.x + 0.7 * self.height / (2 * math.sqrt(2)),
                    self.y + 0.7 * self.width / (2 * math.sqrt(2)),
                    self.x + self.width - 0.7 * self.height / (2 * math.sqrt(2)),
                    self.y + self.height - 0.7 * self.width / (2 * math.sqrt(2))
                )
            )
            Line(
                width=dp(1),
                cap='square',
                points=(
                    self.x + 0.7 * self.height / (2 * math.sqrt(2)),
                    self.y + self.height - 0.7 * self.width / (2 * math.sqrt(2)),
                    self.x + self.width - 0.7 * self.height / (2 * math.sqrt(2)),
                    self.y + 0.7 * self.width / (2 * math.sqrt(2))
                )
            )
            RoundedRectangle(
                size=(self.width * 0.6, self.height * 0.6),
                pos=(self.x + self.width * 0.2, self.y + self.height * 0.2),
                radius=[max(self.width, self.height)]
            )

    def display_cell_value(self, value: int):
        self.canvas.before.clear()

        with self.canvas.before:
            Color(rgba=(0.75, 0.75, 0.75, 1))
            Rectangle(size=self.size, pos=self.pos)
            Color(rgba=(0.52, 0.52, 0.52, 1))
            Line(width=dp(1), rectangle=(self.x, self.y, self.width, self.height))

        self.text = str(value)

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

        _opened_cells = self.cell.open()

        if self.cell.is_mine():
            self.display_mine(True)
            self.game_field.fail()
            return

        self.display_cell_value(self.cell.value)
        self.game_field.open_cells()
