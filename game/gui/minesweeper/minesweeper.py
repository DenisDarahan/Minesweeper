from kivy.app import App
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.utils import platform
from kivy.core.window import Window


Window.clearcolor = (1, 1, 1, 1)
VIEW_BUILD: str

if platform in {'android', 'ios'}:
    VIEW_BUILD = 'android_ios'
    # Builder.load_string('#:include game/gui/minesweeper/android_ios/android_ios.kv')
    # Window.fullscreen = True
    # from gui.minesweeper.android_ios import RootWindow
    pass
else:
    VIEW_BUILD = 'desktop'
    Window.size = (800, 600)
    from gui.minesweeper.desktop import RootWindow


class MinesweeperApp(App):

    def build(self):
        Logger.info(f'{self.__class__.__name__}: Building the app')
        Builder.load_string(f'#:include game/gui/minesweeper/{VIEW_BUILD}/{VIEW_BUILD}.kv')
        return RootWindow()

    # def run(self):
    #     try:
    #         super().run()
    #
    #     except Exception as e:
    #         Logger.exception(f'{e.__class__.__name__}: Raised exception {e}')
    #
    #         with open(Config.CRASH_LOG_DIR_PATH / f'CRASH-{int(time.time())}.txt', 'w') as crash_log:
    #             crash_log.write(f'{traceback.format_exc()}')
