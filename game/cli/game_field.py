from game.core import Field


class GameField:
    _FLAG: str = '⚑'
    _MINE: str = '☀'

    width: int
    height: int
    field: Field

    def __init__(self, width: int = 10, height: int = 10, mines_amount: int = None):
        self.width = width
        self.height = height
        self.field = Field(height, width, mines_amount)

    def open(self, x: int, y: int) -> 'tuple[bool, bool]':
        opened_cells = self.field.field[y][x].open()

        if opened_cells[0].is_mine:
            return True, False
        return self.field.game_ended(), True

    def change_flag(self, x: int, y: int):
        if not self.field.field[y][x].opened:
            self.field.field[y][x].flag = not self.field.field[y][x].flag

    def _display_cell(self, row: int, column: int) -> str:
        cell = self.field.field[row][column]

        if cell.opened:
            symbol = self._MINE if cell.is_mine else cell.value
        else:
            symbol = self._FLAG if cell.flag else ' '

        return f'{symbol: ^3}'

    def display(self):
        print(self)

    def __str__(self) -> str:
        row_divider = '+'.join(['', *['---' for _column in range(self.height)], '']) + '\n'
        rows = ['|'.join(['', *[self._display_cell(row, column) for column in range(self.height)], '']) + '\n'
                for row in range(self.width)]
        return row_divider.join(['', *rows, ''])
