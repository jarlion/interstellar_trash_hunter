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

        self._click = None
        self._mouse_up = None
        self._mouse_down = None
        self._is_mouse_down = False

    @property
    def click(self):
        if not self._click:
            self._click = Handler()
        return self._click

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._trigger_event(event.pos, self._mouse_down):
                self._is_mouse_down = True
            return
        if event.type == pygame.MOUSEBUTTONUP:
            if self._trigger_event(event.pos, self._mouse_up):
                if self._is_mouse_down:
                    self._trigger_event(event.pos, self._click)
                self._is_mouse_down = False
            return

    def _trigger_event(self, position, handler: Handler) -> bool:
        """
        触发事件
        Args
            position: 事件位置
            handler: 事件处理器
        Return: 
            bool: 是否触发区域
        """
        if self.rect.collidepoint(position):
            print("Button event trigger")
            if handler:
                handler.trigger(HandlerArguments(target=self))
            return True
        return False


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
