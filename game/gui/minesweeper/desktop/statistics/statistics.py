from kivy.properties import ObjectProperty

from game.gui.db import db
from ...common import BasePopup, AchievementsTable


class Statistics(BasePopup):
    achievements_table: AchievementsTable = ObjectProperty()

    def on_pre_open(self):
        stats = db.rate.statistics()
        self.achievements_table.achievements = [
            {'name': 'Total played', 'value': f'{stats["played_games"]} / {stats["played_seconds"]} sec'},
            {'name': 'Win rate', 'value': f'{stats["w_wins"] / stats["played_games"] * 100:.0f}%'},
            {'name': 'Average game time', 'value': f'{stats["w_win_time"] / stats["w_wins"]:.1f} sec'},
            {'name': 'Best time',
             'value': f'{stats["t_time"]} sec ({stats["t_width"]}x{stats["t_height"]}, {stats["t_mines_amount"]})'},
            {'name': 'Best score',
             'value': f'{stats["s_score"]} ({stats["s_width"]}x{stats["s_height"]}, {stats["s_mines_amount"]})'}
        ]
