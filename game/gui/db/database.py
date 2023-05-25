from pathlib import Path

from .connector import Connector
from .tables import *


class Database:
    rate: Rate

    def __init__(self, db_path: [str, Path]):
        if isinstance(db_path, str):
            db_path = Path(db_path)
        db_path.parent.mkdir(parents=True, exist_ok=True)
        db_path.touch(exist_ok=True)

        connector = Connector(db_path)

        self.rate = Rate(connector)
