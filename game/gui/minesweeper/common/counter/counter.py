from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from .number import Number


class Counter(BoxLayout):
    first_number: Number = ObjectProperty()
    second_number: Number = ObjectProperty()
    third_number: Number = ObjectProperty()

    _number: int = 0

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, value: int):
        self._number = int(value)  # may raise ValueError
        self.display()

    @number.deleter
    def number(self):
        self.number = 0

    def display(self):
        _number = max(self.number, 0)

        self.first_number.display(_number // 100 % 10)
        self.second_number.display(_number // 10 % 10)
        self.third_number.display(_number % 10)
