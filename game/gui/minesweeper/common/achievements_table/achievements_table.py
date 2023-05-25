from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty


class AchievementsLabel(Label):
    pass


class AchievementsTable(BoxLayout):
    achievements: list[dict] = ListProperty()
    names: BoxLayout = ObjectProperty()
    values: BoxLayout = ObjectProperty()

    def on_achievements(self, _self_instance, _achievements: list[dict]):
        for achievement in self.achievements:
            self.names.add_widget(AchievementsLabel(text=achievement['name'], halign='right'))
            self.values.add_widget(AchievementsLabel(text=achievement['value'], halign='left'))
