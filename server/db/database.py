from server.settings import settings
from .connector import Connector
from .tables import *


class Database:
    connector: Connector

    user: User
    rate: Rate

    def __init__(self):
        self.connector = Connector(
            user=settings.db_user,
            password=settings.db_password,
            database=settings.db_name,
            host=settings.db_host
        )

        self.user = User(self.connector)
        self.rate = Rate(self.connector)
