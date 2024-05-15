import pygame

from interstellar_trash_hunter.view.ui.view import View
from interstellar_trash_hunter.view.ui.label import Label
from interstellar_trash_hunter.view.ui.container import Container

from interstellar_trash_hunter.event.handler import HandlerArguments, Handler

# 按钮类


class Button(Container):

    def __init__(self,
                 text: str = None,
                 font="simHei",
                 font_size=None,
                 width=200,
                 height=40,
                 **kwargs):
        super().__init__(width=width, height=height, **kwargs)
        self.label = Label(text, font=font, font_size=font_size)
        self.add_child(self.label)
        self._has_mouse_down = False
        self._click = None

    @property
    def click(self):
        if not self._click:
            self._click = Handler()
        return self._click

    def trigger(self, event, pos):
        super().trigger(event, pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self._has_mouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if self._has_mouse_down and self._click:
                self.click.trigger(HandlerArguments(target=self, params=pos))
            self._has_mouse_down = False


# # 初始化Pygame
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# clock = pygame.time.Clock()
# font = pygame.font.Font(None, 32)

# # 创建按钮
# button = Button(200, 200, 100, 50, (255, 0, 0), "Click Me", (255, 255, 255),
#                 font)

# # 游戏循环
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             running = False
#         button.handle_event(event)

#     screen.fill((255, 255, 255))
#     button.draw(screen)
#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()
