from shooter.game_object.landscape import Landscape
from shooter.config import LANDSCAPE_STONE


class Stone(Landscape):
    """Класс камня"""
    def __init__(self, x, y, image=LANDSCAPE_STONE):
        super().__init__(x, y, image)
