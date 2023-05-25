from pathlib import Path

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


Builder.load_string('''
<RootWindow>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    Image:
        source: 'validate.png'

''')


class RootWindow(BoxLayout):
    pass


class ImageApp(App):

    def build(self):
        return RootWindow()


if __name__ == '__main__':
    print(Path('validate.png').exists())
    ImageApp().run()
