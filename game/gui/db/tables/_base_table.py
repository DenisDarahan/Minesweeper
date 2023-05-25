from ..connector import Connector


class _BaseTable:
    TABLE_NAME: str
    INIT_TABLE: str

    connector: Connector

    def __init__(self, connector: Connector):
        self.connector = connector
        self._init_table()

    def _init_table(self):
        with self.connector() as (con, cur):
            cur.execute(self.INIT_TABLE)
            con.commit()
