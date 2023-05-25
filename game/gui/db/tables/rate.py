from typing import Optional

from ..connector import ErrorHandler
from ._base_table import _BaseTable


class Rate(_BaseTable):
    TABLE_NAME = 'rate'
    INIT_TABLE = (
        'create table if not exists rate ( '
        '    id integer primary key, '
        '    create_date timestamp default current_timestamp, '
        '    win boolean not null, '
        '    width integer not null, '
        '    height integer not null, '
        '    mines_amount integer not null, '
        '    time integer not null, '
        '    score integer '
        ');'
    )

    def create(self, win: bool, width: int, height: int, mines_amount: int, time: int, score: Optional[int] = None):
        with self.connector() as (con, cur):
            cur.execute('insert into rate (win, width, height, mines_amount, time, score) values (?, ?, ?, ?, ?, ?)',
                        (win, width, height, mines_amount, time, score))
            con.commit()

    @ErrorHandler.filter_dict
    def statistics(self) -> dict:
        with self.connector(use_dict_factory=True) as (con, cur):
            cur.execute(
                'select count(r.id) played_games, coalesce(sum(r.time), 0) played_seconds, '
                '    t.create_date t_create_date, t.width t_width, t.height t_height, t.mines_amount t_mines_amount, '
                '    t.time t_time, '
                '    s.create_date s_create_date, s.width s_width, s.height s_height, s.mines_amount s_mines_amount, '
                '    s.score s_score, '
                '    w.win_time w_win_time, w.wins w_wins '
                'from rate r, '
                '    (select create_date, width, height, mines_amount, time '
                '     from rate where win = 1 order by time limit 1) as t, '
                '    (select create_date, width, height, mines_amount, score '
                '     from rate where win = 1 order by score desc limit 1) as s, '
                '    (select sum(time) win_time, sum(win) wins from rate where win = 1) as w'
            )
            return cur.fetchone()
