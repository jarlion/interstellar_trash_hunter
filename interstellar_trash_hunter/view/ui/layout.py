from abc import abstractmethod
import math
from typing import Any, Callable, List, Tuple


class Layout:
    """
    布局
    默认平均分布局
    """

    def __init__(self, rows: int = 1, cols: int = 1) -> None:
        self._rows = rows
        self._cols = cols

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    @abstractmethod
    def calc_cell_size(self, rect, count: int) -> Tuple[float, float]:
        """
        计算单元格大小
        """
        pass

    def split(
        self,
        rect,
        create_rect: Callable[[float, float, float, float], Any],
        count: int = 1,
    ) -> List[List[Any]]:
        """
        切分矩形
        """
        # 确保矩形的尺寸可以被行数和列数整除，否则需要调整逻辑以处理非均匀划分的情况
        cell_width, cell_height = self.calc_cell_size(rect, count)

        # 初始化二维列表来存储Rect对象
        grid_layout = [[None for _ in range(self._cols)]
                       for _ in range(self._rows)]

        for row in range(self._rows):
            for col in range(self._cols):
                # 计算每个子矩形的坐标
                x = rect.x + col * cell_width
                y = rect.y + row * cell_height

                # 创建并添加子矩形到grid_layout中
                grid_layout[row][col] = create_rect(x, y, cell_width,
                                                    cell_height)

        return grid_layout


class DynamicLayout(Layout):
    """
    动态布局
    先计算实际尺寸，再分配剩余空间
    """

    def __init__(self, rows: int = 1, cols: int = 1) -> None:
        super().__init__(rows, cols)


class Horizontal(Layout):
    """
    水平布局
    """

    def __init__(self, cols: int = 1) -> None:
        super().__init__(None, cols)

    def calc_cell_size(self, rect, count: int) -> Tuple[float, float]:
        """
        优先计算行数
        """
        self._rows = math.ceil(count / self._cols)
        cell_width = rect.width // self._cols
        cell_height = rect.height // self._rows
        return cell_width, cell_height


class Vertical(Layout):
    """
    垂直布局
    """

    def __init__(self, rows: int = 1) -> None:
        super().__init__(rows, None)

    def calc_cell_size(self, rect, count: int) -> Tuple[float, float]:
        """
        优先计算列数
        """
        self._cols = math.ceil(count / self._rows)
        cell_width = rect.width // self._cols
        cell_height = rect.height // self._rows
        return cell_width, cell_height


class Staggered(Layout):
    pass
