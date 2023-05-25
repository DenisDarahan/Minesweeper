# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.relativelayout import RelativeLayout
# from kivy.uix.behaviors import FocusBehavior
# from kivy.properties import ObjectProperty, ListProperty
#
#
# Builder.load_string('''
# #:set LIGHT_GRAY (0.96, 0.96, 0.96, 1)  # (R: 247, G: 247, B: 247)
# #:set NORMAL_GRAY (0.75, 0.75, 0.75, 1)  # (R: 192, G: 192, B: 192)
# #:set DARK_GRAY (0.53, 0.53, 0.53, 1)  # (R: 136, G: 136, B: 136)
# #:set DOWN_LIGHT_GRAY (0.86, 0.86, 0.86, 1)
# #:set DOWN_NORMAL_GRAY (0.65, 0.65, 0.65, 1)
# #:set DOWN_DARK_GRAY (0.43, 0.43, 0.43, 1)
#
#
# <-TextInputField>:
#     #text_input_widget: None
#     disabled_foreground_color: NORMAL_GRAY
#
#     canvas.before:
#         Color:
#             rgba: DARK_GRAY if self.focus else (0, 0, 0, 0)
#         Rectangle:
#             pos: self._cursor_visual_pos
#             size: dp(2), -self._cursor_visual_height
#         Color:
#             rgba:
#                 self.disabled_foreground_color if self.disabled else \
#                 (self.hint_text_color if not self.text else self.foreground_color)
#
#     font_size: '25sp'
#
#
# <InputInfoLabel>:
#     markup: True
#     font_size:
#
#
# <DefaultTextInput>:
#     input_container: input_container
#     input_field: input_field
#
#     input_highlight: NORMAL_GRAY
#
#     canvas.before:
#         Color:
#             rgba: self.input_highlight
#         Line:
#             width: dp(2)
#             points: self.x, self.y, self.x + self.width, self.y
#
#     on_focus: print(f'{self.focus = }'); self.input_highlight = (DARK_GRAY if self.focus else NORMAL_GRAY)
#
#     RelativeLayout:
#         id: input_container
#
#         TextInputField:
#             id: input_field
#             # focus: root.focus
#
# <RootWindow>:
#     padding: '20dp'
#
#     canvas.before:
#         Color:
#             rgba: 1, 1, 1, 1
#         Rectangle:
#             size: self.size
#             pos: self.pos
#
#     RelativeLayout:
#         DefaultTextInput:
#             # canvas.before:
#             #     Color:
#             #         rgba: 1, 0, 0, 0.5
#             #     Rectangle:
#             #         size: self.size
#             #         pos: self.pos
#
#             size_hint: None, None
#             size: '200dp', '40dp'
#             pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#
# ''')
#
#
# class TextInputField(TextInput):
#     pass
#
#
# class InputInfoLabel(Label):
#     pass
#
#
# class DefaultTextInput(FocusBehavior, BoxLayout):
#     input_container: RelativeLayout = ObjectProperty()
#     input_field: TextInputField = ObjectProperty()
#
#     input_highlight = ListProperty([])
#
#
# class RootWindow(BoxLayout):
#     pass
#
#
# class ExtendedTextInputApp(App):
#
#     def build(self):
#         return RootWindow()
#
#
# if __name__ == '__main__':
#     ExtendedTextInputApp().run()


from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ListProperty


Builder.load_string('''
#:set NORMAL_GRAY (0.75, 0.75, 0.75, 1)  # (R: 192, G: 192, B: 192)
#:set DARK_GRAY (0.53, 0.53, 0.53, 1)  # (R: 136, G: 136, B: 136)


<WarningLabel>:
    size_hint: None, None
    size: self.texture_size
    font_size: '15sp'
    color: 1, 0, 0, 1
    markup: True


# <-TextInputField>:
#     input_highlight: NORMAL_GRAY
# 
#     canvas.before:
#         Color:
#             rgba: self.input_highlight
#         Line:
#             width: dp(2)
#             points: self.x, self.y, self.x + self.width, self.y
#         Color:
#             rgba: DARK_GRAY if self.focus else (0, 0, 0, 0)
#         Rectangle:
#             pos: self._cursor_visual_pos
#             size: dp(2), -self._cursor_visual_height
#         Color:
#             rgba:
#                 self.disabled_foreground_color if self.disabled else \
#                 (self.hint_text_color if not self.text else self.foreground_color)
# 
#     font_size: '25sp'
#     on_focus: self.input_highlight = (DARK_GRAY if self.focus else NORMAL_GRAY)


<-DefaultTextInput>:
    # text_input_field: text_input_field
    # font_size: text_input_field.font_size
    # 
    # TextInputField:
    #     id: text_input_field
    #     font_size: root.font_size

    input_highlight: NORMAL_GRAY

    canvas.before:
        Color:
            rgba: self.input_highlight
        Line:
            width: dp(2)
            points: self.x, self.y, self.x + self.width, self.y
        Color:
            rgba: DARK_GRAY if self.focus else (0, 0, 0, 0)
        Rectangle:
            pos: self._cursor_visual_pos
            size: dp(2), -self._cursor_visual_height
        Color:
            rgba:
                self.disabled_foreground_color if self.disabled else \
                (self.hint_text_color if not self.text else self.foreground_color)

    font_size: '25sp'
    on_focus: self.input_highlight = (DARK_GRAY if self.focus else NORMAL_GRAY)


<RootWindow>:
    padding: '20dp'

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        RelativeLayout:
            BoxLayout:
                size_hint: None, None
                size: '200dp', '40dp'
                pos_hint: {'right': 0.9, 'center_y': 0.5}

                DefaultTextInput:
                    id: input_field
                    canvas.before:
                        Color:
                            rgba: 1, 0, 0, 0.5
                        Rectangle:
                            size: self.size
                            pos: self.pos
                    font_size: '20sp'

    BoxLayout:
        RelativeLayout:
            Button:
                size_hint: None, None
                size: '150dp', '50dp'
                pos_hint: {'x': 0.1, 'center_y': 0.5}
                font_size: '25sp'
                text: 'Warning'
                on_release: input_field.warning('Bad input')
''')


class WarningLabel(Label):

    def __init__(self, warning: str, **kwargs):
        super().__init__(**kwargs)
        self.text = f'[i][u]{warning}[/u][/i]'
        Clock.schedule_once(lambda _dt: self._set_pos())

    def _set_pos(self):
        self.right = self.parent.right
        self.center_y = self.parent.center_y


# class TextInputField(TextInput):
#     input_highlight = ListProperty([])


class DefaultTextInput(TextInput, RelativeLayout):
    # text_input_field: TextInputField = ObjectProperty()
    # font_size = ObjectProperty()

    input_highlight = ListProperty([])

    def warning(self, text: str):
        warning_label = WarningLabel(text)
        self.add_widget(warning_label)
        print(self.pos, warning_label.pos, warning_label.parent)
        Clock.schedule_once(lambda _dt: self.remove_widget(warning_label), 1)


class RootWindow(BoxLayout):
    pass


class ExtendedTextInputApp(App):

    def build(self):
        return RootWindow()


if __name__ == '__main__':
    ExtendedTextInputApp().run()
