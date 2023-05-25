from kivy.properties import ListProperty

from kivy.uix.label import Label


class Number(Label):
    dash_passive = ListProperty([1, 0, 0, 0.25])
    dash_active = ListProperty([1, 0, 0, 0.9])

    def display(self, number: int):
        getattr(self, f'display_{number}')()

    def display_0(self):
        self.canvas.before.get_group('top')[0].rgba = self.dash_active
        self.canvas.before.get_group('top_left')[0].rgba = self.dash_active
        self.canvas.before.get_group('top_right')[0].rgba = self.dash_active
        self.canvas.before.get_group('middle')[0].rgba = self.dash_passive
        self.canvas.before.get_group('bottom_left')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom_right')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom')[0].rgba = self.dash_active

    def display_1(self):
        self.canvas.before.get_group('top')[0].rgba = self.dash_passive
        self.canvas.before.get_group('top_left')[0].rgba = self.dash_passive
        self.canvas.before.get_group('top_right')[0].rgba = self.dash_active
        self.canvas.before.get_group('middle')[0].rgba = self.dash_passive
        self.canvas.before.get_group('bottom_left')[0].rgba = self.dash_passive
        self.canvas.before.get_group('bottom_right')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom')[0].rgba = self.dash_passive

    def display_2(self):
        self.canvas.before.get_group('top')[0].rgba = self.dash_active
        self.canvas.before.get_group('top_left')[0].rgba = self.dash_passive
        self.canvas.before.get_group('top_right')[0].rgba = self.dash_active
        self.canvas.before.get_group('middle')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom_left')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom_right')[0].rgba = self.dash_passive
        self.canvas.before.get_group('bottom')[0].rgba = self.dash_active

    def display_3(self):
        self.canvas.before.get_group('top')[0].rgba = self.dash_active
        self.canvas.before.get_group('top_left')[0].rgba = self.dash_passive
        self.canvas.before.get_group('top_right')[0].rgba = self.dash_active
        self.canvas.before.get_group('middle')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom_left')[0].rgba = self.dash_passive
        self.canvas.before.get_group('bottom_right')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom')[0].rgba = self.dash_active

    def display_4(self):
        self.canvas.before.get_group('top')[0].rgba = self.dash_passive
        self.canvas.before.get_group('top_left')[0].rgba = self.dash_active
        self.canvas.before.get_group('top_right')[0].rgba = self.dash_active
        self.canvas.before.get_group('middle')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom_left')[0].rgba = self.dash_passive
        self.canvas.before.get_group('bottom_right')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom')[0].rgba = self.dash_passive

    def display_5(self):
        self.canvas.before.get_group('top')[0].rgba = self.dash_active
        self.canvas.before.get_group('top_left')[0].rgba = self.dash_active
        self.canvas.before.get_group('top_right')[0].rgba = self.dash_passive
        self.canvas.before.get_group('middle')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom_left')[0].rgba = self.dash_passive
        self.canvas.before.get_group('bottom_right')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom')[0].rgba = self.dash_active

    def display_6(self):
        self.canvas.before.get_group('top')[0].rgba = self.dash_active
        self.canvas.before.get_group('top_left')[0].rgba = self.dash_active
        self.canvas.before.get_group('top_right')[0].rgba = self.dash_passive
        self.canvas.before.get_group('middle')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom_left')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom_right')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom')[0].rgba = self.dash_active

    def display_7(self):
        self.canvas.before.get_group('top')[0].rgba = self.dash_active
        self.canvas.before.get_group('top_left')[0].rgba = self.dash_passive
        self.canvas.before.get_group('top_right')[0].rgba = self.dash_active
        self.canvas.before.get_group('middle')[0].rgba = self.dash_passive
        self.canvas.before.get_group('bottom_left')[0].rgba = self.dash_passive
        self.canvas.before.get_group('bottom_right')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom')[0].rgba = self.dash_passive

    def display_8(self):
        self.canvas.before.get_group('top')[0].rgba = self.dash_active
        self.canvas.before.get_group('top_left')[0].rgba = self.dash_active
        self.canvas.before.get_group('top_right')[0].rgba = self.dash_active
        self.canvas.before.get_group('middle')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom_left')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom_right')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom')[0].rgba = self.dash_active

    def display_9(self):
        self.canvas.before.get_group('top')[0].rgba = self.dash_active
        self.canvas.before.get_group('top_left')[0].rgba = self.dash_active
        self.canvas.before.get_group('top_right')[0].rgba = self.dash_active
        self.canvas.before.get_group('middle')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom_left')[0].rgba = self.dash_passive
        self.canvas.before.get_group('bottom_right')[0].rgba = self.dash_active
        self.canvas.before.get_group('bottom')[0].rgba = self.dash_active
