import math
import random

from game.core.cell import Cell


class Field:
    _MIN_WIDTH: int = 5
    _MIN_HEIGHT: int = 5
    _MAX_WIDTH: int
    _MAX_HEIGHT: int

    width: int
    height: int
    mines_amount: int
    field: list[list[Cell]]

    def __init__(self, width: int, height: int, mines_amount: int = None):
        if width < self._MIN_WIDTH or height < self._MIN_HEIGHT:
            raise ValueError(f'Too small field, at least {self._MIN_WIDTH}x{self._MIN_HEIGHT} available')

        _max_mines = int(width * height / 2)
        if mines_amount is not None and mines_amount > _max_mines:
            raise ValueError(f'Too many mines, not more than {_max_mines} available')

        self.height = height
        self.width = width
        self.mines_amount = mines_amount or int(math.sqrt(self.height * self.width))

        self.field = self.generate()

    def generate(self) -> list[list]:
        field = [[Cell() for _x in range(self.width)] for _y in range(self.height)]

        self._set_neighbours(field)
        self._set_mines(field, self.mines_amount)
        self._set_values(field)

        return field

    def _set_neighbours(self, field: list[list]):
        field[0][0].set_neighbours(None, None, field[0][1], field[1][1], field[1][0], None, None, None)
        field[0][-1].set_neighbours(None, None, None, None, field[1][-1], field[1][-2], field[0][-2], None)
        field[-1][0].set_neighbours(field[-2][0], field[-2][1], field[-1][1], None, None, None, None, None)
        field[-1][-1].set_neighbours(field[-2][-1], None, None, None, None, None, field[-1][-2], field[-2][-2])

        for column in range(1, self.width - 1):
            field[0][column].set_neighbours(None, None, field[0][column + 1], field[1][column + 1],
                                            field[1][column], field[1][column - 1], field[0][column - 1], None)
            field[-1][column].set_neighbours(field[-2][column], field[-2][column + 1], field[-1][column + 1], None,
                                             None, None, field[-1][column - 1], field[-2][column - 1])

        for row in range(1, self.height - 1):
            field[row][0].set_neighbours(field[row - 1][0], field[row - 1][1], field[row][1], field[row + 1][1],
                                         field[row + 1][0], None, None, None)
            field[row][-1].set_neighbours(field[row - 1][-1], None, None, None,
                                          field[row + 1][-1], field[row + 1][-2], field[row][-2], field[row - 1][-2])

        for y in range(1, self.height - 1):
            north, south = y - 1, y + 1

            for x in range(1, self.width - 1):
                east, west = x + 1, x - 1

                field[y][x].set_neighbours(field[north][x], field[north][east], field[y][east], field[south][east],
                                           field[south][x], field[south][west], field[y][west], field[north][west])

    def _set_mines(self, field: list[list], mines_amount: int):
        for mine in range(mines_amount):
            while True:
                x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
                if field[y][x].value:
                    continue
                field[y][x].set_mine()
                break

    @classmethod
    def _set_values(cls, field: list[list[Cell]]):
        for row in field:
            for cell in row:
                cell.set_value()

    def game_ended(self) -> bool:
        return all([cell.opened or cell.is_mine for row in self.field for cell in row])

    def display(self):
        print(self)

    def __str__(self) -> str:
        return '\n'.join([''.join(f'{cell: ^3}' for cell in row) for row in self.field])


if __name__ == '__main__':
    Field(10, 10, 10).display()
