import typing


class Field:

    def __init__(self, value: typing.Any = None):
        self._value = value
        self._default_value = value

    def __set_name__(self, owner: typing.Any, name: typing.Any):
        self.name = name

    def __set__(self, instance: typing.Any, value: typing.Any):
        self._value = value

    def __get__(self, instance: typing.Any, owner: typing.Any) -> typing.Any:
        return self._value

    def __delete__(self, instance: typing.Any):
        self._value = self._default_value


class IntField:

    def __set__(self, instance, value):
        self._value = int(value)  # can raise ValueError
