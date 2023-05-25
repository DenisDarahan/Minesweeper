import time
import traceback

from kivy.app import App
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.utils import platform
from kivy.context import register_context
from kivy.core.window import Window

from game.gui.settings import settings


Window.clearcolor = (1, 1, 1, 1)
VIEW_BUILD: str

if platform in {'android', 'ios'}:
    VIEW_BUILD = 'mobile'
    # Builder.load_string('#:include game/gui/minesweeper/mobile/mobile.kv')
    # Window.fullscreen = True
    # from gui.minesweeper.android_ios import RootWindow
else:
    VIEW_BUILD = 'desktop'
    # Builder.load_string(f'#:include game/gui/minesweeper/desktop/desktop.kv')
    from gui.minesweeper.desktop import RootWindow

    from kivy.config import Config
    Config.set('graphics', 'resizable', False)
    Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class MinesweeperApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        register_context('field', dict, {'width': 10, 'height': 10, 'mines_amount': 10})

    def build(self):
        Logger.info(f'{self.__class__.__name__}: Building the app')
        Builder.load_string(f'#:include game/gui/minesweeper/{VIEW_BUILD}/{VIEW_BUILD}.kv')
        return RootWindow()

    def run(self):
        try:
            super().run()

        except Exception as e:
            Logger.exception(f'{e.__class__.__name__}: Raised exception {e}')

            with open(settings.CRASH_LOG_DIR_PATH / f'CRASH-{int(time.time())}.txt', 'w') as crash_log:
                crash_log.write(f'{traceback.format_exc()}')
