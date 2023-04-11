from ._base_table import _BaseTable


class Gamer(_BaseTable):
    TABLE_NAME = 'gamer'
    INIT_TABLE = ('create table if not exists gamer ( '
                  '    id bigserial not null primary key, '
                  '    login varchar(100) not null, '
                  '    reg_date timestamp default current_timestamp, '
                  '    unique (login) '
                  ')')
