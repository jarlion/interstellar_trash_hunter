from interstellar_trash_hunter.view.ui.view import View


class Container(View):
    """
    容器视图，可以包含其他视图
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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
        for child in self._children:
            child.render(screen, render_rect)

    def destroy(self):
        super().destroy()

        for child in self._children:
            child.destroy()
