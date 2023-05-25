from kivy.graphics import Color, Line
from kivy.clock import Clock
from kivy.metrics import dp

from ..default_button import DefaultButton


class StatusButton(DefaultButton):
    _status: str
    _available_status: tuple = ('normal', 'fail', 'success')

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str):
        if value not in self._available_status:
            raise ValueError(f'{self.__class__.__name__}: status {value} not valid, '
                             f'only {self._available_status} available')

        self._status = value
        Clock.schedule_once(lambda _dt: getattr(self, f'_display_{self._status}')())

    @status.deleter
    def status(self):
        self.status = 'normal'

    def _clear_status(self):
        self.canvas.before.remove_group('left_eye')
        self.canvas.before.remove_group('right_eye')
        self.canvas.before.remove_group('mouth')

    def _display_normal(self):
        self._clear_status()

        with self.canvas.before:
            Color(rgba=(0, 0, 0, 1))
            Line(
                group='left_eye',
                width=dp(1),
                circle=(self.x + 0.42 * self.width, self.y + 0.57 * self.height, dp(1))
            )
            Line(
                group='right_eye',
                width=dp(1),
                circle=(self.x + 0.58 * self.width, self.y + 0.57 * self.height, dp(1))
            )
            Line(
                group='mouth',
                width=dp(1),
                ellipse=(self.x + 0.25 * self.width, self.y + 0.35 * self.height,
                         0.5 * self.width, 0.6 * self.height, 135, 225)
            )

    def _display_fail(self):
        self._clear_status()

        with self.canvas.before:
            Color(rgba=(0, 0, 0, 1))
            Line(
                group='left_eye',
                width=dp(1),
                points=(
                    self.x + 0.38 * self.width, self.y + 0.53 * self.height,
                    self.x + 0.38 * self.width + dp(3), self.y + 0.53 * self.height + dp(3)
                )
            )
            Line(
                group='left_eye',
                width=dp(1),
                points=(self.x + 0.38 * self.width + dp(3), self.y + 0.53 * self.height,
                        self.x + 0.38 * self.width, self.y + 0.53 * self.height + dp(3))
            )
            Line(
                group='right_eye',
                width=dp(1),
                points=(
                    self.x + 0.55 * self.width, self.y + 0.53 * self.height,
                    self.x + 0.55 * self.width + dp(3), self.y + 0.53 * self.height + dp(3)
                )
            )
            Line(
                group='right_eye',
                width=dp(1),
                points=(self.x + 0.55 * self.width + dp(3), self.y + 0.53 * self.height,
                        self.x + 0.55 * self.width, self.y + 0.53 * self.height + dp(3))
            )
            Line(
                group='mouth',
                width=dp(1),
                ellipse=(self.x + 0.25 * self.width, self.y - 0.2 * self.height,
                         0.5 * self.width, 0.6 * self.height, 325, 395)
            )

    def _display_success(self):
        with self.canvas.before:
            Color(rgba=(0, 0, 0, 1))
            Line(
                group='left_eye',
                width=dp(2),
                cap='square',
                points=(self.x + 0.23 * self.width, self.y + 0.62 * self.height,
                        self.x + 0.77 * self.width, self.y + 0.62 * self.height)
            )
            Line(
                group='left_eye',
                width=dp(2),
                cap='square',
                points=(self.x + 0.28 * self.width, self.y + 0.62 * self.height - dp(2),
                        self.x + 0.42 * self.width, self.y + 0.62 * self.height - dp(2))
            )
            Line(
                group='right_eye',
                width=dp(2),
                cap='square',
                points=(self.x + 0.58 * self.width, self.y + 0.62 * self.height - dp(2),
                        self.x + 0.72 * self.width, self.y + 0.62 * self.height - dp(2))
            )
            Line(
                group='left_eye',
                width=dp(2),
                cap='square',
                points=(self.x + 0.33 * self.width, self.y + 0.62 * self.height - dp(4),
                        self.x + 0.37 * self.width, self.y + 0.62 * self.height - dp(4))
            )
            Line(
                group='right_eye',
                width=dp(2),
                cap='square',
                points=(self.x + 0.62 * self.width, self.y + 0.62 * self.height - dp(4),
                        self.x + 0.67 * self.width, self.y + 0.62 * self.height - dp(4))
            )
