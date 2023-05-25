from game.gui.settings import settings
from .database import Database


db = Database(settings.DB_PATH)
