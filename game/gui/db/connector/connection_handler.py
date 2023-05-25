from pathlib import Path
from sqlite3 import Connection, Cursor, Row
from typing import Callable, Union


class ConnectionHandler:
    db_path: Path
    row_factory: Union[None, Callable]

    con: Connection
    cur: Cursor

    def __init__(self, db_path: Path, use_dict_factory: bool):
        self.db_path = db_path
        self.row_factory = self.dict_factory if use_dict_factory else None

    @staticmethod
    def dict_factory(cursor: Cursor, row: Row) -> dict:
        return {column[0]: row[index] for index, column in enumerate(cursor.description)}

    def __enter__(self) -> tuple[Connection, Cursor]:
        self.con = Connection(self.db_path)
        self.con.row_factory = self.row_factory
        self.cur = self.con.cursor()
        return self.con, self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.con.close()
