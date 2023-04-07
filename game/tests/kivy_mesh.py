# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.boxlayout import BoxLayout
#
# Builder.load_string("""
# <RootWidget>:
#     RelativeLayout:
#
#         BoxLayout:
#             canvas.before:
#                 Color:
#                     rgba: 1, 0, 0, 0.5
#                 Rectangle:
#                     size: self.size
#                     pos: self.pos
#                 Color:
#                     rgba: 0, 1, 0, 0.9
#                 Mesh:
#                     mode: "triangle_fan"
#                     vertices: [self.x, self.y, 0, 0, self.x, self.y + self.height, dp(100), dp(100), self.x + self.width, self.y + self.height, 0, 0]
#                     indices: [0, 1, 2]
#
#             size_hint: None, None
#             size: '200dp', '200dp'
#             pos_hint: {'center_x': 0.5, 'center_y': 0.5}
# """)
#
#
# class RootWidget(BoxLayout):
#     pass
#
#
# class MyApp(App):
#
#     def build(self):
#         return RootWidget()
#
#
# if __name__ == '__main__':
#     MyApp().run()


from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty


kv = '''
BoxLayout:
    orientation: 'vertical'
    Widget:
        canvas:
            Mesh:
                vertices: app.vertices
                indices: app.indices
                mode: app.mode
        on_touch_down:
            if self.collide_point(*args[1].pos): app.add_point(args[1].pos)
    BoxLayout:
        size_hint_y: None
        height: '20sp'
        Spinner:
            text: app.mode
            values:
                'points', 'line_strip', 'line_loop', 'lines',\
                'triangle_strip', 'triangle_fan'
            on_text: app.mode = args[1]
        Button:
            text: 'clear'
            on_press: app.clear()
'''


class TriangleApp(App):
    vertices = ListProperty([])
    indices = ListProperty([])
    mode = StringProperty('points')

    def build(self):
        return Builder.load_string(kv)

    def add_point(self, pos):
        self.vertices.extend([pos[0], pos[1], 0, 0])
        self.indices.append(len(self.indices))

    def clear(self):
        self.vertices = []
        self.indices = []


if __name__ == '__main__':
    TriangleApp().run()
