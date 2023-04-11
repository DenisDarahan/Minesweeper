from .connector import Connector
from .tables import *


class Database:
    gamer: Gamer
    rate: Rate

    def __init__(self):
        connector = Connector(**MINESWEEPER_BD)

        self.gamer = Gamer(connector)
        self.rate = Rate(connector)
