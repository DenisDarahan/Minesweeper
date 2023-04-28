from asyncpg import Record

from ._base_table import _BaseTable


class User(_BaseTable):
    TABLE_NAME = 'user'
    INIT_TABLE = ('create table if not exists "user" ( '
                  '    id bigint generated always as identity primary key, '
                  '    username varchar(100) not null, '
                  '    password_hash varchar(200) not null, '
                  '    reg_date timestamp default current_timestamp, '
                  '    unique (username) '
                  ')')

    async def create(self, login: str, password_hash: str) -> int:
        async with self.connector() as con:
            return await con.fetchval(
                'insert into "user" (username, password_hash) values ($1, $2) returning id', login, password_hash)

    async def get(self, user_id: int) -> Record:
        async with self.connector() as con:
            return await con.fetchrow('select id, username, password_hash, reg_date from "user" where id = $1', user_id)

    async def get_by_username(self, username: str) -> Record:
        async with self.connector() as con:
            return await con.fetchrow(
                'select id, username, password_hash, reg_date from "user" where username = $1', username)

    async def get_info(self, user_id: int) -> Record:
        async with self.connector() as con:
            return await con.fetchrow(
                'select u.id, u.username, u.reg_date, r.games_count, r.max_score, r.play_time '
                'from "user" u '
                '    left join ( '
                '        select user_id, count(*) games_count, max(game_score) max_score, sum(game_time) play_time '
                '        from rate where user_id = $1 '
                '        group by user_id '
                '    ) r on u.id = r.user_id '
                'where u.id = $1',
                user_id
            )
