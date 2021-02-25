from .tile import Tile
from Point import Point
from .kierunek import Kierunek


class Mapa:
    def __init__(self, szerokosc, wysokosc):
        self._szerokosc = szerokosc
        self._wysokosc = wysokosc
        self._mapa = []
        self._init()

    def _init(self):
        self._mapa = [[None for x in range(self._wysokosc)] for y in range(self._szerokosc)]
        for x in range(0, self._szerokosc):
            for y in range(0, self._wysokosc):
                self._mapa[x][y] = Tile(Point(x, y), None)
        self._init_sasiedzi()

    def _init_sasiedzi(self):
        for x in range(0, self._szerokosc):
            for y in range(0, self._wysokosc):
                sasiedzi = [None, None, None, None]
                kierunki = Kierunek.NORTH
                while True:
                    sasiedzi[kierunki.to_int()] = self.get_tile(x + kierunki.get_x(), y + kierunki.get_y())
                    kierunki = kierunki.get_nastepny_kierunek()
                    if kierunki is None:
                        break
                self._mapa[x][y].set_sasiedzi(sasiedzi)

    def get_szerokosc(self):
        return self._szerokosc

    def get_wysokosc(self):
        return self._wysokosc

    def get_tile(self, x, y):
        if x < 0 or y < 0 or x >= self._szerokosc or y >= self._wysokosc:
            return None
        return self._mapa[x][y]

    def set_rozmiar(self, szerokosc, wysokosc):
        self._szerokosc = szerokosc
        self._wysokosc = wysokosc
        self._init()
