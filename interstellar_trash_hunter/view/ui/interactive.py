import pygame
from interstellar_trash_hunter.event.handler import Handler, HandlerArguments
from interstellar_trash_hunter.view.ui.view import View


class Interactive(View):
    """
    交互对象
    """

    def __init__(self, interactive: bool, **kwargs):
        super().__init__(**kwargs)
        self.interactive = interactive

        self._init_event_dict()

    def _init_event_dict(self):
        self._mouse_down = None
        self._mouse_up = None
        self._mouse_move = None
        self._event_dict = {
            pygame.MOUSEBUTTONDOWN: lambda: self._mouse_down,
            pygame.MOUSEBUTTONUP: lambda: self._mouse_up,
            pygame.MOUSEMOTION: lambda: self._mouse_move
        }

    @property
    def mouse_down(self):
        if not self._mouse_down:
            self._mouse_down = Handler()
        return self._mouse_down

    @property
    def mouse_up(self):
        if not self._mouse_up:
            self._mouse_up = Handler()
        return self._mouse_up

    @property
    def mouse_move(self):
        if not self._mouse_move:
            self._mouse_move = Handler()
        return self._mouse_move

    def collision_detection(self, pos) -> bool:
        return self._render_rect.collidepoint(*pos)

    def capture(self, event, pos) -> bool:
        if self.visible and self.interactive:
            if self.collision_detection(pos):
                self.trigger(event, pos)
                return True
        return False

    def trigger(self, event, pos):
        if event.type in self._event_dict:
            handler = self._event_dict[event.type]()
            if isinstance(handler, Handler):
                handler.trigger(HandlerArguments(target=self, params=pos))
