from interstellar_trash_hunter.model.entry import Entry
from interstellar_trash_hunter.model.role import Role


class Player(Role):

    def __init__(self):
        super().__init__()
        self.score = 0
