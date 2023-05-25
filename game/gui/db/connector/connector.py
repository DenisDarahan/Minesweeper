from pathlib import Path

from .connection_handler import ConnectionHandler


class Connector:
    db_path: Path

    def __init__(self, db_path: Path):
        self.db_path = db_path

    def __call__(self, *, use_dict_factory: bool = False) -> ConnectionHandler:
        return ConnectionHandler(self.db_path, use_dict_factory)
