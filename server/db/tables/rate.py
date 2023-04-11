from ._base_table import _BaseTable


class Rate(_BaseTable):
    TABLE_NAME = 'rate'
    INIT_TABLE = ('create table if not exists rate ( '
                  '    id bigserial not null primary key, '
                  '    gamer_id bigint not null, '
                  '    game_score decimal(10,3) not null, '
                  '    game_time int not null, '
                  '    create_date date default current_date, '
                  '    foreign key (gamer_id) references gamer(id) on delete cascade on update cascade '
                  ')')
