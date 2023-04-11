from ..connector import Connector


class _BaseTable:
    TABLE_NAME: str
    INIT_TABLE: str

    connector: Connector

    def __init__(self, connector: Connector):
        self.connector = connector

    def _init_table(self):
        con, cur = self.connector.create_sync()
        cur.execute(self.INIT_TABLE)
        con.commit()
        cur.close()
        con.close()
