import pygame

from interstellar_trash_hunter.view.ui.view import View
from interstellar_trash_hunter.view.ui.align import Align


class Label(View):
    """
    A label is a view that displays text.
    """

    def __init__(self,
                 text: str = None,
                 font='simHei',
                 font_size=None,
                 color=(255, 255, 255),
                 align=Align(),
                 **kwargs):
        super().__init__(color=color, align=align, **kwargs)
        self.text = text
        self.font = font
        self.font_size = font_size
        self.text_rect = None

    def _render_self(self, screen, rect):

        # 使用系统字体
        font = pygame.font.SysFont(self.font, self.font_size)
        # 使用render()方法，但不传入True作为最后一个参数（表示不需要立即进行抗锯齿处理）
        # 第二个参数可以是文本颜色，第三个参数是一个可选的背景颜色（若不需背景色则设为None）
        text_surface = font.render(self.text,
                                   True,
                                   color=self.color,
                                   bgcolor=self.bgcolor)
        text_rect = text_surface.get_rect()
        self.width = text_rect.width
        self.height = text_rect.height

        # 计算文本的显示位置
        x, y = self.align.get_position(rect, text_rect)
        self.x = x - rect.x
        self.y = y - rect.y
        text_rect.topleft = (x, y)
        # 将文本渲染到屏幕上
        screen.blit(text_surface, text_rect)
