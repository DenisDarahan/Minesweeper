from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.properties import ObjectProperty, ListProperty


class MenuButton(Button):
    pass


class MenuDropDown(DropDown):

    def __init__(self, menu_list: list[dict], **kwargs):
        super().__init__(**kwargs)

        for menu in menu_list:
            self.add_widget(MenuButton(**menu))

    def on_parent(self, _self_instance, _window):
        self.width = max(c.width for c in self.children[0].children)


class MenuBarButton(Button):
    menu_list: list[dict] = ListProperty([])
    menu_drop_down: DropDown = ObjectProperty()

    def on_kv_post(self, base_widget):
        self.menu_drop_down = MenuDropDown(self.menu_list)
        self.bind(on_release=self.menu_drop_down.open)
