from kivy.uix.button import Button
from kivy.properties import NumericProperty, ListProperty


class DefaultButton(Button):
    normal_light_color = ListProperty([0.96, 0.96, 0.96, 1])
    normal_dark_color = ListProperty([0.53, 0.53, 0.53, 1])
    normal_face_color = ListProperty([0.75, 0.75, 0.75, 1])
    down_light_color = ListProperty([0.86, 0.86, 0.86, 1])
    down_dark_color = ListProperty([0.43, 0.43, 0.43, 1])
    down_face_color = ListProperty([0.65, 0.65, 0.65, 1])

    round_radius = NumericProperty(1)
    radius_distance = NumericProperty(1)

    light_side = ListProperty(normal_light_color.defaultvalue)
    dark_side = ListProperty(normal_dark_color.defaultvalue)
    face = ListProperty(normal_face_color.defaultvalue)

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
