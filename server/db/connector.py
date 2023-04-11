import asyncpg
import psycopg2
from psycopg2 import extensions


class Connector:
    __user: str
    __password: str
    __database: str
    __host: str

    def __init__(self, user: str, database: str, password: str = '', host: str = '127.0.0.1'):
        self.__user = user
        self.__password = password
        self.__database = database
        self.__host = host

    async def create(self) -> asyncpg.Connection:
        con = await asyncpg.connect(
            user=self.__user, password=self.__password, database=self.__database, host=self.__host)
        return con

    def create_sync(self) -> tuple[extensions.connection, extensions.cursor]:
        con = psycopg2.connect(
            user=self.__user, password=self.__password, database=self.__database, host=self.__host)
        cur = con.cursor()
        return con, cur
