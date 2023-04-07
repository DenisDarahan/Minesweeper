from kivy.uix.gridlayout import GridLayout
# from kivy.uix.recycleview import RecycleView
# from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty, NumericProperty

from game.core import Field, Cell
from gui.minesweeper.templates import FadingLayout, CellButton
# from ..mine_field import MineField


class GameField(FadingLayout):
    # scroll_widget: RecycleView = ObjectProperty()
    mine_field: GridLayout = ObjectProperty()
    # mine_field_container: RelativeLayout = ObjectProperty()
    # mine_field_width = NumericProperty(0)
    # mine_field_height = NumericProperty(0)

    field: Field

    def on_kv_post(self, base_widget):
        self.build_game(20, 20, 30)

    def build_game(self, width: int = 10, height: int = 10, mines_amount: int = 10):
        self.field = Field(width, height, mines_amount)

        self.mine_field.clear_widgets()
        self.mine_field.rows = width
        self.mine_field.cols = height
        for row in self.field.field:
            for cell in row:
                self.mine_field.add_widget(CellButton(self, cell))

        # self.scroll_widget.data = [{'game_field': self, 'cell': cell} for row in self.field.field for cell in row]

        # mine_field = MineField(
        #     self, width, height, [{'game_field': self, 'cell': cell} for row in self.field.field for cell in row])
        # mine_field.scroll_x = 0
        # mine_field.scroll_y = 1  # TODO
        # self.mine_field_width = mine_field.mine_field.width
        # self.mine_field_height = mine_field.mine_field.height
        # self.mine_field_container.add_widget(mine_field)

    def open_cells(self):
        if self.field.game_ended():
            self.end_game()
            return

        for cell_button in self.mine_field.children:
            if cell_button.cell.opened and not cell_button.opened:
                if cell_button.cell.is_mine():
                    cell_button.display_mine()
                else:
                    cell_button.display_cell_value(cell_button.cell.value)

    def end_game(self):
        self.build_game()
