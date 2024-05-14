import pygame
from interstellar_trash_hunter.view.ui.layout import Horizontal
from interstellar_trash_hunter.view.ui.view import View


class Container(View):
    """
    容器视图，可以包含其他视图
    """

    def __init__(self, layout=Horizontal(), interactive=True, **kwargs):
        super().__init__(interactive=True, **kwargs)
        self.layout = layout
        self._children = []

    def children(self):
        return self._children

    def add_child(self, child: View) -> "Container":
        self._children.append(child)
        self._dirty = True
        return self

    def remove_child(self,
                     child: View,
                     destroy: bool = True,
                     delete: bool = True) -> "Container":
        if delete:
            self._children.remove(child)
        if destroy:
            child.destroy()
        self._dirty = True
        return self

    def remove_all_children(self,
                            child: View,
                            destroy: bool = True) -> "Container":
        for child in child.children:
            self.remove_child(child, destroy, delete=False)
        self._children.clear()
        return self

    def find_child(self, name: str) -> View:
        for child in self._children:
            if child.name == name:
                return child
        return None

    def _render_self(self, screen, rect):
        # TODO 需要判断是否因为子组件导致父组件需要渲染
        render_rect = super()._render_self(screen, rect)
        if self.layout:
            # 如果有布局，则需要计算出子组件的位置
            rects = self.layout.split(
                render_rect, lambda x, y, w, h: pygame.Rect(x, y, w, h),
                len(self._children))
            for row in range(len(rects)):
                cols = len(rects[row])
                for col in range(cols):
                    index = row * cols + col
                    if index >= len(self._children):
                        break
                    child = self._children[index]
                    child.render(screen, rects[row][col])
        else:
            for child in self._children:
                child.render(screen, render_rect)

    def capture(self, event, pos):
        if self.collision_detection(pos):
            for child in self._children[::-1]:
                # 如果已经有子组件触发了则停止捕获事件
                if child.capture(event, pos):
                    break
        # 父组件冒泡
        return super().capture(event, pos)

    def destroy(self):
        super().destroy()

        for child in self._children:
            child.destroy()
