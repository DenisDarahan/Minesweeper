from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, BooleanProperty


class FadingLayout(BoxLayout):
    blur_color = ListProperty([1, 1, 1])

    left_blur = BooleanProperty(True)
    top_blur = BooleanProperty(True)
    right_blur = BooleanProperty(True)
    bottom_blur = BooleanProperty(True)
