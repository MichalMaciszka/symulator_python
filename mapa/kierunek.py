from enum import Enum


class Kierunek(Enum):
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)
    NONE = (0, 0)

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def to_int(self):
        if self._x == 0 and self._y == -1:
            return 0
        elif self._x == 1 and self._y == 0:
            return 1
        elif self._x == 0 and self._y == 1:
            return 2
        elif self._x == -1 and self._y == 0:
            return 3
        else:
            return -1

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_nastepny_kierunek(self):
        choices = {0: self.EAST, 1: self.SOUTH, 2: self.WEST}
        return choices.get(self.to_int(), None)

    def reset(self):
        self._x = 0
        self._y = -1
