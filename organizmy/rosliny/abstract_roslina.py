from organizmy import Organizm
import random


class AbstractRoslina(Organizm):
    __inicjatywa_rosliny = 0
    __szansa_rozsiana = 0.1

    def __init__(self, swiat, tile, pozycja, kolor, nazwa, tekstura, sila, wiek=1):
        super().__init__(swiat, tile, pozycja, kolor, nazwa, tekstura, sila, self.__inicjatywa_rosliny, wiek)

    def akcja(self):
        if not self.czy_zywy():
            return
        self._sprobuj_sie_rozsiac()

    def kolizja(self, organizm):
        self.umrzyj(organizm)
        return True

    def _sprobuj_sie_rozsiac(self):
        szansa = random.random()
        if not szansa <= self.__szansa_rozsiana:
            return False
        tile = self.get_tile().get_losowy_pusty_sasiad()
        if tile is None:
            return False

        offspring = self.stworz_kopie()
        offspring.set_tile(tile)
        offspring.set_pozycja(tile.get_pozycja())
        tile.set_organizm(offspring)
        self._swiat.dodaj_organizm(offspring)
        print(str(self) + " zasial " + str(offspring))
        return True
