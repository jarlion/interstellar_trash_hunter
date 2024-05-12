from interstellar_trash_hunter.core.game import Game
from interstellar_trash_hunter.core.engine import Engine


def main():
    game = Game()
    engine = Engine(root=game.view)
    engine.start()


if __name__ == "__main__":
    main()
