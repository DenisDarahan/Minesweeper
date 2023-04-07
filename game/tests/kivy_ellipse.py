from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

Builder.load_string('''
# For the arcs, we have to give the start,
# and the end angle. We use default number of segments,
# 180, and 5, for the two ellipse arcs.
# The rest of the kv file, corresponds, to the other,
# 6 ellipse arcs, following the same pattern.

#:set angle_start_row2 240
#:set angle_end_row2 480
#:set angle_start_row3 120
#:set angle_end_row3 240


<EllipseLayout>:
    cols:4

    canvas.before:
        Color:
            rgba: 0, 0, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        canvas.before:
            Color:
                rgba: 1, .8, .5, 1
            Ellipse:
                pos: self.pos
                size: self.size

    BoxLayout:
        canvas.before:
            Ellipse:
                segments: 5
                pos: self.pos
                size: self.size

    BoxLayout:
        canvas.before:
            Ellipse:
                segments: 4
                pos: self.pos
                size: self.size

    BoxLayout:
        canvas.before:
            Ellipse:
                segments: 3
                pos: self.pos
                size: self.size

    BoxLayout:
        canvas.before:
            Color:
                rgba: 1, .59, .86, 1
            Ellipse:
                angle_start: angle_start_row2
                angle_end: angle_end_row2
                pos: self.pos
                size: self.size

    BoxLayout:
        canvas.before:
            Ellipse:
                angle_start: angle_start_row2
                angle_end: angle_end_row2
                segments: 5
                pos: self.pos
                size: self.size

    BoxLayout:
        canvas.before:
            Ellipse:
                angle_start: angle_start_row2
                angle_end: angle_end_row2
                segments: 4
                pos: self.pos
                size: self.size

    BoxLayout:
        canvas.before:
            Ellipse:
                angle_start: angle_start_row2
                angle_end: angle_end_row2
                segments: 3
                pos: self.pos
                size: self.size

    BoxLayout:
        canvas.before:
            Color:
                rgba: .5, .5, .5, 1
            Ellipse:
                angle_start: angle_start_row3
                angle_end: angle_end_row3
                pos: self.pos
                size: self.size

    BoxLayout:
        canvas.before:
            Ellipse:
                angle_start: angle_start_row3
                angle_end: angle_end_row3
                segments: 5
                pos: self.pos
                size: self.size

    BoxLayout:
        canvas.before:
            Ellipse:
                angle_start: angle_start_row3
                angle_end: angle_end_row3
                segments: 4
                pos: self.pos
                size: self.size

    BoxLayout:
        canvas.before:
            Ellipse:
                angle_start: angle_start_row3
                angle_end: angle_end_row3
                segments: 3
                pos: self.pos
                size: self.size
''')


class EllipseLayout(GridLayout):
    pass


class EllipseApp(App):
    def build(self):
        return EllipseLayout()


if __name__ == '__main__':
    EllipseApp().run()
