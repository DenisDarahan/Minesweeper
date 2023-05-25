from pathlib import Path


class Settings:
    DB_PATH: Path = Path('./game/gui/minesweeper.db')
    CRASH_LOG_DIR_PATH: Path = Path('./game/gui/crashlog/')

    SERVER_API: str = 'http://127.0.0.1:8000'

    def __init__(self):
        self.DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        self.DB_PATH.touch(exist_ok=True)
        self.CRASH_LOG_DIR_PATH.mkdir(parents=True, exist_ok=True)


settings = Settings()
