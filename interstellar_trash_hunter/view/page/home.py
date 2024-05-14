# 游戏开始页面
# 第一行是游戏标题：星际垃圾猎手
# 第二行是游戏版本号：v0.0.1
# 第三行是游戏作者：Jarlion
# 第四行是游戏 【开始】按钮：开始游戏
# 第五行是游戏 输入框：提示请输入游戏密码【帮助】按钮：退出游戏
# 第六行是游戏 【退出】按钮：退出游戏

from interstellar_trash_hunter.event.handler import HandlerArguments
from interstellar_trash_hunter.view.ui.align import Center
from interstellar_trash_hunter.view.ui.label import Label
from interstellar_trash_hunter.view.ui.button import Button
from interstellar_trash_hunter.setting.base import NAME, version, SCREEN_WIDTH, SCREEN_HEIGHT, FONT_SIZE, SCREEN_BUTTON_BORDER_COLOR
from interstellar_trash_hunter.view.page.screen import Screen
from interstellar_trash_hunter.view.ui.layout import Horizontal
from interstellar_trash_hunter.view.ui.view import Border


class Home(Screen):

    def __init__(self):
        super().__init__(layout=Horizontal())
        # UI元素位置
        TITLE_POS = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        VERSION_POS = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + FONT_SIZE * 1.5)
        AUTHOR_POS = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + FONT_SIZE * 3)
        START_BTN_POS = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        PASSWORD_INPUT_POS = (SCREEN_WIDTH // 2 - 100,
                              SCREEN_HEIGHT // 2 + FONT_SIZE * 1.5)
        HELP_BTN_POS = (PASSWORD_INPUT_POS[0] + 200, PASSWORD_INPUT_POS[1])
        EXIT_BTN_POS = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + FONT_SIZE * 3)

        title = Label(text=NAME, font_size=FONT_SIZE * 2)
        self.add_child(title)

        ver = Label(text=version, font_size=FONT_SIZE)
        self.add_child(ver)

        start_btn = Button(align=Center(),
                           text="开始游戏",
                           font_size=FONT_SIZE,
                           border=Border(SCREEN_BUTTON_BORDER_COLOR, 1))
        start_btn.click.add(self.on_start_game)
        self.add_child(start_btn)

        load_btn = Button(align=Center(),
                          text="载入游戏",
                          font_size=FONT_SIZE,
                          border=Border(SCREEN_BUTTON_BORDER_COLOR, 1))
        load_btn.click.add(self.on_load_game)
        self.add_child(load_btn)

    def on_start_game(self):
        print("start game")
        self.change.trigger(HandlerArguments(params="level", target=self))

    def on_load_game(self):
        print("load game")
        self.change.trigger(HandlerArguments(params="load", target=self))
