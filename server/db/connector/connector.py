from .async_connector import Async
from .sync_connector import Sync


class Connector:
    __user: str
    __password: str
    __database: str
    __host: str

    def __init__(self, *, user: str, password: str = '', database: str, host: str = '127.0.0.1'):
        self.__user = user
        self.__password = password
        self.__database = database
        self.__host = host

    def __call__(self) -> Async:
        return Async(self.__user, self.__password, self.__database, self.__host)

    def sync(self) -> Sync:
        return Sync(self.__user, self.__password, self.__database, self.__host)
