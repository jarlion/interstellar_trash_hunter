from abc import abstractmethod
import pygame

from interstellar_trash_hunter.event.handler import Handler, HandlerArguments
from interstellar_trash_hunter.view.ui.align import Align


class Border:

    def __init__(self, color=None, thickness=1):
        self.color = color
        self.thickness = thickness


class View:

    def __init__(self,
                 x: float = 0,
                 y: float = 0,
                 width: float = 0,
                 height: float = 0,
                 color=None,
                 bgcolor=None,
                 border=None,
                 interactive=False,
                 align: Align = None,
                 name: str = None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.bgcolor = bgcolor
        self.visible = True
        self.border = border
        self.interactive = interactive
        self.align = align
        self._dirty = True
        self._change = None
        self._init_event_dict()
        self._render_rect = None
        if name:
            self._name = name
        else:
            self._name = f"{self.__class__.__name__}_{id(self)}"

    def _init_event_dict(self):
        self._mouse_pressed = None
        self._mouse_released = None
        self._mouse_moved = None
        self._event_dict = {
            pygame.MOUSEBUTTONDOWN: lambda: self._mouse_pressed,
            pygame.MOUSEBUTTONUP: lambda: self._mouse_released,
            pygame.MOUSEMOTION: lambda: self._mouse_moved
        }

    @property
    def mouse_pressed(self):
        if not self._mouse_pressed:
            self._mouse_pressed = Handler()
        return self._mouse_pressed

    @property
    def mouse_released(self):
        if not self._mouse_released:
            self._mouse_released = Handler()
        return self._mouse_released

    @property
    def mouse_moved(self):
        if not self._mouse_moved:
            self._mouse_moved = Handler()
        return self._mouse_moved

    @property
    def changed(self):
        if not self._change:
            self._change = Handler()

    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, value):
        self.rect.x = value
        self._dirty = True

    @property
    def y(self):
        return self.rect.y

    @y.setter
    def y(self, value):
        self.rect.y = value
        self._dirty = True

    @property
    def width(self):
        return self.rect.width

    @width.setter
    def width(self, value):
        self.rect.width = value
        self._dirty = True

    @property
    def height(self):
        return self.rect.height

    @height.setter
    def height(self, value):
        self.rect.height = value
        self._dirty = True

    @property
    def dirty(self):
        return self._dirty

    @dirty.setter
    def dirty(self, value):
        change = self._dirty != value
        self._dirty = value
        if change:
            if self._change:
                self._change.trigger(HandlerArguments(target=self))

    @property
    def name(self):
        return self._name

    def render(self, screen, rect):
        if self._dirty:
            self._render_self(screen, rect)
            self._dirty = False

    def _render_self(self, screen, rect):
        return self._render_background(screen, rect)

    def _render_background(self, screen, rect):
        """
        渲染背景

        Args:
            screen (_type_): 渲染的场景
            rect (_type_): 父组件渲染区域

        Returns:
            _type_: 当前组件渲染区域
        """
        self._render_rect = self.get_render_rect(rect)
        # 先绘制边框，再填充内部
        thickness = 0
        if self.border:
            thickness = self.border.thickness
            pygame.draw.rect(
                screen, self.border.color,
                (self._render_rect.topleft, self._render_rect.size),
                self.border.thickness)  # 边框
        if self.bgcolor:
            # 计算除去边框的矩形
            inner_rect = pygame.Rect(self._render_rect.x + thickness,
                                     self._render_rect.y + thickness,
                                     self._render_rect.width - 2 * thickness,
                                     self._render_rect.height - 2 * thickness)
            pygame.draw.rect(screen, self.bgcolor, inner_rect)
        return self._render_rect

    def get_render_rect(self, space: pygame.Rect):
        if self.align:
            x, y = self.align.get_position(space, self.rect)
        else:
            x = space.x + self.rect.x
            y = space.y + self.rect.y
        w = min(self.rect.width, space.width)
        h = min(self.rect.height, space.height)
        return pygame.Rect(x, y, w, h)

    def on_enter_frame(self, screen, rect):
        if self.visible:
            self.render(screen, rect)
            self._on_enter_frame()

    def _on_enter_frame(self):
        pass

    def destroy(self):
        if self._change:
            self._change.removeAll()

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
            print(event.type, self._event_dict[event.type], handler,
                  self._mouse_released, self.name)
            if isinstance(handler, Handler):
                handler.trigger(HandlerArguments(target=self, params=pos))
