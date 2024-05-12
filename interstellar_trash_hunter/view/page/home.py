# 游戏开始页面
# 第一行是游戏标题：星际垃圾猎手
# 第二行是游戏版本号：v0.0.1
# 第三行是游戏作者：Jarlion
# 第四行是游戏 【开始】按钮：开始游戏
# 第五行是游戏 输入框：提示请输入游戏密码【帮助】按钮：退出游戏
# 第六行是游戏 【退出】按钮：退出游戏

from ...event.handler import HandlerArguments
from ...view.ui.label import Label
from ...view.ui.button import Button
from ...setting.base import NAME, SCREEN_WIDTH, SCREEN_HEIGHT, FONT_SIZE
from interstellar_trash_hunter.view.page.screen import Screen


class Home(Screen):

    def __init__(self):
        super().__init__()
        # UI元素位置
        TITLE_POS = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        VERSION_POS = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + FONT_SIZE * 1.5)
        AUTHOR_POS = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + FONT_SIZE * 3)
        START_BTN_POS = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        PASSWORD_INPUT_POS = (SCREEN_WIDTH // 2 - 100,
                              SCREEN_HEIGHT // 2 + FONT_SIZE * 1.5)
        HELP_BTN_POS = (PASSWORD_INPUT_POS[0] + 200, PASSWORD_INPUT_POS[1])
        EXIT_BTN_POS = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + FONT_SIZE * 3)

        title = Label(text=NAME,
                      x=TITLE_POS[0],
                      y=TITLE_POS[1],
                      font_size=FONT_SIZE * 2)
        self.add_child(title)
        start_btn = Button(text=NAME,
                           x=START_BTN_POS[0],
                           y=START_BTN_POS[1],
                           font_size=FONT_SIZE * 2)
        start_btn.click.add(self.on_start_game)
        self.add_child(start_btn)
        # title = Label(text=NAME, pos=TITLE_POS, font_size=FONT_SIZE * 2)
        # self.add_child(title)
        # title = Label(text=NAME, pos=TITLE_POS, font_size=FONT_SIZE * 2)
        # self.add_child(title)
        # title = Label(text=NAME, pos=TITLE_POS, font_size=FONT_SIZE * 2)
        # self.add_child(title)

    def on_start_game(self):
        self.change.trigger(HandlerArguments(params="level", target=self))