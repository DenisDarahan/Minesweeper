from functools import reduce

from kivy.clock import Clock, ClockEvent
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.context import get_current_context
from kivy.properties import ObjectProperty

from game.core import Field
from game.gui.db import db
from game.gui.api import server_api
from ...common import CellButton
from ..game_achievements import GameAchievements


class GameField(BoxLayout):
    mine_field: GridLayout = ObjectProperty()
    root_window: BoxLayout = ObjectProperty()

    field: Field

    timer: ClockEvent = None
    _available_game_status: tuple[str] = ('new', 'started', 'ended')
    _game_status: str = 'new'

    @property
    def game_status(self) -> str:
        return self._game_status

    @game_status.setter
    def game_status(self, value: str):
        if value not in self._available_game_status:
            raise ValueError(f'{self.__class__.__name__}: status {value} not valid, '
                             f'only {self._available_game_status} available')

        if self._game_status == 'new' and value == 'started':
            self.timer = Clock.schedule_interval(self.update_timer, 1)
        elif value in {'new', 'ended'} and self.timer is not None:
            self.timer.cancel()

        self._game_status = value

    @game_status.deleter
    def game_status(self):
        self.game_status = 'new'

    def update_timer(self, _dt: float):
        self.root_window.time_counter.number += 1

    def on_kv_post(self, base_widget):
        self.build_game()

    def build_game(self):
        self.field = Field(**get_current_context()['field'])
        self.game_status = 'new'

        self.mine_field.clear_widgets()
        self.mine_field.rows = self.field.height
        self.mine_field.cols = self.field.width
        for row in self.field.field:
            for cell in row:
                self.mine_field.add_widget(CellButton(self, cell))

        self.root_window.mines_counter.number = self.field.mines_amount
        self.root_window.time_counter.number = 0

    def open_cells(self):
        if self.field.game_ended():
            self.success()
            return

        for cell_button in self.mine_field.children:
            if cell_button.cell.opened:
                if cell_button.cell.is_mine:
                    cell_button.display_mine()
                else:
                    cell_button.display_cell_value()

    def success(self):
        self.game_status = 'ended'
        self.root_window.status_button.status = 'success'

        field = get_current_context()['field']
        score = int(reduce(lambda a, b: a * b, field.values()) / self.root_window.time_counter.number)
        GameAchievements(self.root_window.time_counter.number, score).open()

        db.rate.create(True, **field, time=self.root_window.time_counter.number, score=score)
        server_api.create_rate(self.root_window.time_counter.number, score)

    def fail(self):
        self.game_status = 'ended'
        self.root_window.status_button.status = 'fail'

        for cell_button in self.mine_field.children:
            if cell_button.cell.is_mine and not cell_button.cell.opened:
                cell_button.display_mine()

        field = get_current_context()['field']
        db.rate.create(False, **field, time=self.root_window.time_counter.number)
