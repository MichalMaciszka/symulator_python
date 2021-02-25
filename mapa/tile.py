import random

class Tile:
    def __init__(self, pozycja, organizm):
        self._organizm=organizm
        self._pozycja=pozycja
        self._sasiedzi = [None, None, None, None]

    def empty(self):
        return self._organizm is None

    def set_organizm(self, organizm):
        self._organizm = organizm

    def get_organizm(self):
        return  self._organizm

    def set_pozycja(self, pozycja):
        self._pozycja=pozycja

    def get_pozycja(self):
        return  self._pozycja

    def get_sasiad(self, kierunek):
        return self._sasiedzi[kierunek.to_int()]

    def get_sasiedzi(self):
        return list(self._sasiedzi)

    def get_zajeci_sasiedzi(self):
        list = []
        for i in range(0,4):
            if self._sasiedzi[i] is not None and not self._sasiedzi[i].empty():
                list.append(self._sasiedzi[i])
        return list

    def set_sasiad(self, sasiad, kierunek):
        self._sasiedzi[kierunek] = sasiad

    def set_sasiedzi(self, sasiedzi):
        self._sasiedzi = sasiedzi

    def get_losowy_sasiad(self):
        while True:
            sasiad=random.choice(self._sasiedzi)
            if sasiad is not None:
                return sasiad

    def get_losowy_pusty_sasiad(self):
        if not self._ma_pustego_sasiada():
            return None
        while True:
            tile = random.choice(self._sasiedzi)
            if tile is None:
                continue
            if tile.empty():
                return tile

    def get_losowy_slabszy_sasiad(self, sila):
        if not self._ma_slabszego_sasiada(sila):
            return None
        while True:
            tile = random.choice(self._sasiedzi)
            if tile is None:
                continue
            if tile.empty() or tile.get_organizm().get_sila() < sila:
                return tile

    def _ma_pustego_sasiada(self):
        for tile in self._sasiedzi:
            if tile is not None and tile.empty():
                return True
        return False

    def _ma_slabszego_sasiada(self, sila):
        for tile in self._sasiedzi:
            if tile is not None:
                if tile.empty():
                    return True
                elif tile.get_organizm().get_sila()<sila:
                    return True
        return False

    def __str__(self):
        return "Tile("+str(self._pozycja.x)+", "+str(self._pozycja.y)+", "+str(self._organizm)+")"

    def __repr__(self):
        return self.__str__()
