from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, NumericProperty
from kivy.clock import ClockEvent, Clock


Builder.load_string('''
#:import math math


<DefaultButton>:
    normal_light_color: 0.96, 0.96, 0.96, 1
    normal_dark_color: 0.53, 0.53, 0.53, 1
    normal_face_color: 0.75, 0.75, 0.75, 1
    down_light_color: 0.86, 0.86, 0.86, 1
    down_dark_color: 0.43, 0.43, 0.43, 1
    down_face_color: 0.65, 0.65, 0.65, 1

    # border_line_width: math.ceil(max(self.size) * 7 / 100)
    # middle_line_width: math.ceil(self.border_line_width / 2)
    # shift_width: math.ceil(max(self.size) / 100)
    r: math.ceil(max(self.size) / 25)
    d: (math.sqrt(2) - 1) / math.sqrt(2) * self.r
    flag: 0

    light_side: self.normal_light_color
    dark_side: self.normal_dark_color
    face: self.normal_face_color
    

    canvas.before:
        # Color:
        #     rgba: self.light_side
        # Line:
        #     width: self.border_line_width
        #     points: self.x + self.middle_line_width, self.y + self.middle_line_width, \
        #     self.x + self.middle_line_width, self.y + self.height - self.middle_line_width, \
        #     self.x + self.width - self.middle_line_width, self.y + self.height - self.middle_line_width
        # Color:
        #     rgba: self.dark_side
        # Line:
        #     width: self.border_line_width
        #     points: self.x + self.middle_line_width, self.y + self.middle_line_width, \
        #     self.x + self.width - self.middle_line_width, self.y + self.middle_line_width, \
        #     self.x + self.width - self.middle_line_width, self.y + self.height - self.middle_line_width
        # Color:
        #     rgba: self.light_side
        # Line:
        #     width: self.middle_line_width + self.shift_width
        #     cap_precision: self.middle_line_width // self.shift_width
        #     points: self.x - self.shift_width, self.y + self.middle_line_width + self.shift_width, \
        #     self.x + self.width - self.middle_line_width - self.shift_width, self.y + self.height + self.shift_width

        # Color:
        #     rgba: self.dark_side
        # RoundedRectangle:
        #     size: self.size
        #     pos: self.pos
        #     radius: [self.middle_line_width // 2]
        # Color:
        #     rgba: self.light_side
        # Triangle:
        #     points: self.x, self.y, self.x, self.y + self.height, self.x + self.width, self.y + self.height

        Color:
            rgba: self.dark_side
        Ellipse:
            angle_start: 135
            angle_end: 225
            pos: self.x, self.y
            size: 2 * self.r, 2 * self.r
        Ellipse:
            angle_start: 45
            angle_end: 225
            pos: self.x + self.width - 2 * self.r, self.y
            size: 2 * self.r, 2 * self.r
        Ellipse:
            angle_start: 45
            angle_end: 135
            pos: self.x + self.width - 2 * self.r, self.y + self.height - 2 * self.r
            size: 2 * self.r, 2 * self.r
        Triangle:
            points: self.x + self.d, self.y + self.d, self.x + self.width - self.d, self.y + self.d, \
            self.x + self.width - self.d, self.y + self.height - self.d
        Line:
            cap: 'none'
            width: self.d
            points: self.x + self.r, self.y + self.d, self.x + self.width - self.r, self.y + self.d
        Line:
            cap: 'none'
            width: self.d
            points: self.x + self.width - self.d, self.y + self.r, self.x + self.width - self.d, \
            self.y + self.height - self.r

        Color:
            rgba: self.light_side
        Ellipse:
            angle_start: -45
            angle_end: -135
            pos: self.x, self.y
            size: 2 * self.r, 2 * self.r
        Ellipse:
            angle_start: 45
            angle_end: -135
            pos: self.x, self.y + self.height - 2 * self.r
            size: 2 * self.r, 2 * self.r
        Ellipse:
            angle_start: 45
            angle_end: -45
            pos: self.x + self.width - 2 * self.r, self.y + self.height - 2 * self.r
            size: 2 * self.r, 2 * self.r
        Triangle:
            points: self.x + self.d, self.y + self.d, self.x + self.d, self.y + self.height - self.d, \
            self.x + self.width - self.d, self.y + self.height - self.d
        Line:
            cap: 'none'
            width: self.d
            points: self.x + self.d, self.y + self.r, self.x + self.d, self.y + self.height - self.r
        Line:
            cap: 'none'
            width: self.d
            points: self.x + self.r, self.y + self.height - self.d, self.x + self.width - self.r, \
            self.y + self.height - self.d

        Color:
            rgba: self.face
        RoundedRectangle:
            size: 0.8 * self.width, 0.8 * self.height
            pos: self.x + 0.1 * self.width, self.y + 0.1 * self.height
            radius: [self.r]

        Color:
            rgba: 0, 0, 0, self.flag
        Line:
            width: self.r
            points: self.x + self.width / 2 + self.r, self.y + self.height / 2 + self.d, \
            self.x + self.width / 2 + self.r, self.y + 0.2 * self.height + self.r
        Line:
            cap: 'none'
            width: self.r
            points: self.x + 0.25 * self.width, self.y + 0.2 * self.height + self.r, \
            self.x + 0.75 * self.width, self.y + 0.2 * self.height + self.r
        Line:
            cap: 'none'
            width: self.r
            points: self.x + 0.3 * self.width, self.y + 0.2 * self.height + 2 * self.r, \
            self.x + 0.7 * self.width, self.y + 0.2 * self.height + 2 * self.r
        Color:
            rgba: 1, 0, 0, self.flag
        Triangle:
            points: self.x + self.width / 2 + 2 * self.r, self.y + self.height / 2, \
            self.x + self.width / 2 + 2 * self.r, self.y + 0.8 * self.height, self.x + 0.2 * self.width, \
            self.y + 0.65 * self.height

    size_hint: None, None
    size: '30dp', '30dp'

    background_color: 0, 0, 0, 0
    background_normal: ''
    background_down: ''

    font_size: '30sp'

    on_touch_down: self.on_right_click(*args)
    on_long_press: self.set_flag()
    on_release: print(f'{self.r = }, {self.d = }')


<RootWindow>:
    padding: '20dp'

    RelativeLayout:

        BoxLayout:
            size_hint: None, None
            size: '200dp', '100dp'
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            DefaultButton:
            DefaultButton:

''')


class DefaultButton(Button):
    normal_light_color = ListProperty([0.96, 0.96, 0.96, 1])
    normal_dark_color = ListProperty([0.53, 0.53, 0.53, 1])
    normal_face_color = ListProperty([0.75, 0.75, 0.75, 1])
    down_light_color = ListProperty([0.86, 0.86, 0.86, 1])
    down_dark_color = ListProperty([0.43, 0.43, 0.43, 1])
    down_face_color = ListProperty([0.65, 0.65, 0.65, 1])

    r = NumericProperty(1)
    d = NumericProperty(1)
    flag = NumericProperty(0)

    light_side = ListProperty(normal_light_color.defaultvalue)
    dark_side = ListProperty(normal_dark_color.defaultvalue)
    face = ListProperty(normal_face_color.defaultvalue)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.bind(on_touch_down=self.on_right_click)

    def on_right_click(self, _instance, touch):
        if touch.button == 'right' and self.collide_point(*touch.pos):
            self.set_flag()

    def set_flag(self):
        self.flag = 0 ** self.flag

    def set_face_color(self):
        pass

    def on_press(self):
        self.light_side = self.down_light_color
        self.dark_side = self.down_dark_color
        self.face = self.down_face_color
        super().on_press()

    def on_release(self):
        self.light_side = self.normal_light_color
        self.dark_side = self.normal_dark_color
        self.face = self.normal_face_color
        super().on_release()

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


class RootWindow(BoxLayout):
    pass


class DefaultButtonApp(App):

    def build(self):
        return RootWindow()


if __name__ == '__main__':
    DefaultButtonApp().run()
