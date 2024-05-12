import pygame

from interstellar_trash_hunter.view.ui.view import View


class Label(View):
    """
    A label is a view that displays text.
    """

    def __init__(self,
                 text: str = None,
                 font='simHei',
                 font_size=None,
                 width=200,
                 height=40,
                 color=(255, 255, 255),
                 **kwargs):
        super().__init__(color=color, width=width, height=height, **kwargs)
        self.text = text
        self.font = font
        self.font_size = font_size

    def _render_self(self, screen, rect):
        render_rect = self._render_background(screen, rect)

        # 使用系统字体
        font = pygame.font.SysFont(self.font, self.font_size)
        text_surface = font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.center = render_rect.center
        screen.blit(text_surface, text_rect)
