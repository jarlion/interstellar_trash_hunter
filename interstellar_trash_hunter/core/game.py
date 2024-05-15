from interstellar_trash_hunter.event.handler import HandlerArguments
from interstellar_trash_hunter.view.page.level import Level
from interstellar_trash_hunter.view.ui.container import Container
from interstellar_trash_hunter.view.page.home import Home

from interstellar_trash_hunter.setting.base import SCREEN_WIDTH, SCREEN_HEIGHT


class Game:

    def __init__(self):
        self.view = Container(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self._ctx = {}
        self.screens = {
            "home": lambda: Home,
            "level": lambda: Level,
            "load": lambda: Level(),
            "over": None,
            "about": None
        }
        screen = Home()

        screen.change.add(self.on_screen_change)
        self.view.add_child(screen)

    def on_screen_change(self, params: HandlerArguments):
        screen_name = params.params
        self.screens[screen_name](self._ctx)

    def change_screen(self, name: str):
        # 删除当前的界面
        self.view.remove_all_children()
        # 创建新的界面
        screen = Home(name)
        screen.change.add(self.on_screen_change)
        self.view.add_child(screen)

    def run(self):
        self.view.run()
