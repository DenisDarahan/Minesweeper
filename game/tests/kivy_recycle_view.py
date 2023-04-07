from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.uix.label import Label


Builder.load_string('''
#:import ScrollEffect kivy.effects.scroll.ScrollEffect


<UserLabel>:
    canvas.before:
        Color:
            rgba: 1, 0, 0, 0.3
        Rectangle:
            size: self.size
            pos: self.pos


<UserButton>:
    canvas.before:
        Color:
            rgba: 0, 1, 0, 0.3
        Rectangle:
            size: self.size
            pos: self.pos

    background_normal: ''
    background_color: 0, 0, 0, 0

    on_release: self.change_text()


# <RV>:
#     viewclass: 'UserLabel'
#     effect_cls: ScrollEffect
#     RecycleBoxLayout:
#         default_size_hint: 1, None
#         default_size: None, dp(56)
#         size_hint_y: None
#         height: self.minimum_height
#         orientation: 'vertical'
#         spacing: '1dp'

<RV>:
    viewclass: 'UserButton'
    effect_cls: ScrollEffect
    RecycleGridLayout:
        default_size_hint: None, None
        default_size: '100dp', '100dp'
        size_hint: None, None
        size: self.minimum_width, self.minimum_height
        rows: 10
        cols: 10
        spacing: '1dp'
''')


class Cell:
    flag: bool = False


class UserLabel(Label):
    pass


class UserButton(RecycleDataViewBehavior, Button):
    parent_layout: RecycleView
    index: int
    cell: Cell

    def refresh_view_attrs(self, rv, index, data):
        self.parent_layout = rv
        self.index = index
        self.cell = data['cell']
        data['text'] = str(self.cell.flag)
        super().refresh_view_attrs(rv, index, data)

    def change_text(self):
        # self.text = str(int(self.text) ** 2)
        self.cell.flag = not self.cell.flag
        self.text = str(self.cell.flag)
        # self.parent_layout.data[self.index]['text'] = self.text


class RV(RecycleView):

    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x), 'parent_layout': self, 'cell': Cell()} for x in range(100)]


class TestApp(App):
    def build(self):
        return RV()


if __name__ == '__main__':
    TestApp().run()
