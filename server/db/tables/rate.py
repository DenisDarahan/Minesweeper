from typing import Any

from asyncpg import Connection, Record

from ._base_table import _BaseTable


class Rate(_BaseTable):
    # game_score: int = int(game_field.width * game_field.height * mines_count * 1000 / game_time)
    #                                                                            ^ 3 decimals accuracy
    _PAGE_SIZE: int = 5

    TABLE_NAME = 'rate'
    INIT_TABLE = ('create table if not exists rate ( '
                  '    id bigint generated always as identity primary key, '
                  '    user_id bigint not null, '
                  '    game_score int not null, '
                  '    game_time int not null, '
                  '    create_date date default current_date, '
                  '    foreign key (user_id) references "user"(id) on delete cascade on update cascade '
                  ')')

    _ORDERED_RATE: str = (
        'select row_number() over (order by game_score desc) line_number, id, user_id, '
        '    game_score, game_time '
        'from rate '
        'order by game_score desc'
    )

    async def top(self, limit: int = 10, offset: int = 0) -> dict[str, Any]:
        async with self.connector() as con:
            async with con.transaction():
                count = await con.fetchval('select count(*) from rate')
                top = await con.fetch(
                    'select row_number() over (order by r.game_score desc) line_number, '
                    '    u.username, r.game_score, r.game_time '
                    'from rate r '
                    '    join "user" u on u.id = r.user_id '
                    'order by r.game_score desc '
                    'limit $1 offset $2',
                    limit, offset
                )
                return {'count': count, 'top': top}

    @classmethod
    async def poor_create(cls, con: Connection, user_id: int, game_score: int, game_time: int) -> int:
        return await con.fetchval(
            'insert into rate (user_id, game_score, game_time) values ($1, $2, $3) returning id',
            user_id, game_score, game_time
        )

    @classmethod
    async def poor_rate(cls, con: Connection, rate_id: int, page_size: int = _PAGE_SIZE) -> list[Record]:
        return await con.fetch(
            'with ordered_rate as ( '
            '    select row_number() over (order by game_score desc) line_number, id, user_id, game_score, game_time '
            '    from rate order by game_score desc '
            ') '
            'select _or.line_number, u.username, _or.game_score, _or.game_time '
            'from (select line_number from ordered_rate where id = $1) target, ordered_rate _or '
            '    join "user" u on _or.user_id = u.id '
            'where _or.line_number >= target.line_number - $2 and _or.line_number <= target.line_number + $2',
            rate_id, page_size
        )

    async def create(self, user_id: int, game_score: int, game_time: int) -> int:
        async with self.connector() as con:
            return await self.poor_create(con, user_id, game_score, game_time)

    async def me(self, user_id: int, page_size: int = _PAGE_SIZE) -> list[Record]:
        async with self.connector() as con:
            return await con.fetch(
                'with ordered_rate as ( '
                '    select row_number() over (order by game_score desc) line_number, id, user_id, '
                '        game_score, game_time '
                '    from rate order by game_score desc '
                ') '
                'select _or.line_number, u.username, _or.game_score, _or.game_time '
                'from '
                '    (select line_number from ordered_rate '
                '     where user_id = $1 order by game_score desc limit 1) target, '
                '    ordered_rate _or '
                '        join "user" u on _or.user_id = u.id '
                'where _or.line_number >= target.line_number - $2 and _or.line_number <= target.line_number + $2',
                user_id, page_size
            )
