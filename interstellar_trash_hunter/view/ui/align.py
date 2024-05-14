class Align:

    def __init__(self, offset_x: float = 0, offset_y: float = 0):
        self.offset_x = offset_x
        self.offset_y = offset_y

    def get_position(self, space, target):
        x = (space.width - target.width) / 2 + space.x + self.offset_x
        y = (space.height - target.height) / 2 + space.y + self.offset_y
        return x, y


class TopLeft(Align):

    def get_position(self, space, target):
        x = space.x + self.offset.x
        y = space.y + self.offset.y
        return x, y


class Top(Align):

    def get_position(self, space, target):
        x = (space.width - target.width) / 2 + space.x + self.offset_x
        y = space.y + self.offset.y
        return x, y


class TopRight(Align):

    def get_position(self, space, target):
        x = (space.width - target.width) + space.x + self.offset_x
        y = space.y + self.offset.y
        return x, y


class MidLeft(Align):

    def get_position(self, space, target):
        x = space.x + self.offset_x
        y = (space.height - target.height) / 2 + space.y + self.offset_y
        return x, y


class Center(Align):

    def get_position(self, space, target):
        x = (space.width - target.width) / 2 + space.x + self.offset_x
        y = (space.height - target.height) / 2 + space.y + self.offset_y
        return x, y


class MidRight(Align):

    def get_position(self, space, target):
        x = (space.width - target.width) + space.x + self.offset_x
        y = (space.height - target.height) / 2 + space.y + self.offset_y
        return x, y


class BottomLeft(Align):

    def get_position(self, space, target):
        x = space.x + self.offset_x
        y = (space.height - target.height) + space.y + self.offset_y
        return x, y


class Bottom(Align):

    def get_position(self, space, target):
        x = (space.width - target.width) / 2 + space.x + self.offset_x
        y = (space.height - target.height) + space.y + self.offset_y
        return x, y


class BottomRight(Align):

    def get_position(self, space, target):
        x = (space.width - target.width) + space.x + self.offset_x
        y = (space.height - target.height) + space.y + self.offset_y
        return x, y
