from kivy.properties import ObjectProperty

from ...common import BasePopup, AchievementsTable


class GameAchievements(BasePopup):
    achievements_table: AchievementsTable = ObjectProperty()

    time: int
    score: int

    def __init__(self, time: int, score: int, **kwargs):
        super().__init__(**kwargs)

        self.time = time
        self.score = score

    def on_pre_open(self):
        self.achievements_table.achievements = [
            {'name': 'Time', 'value': f'{self.time} sec'},
            {'name': 'Score', 'value': f'{self.score}'}
        ]
