from interstellar_trash_hunter.core.controller import Controller


class Entry(Controller):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hp = 0

    def init(self):
        # TODO: Implement the initialization of the game
        pass
