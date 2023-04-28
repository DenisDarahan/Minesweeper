import psycopg2
from psycopg2 import extensions

from ._base_connector import _BaseConnector


class Sync(_BaseConnector):
    con: extensions.connection
    cur: extensions.cursor

    def __enter__(self) -> tuple[extensions.connection, extensions.cursor]:
        self.con = psycopg2.connect(user=self._user, password=self._password, database=self._database, host=self._host)
        self.cur = self.con.cursor()
        return self.con, self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.con.close()

    def get(self):
        with self as (con, cur):
            yield con, cur
