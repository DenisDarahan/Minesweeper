import asyncpg

from ._base_connector import _BaseConnector


class Async(_BaseConnector):
    con: asyncpg.Connection

    async def __aenter__(self) -> asyncpg.Connection:
        self.con = await asyncpg.connect(
            user=self._user, password=self._password, database=self._database, host=self._host)
        return self.con

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.con.close()

    async def get(self):
        async with self as con:
            yield con
