from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

from game.core import Field
from gui.minesweeper.templates import FadingLayout, CellButton


class GameField(FadingLayout):
    mine_field: GridLayout = ObjectProperty()

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
        # self.build_game()
        pass
