from kivy.uix.button import Button
from kivy.clock import ClockEvent, Clock
from kivy.properties import NumericProperty


class LongPressButton(Button):
    __events__ = ('on_long_press',)

    _long_press_time = NumericProperty(1.0)
    timer: ClockEvent = None

    def on_state(self, _instance: Button, value: str):
        if value == 'down':
            self.timer = Clock.schedule_once(self._do_long_press, self._long_press_time)
        else:
            if self.timer is not None:
                self.timer.cancel()

    def _do_long_press(self, _dt):
        self.dispatch('on_long_press')

    def on_long_press(self, *args):
        pass
