# 游戏开始页面
# 第一行是游戏标题：星际垃圾猎手
# 第二行是游戏版本号：v0.0.1
# 第三行是游戏作者：Jarlion
# 第四行是游戏 【开始】按钮：开始游戏
# 第五行是游戏 输入框：提示请输入游戏密码【帮助】按钮：退出游戏
# 第六行是游戏 【退出】按钮：退出游戏

from interstellar_trash_hunter.event.handler import Handler
from interstellar_trash_hunter.view.ui.label import Label
from interstellar_trash_hunter.view.ui.button import Button
from interstellar_trash_hunter.view.ui.container import Container


class Level(Container):

    def __init__(self, level: str):
        super().__init__()
        self.change = Handler()
        self.level = level
