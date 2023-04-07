import typing


class Cell:
    value: int
    opened: bool
    flag: bool
    neighbours: 'list[typing.Any]'

    def __init__(self, value: int = 0):
        self.value = value
        self.opened = False
        self.flag = False

    def set_neighbours(self, north: object, north_east: object, east: object, south_east: object,
                       south: object, south_west: object, west: object, north_west: object):
        self.neighbours = [*filter(None, [north, north_east, east, south_east, south, south_west, west, north_west])]

    def set_mine(self):
        self.value = -1

    def is_mine(self) -> bool:
        return self.value == -1

    def set_value(self):
        if self.value:
            return
        self.value = len([*filter(lambda cell: cell is not None and cell.is_mine(), self.neighbours)])

    def open(self) -> list[typing.Any]:
        opened_cells = [self]

        if not self.opened:
            self.opened = True

            if not self.value:  # self.value == 0
                # opened_cells.extend(self.open_neighbours())
                opened_cells.extend(neighbour.open() for neighbour in self.neighbours)

        return opened_cells

    def open_neighbours(self) -> typing.Generator:
        # for neighbour in self.neighbours:
        #     neighbour.open()
        return (neighbour.open() for neighbour in self.neighbours)

    def __format__(self, format_spec: str) -> str:
        return format(self.value, format_spec)

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(value={self.value}, opened={self.opened}, flag={self.flag})'
