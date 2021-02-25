from ..organizm import Organizm
from abc import ABC, abstractmethod
import random


class AbstractZwierze(Organizm):

    def __init__(self, swiat, tile, pozycja, kolor, nazwa, tekstura, sila, inicjatywa, zasieg_ruchu, szansa_roll, wiek=1):
        super().__init__(swiat, tile, pozycja, kolor, nazwa, tekstura, sila, inicjatywa, wiek)
        self._zasieg_ruchu = zasieg_ruchu
        self._szansa_roll = szansa_roll

    def akcja(self):
        if self.czy_zywy() and self.czy_roll():
            for i in range(self._zasieg_ruchu):
                if not self._travel():
                    break

    def get_target_tile(self):
        return self.get_tile().get_losowy_sasiad()

    def _travel(self):
        target_tile = self.get_target_tile()
        if target_tile is None:
            return False
        if target_tile.empty():
            return self.ruch(target_tile)
        elif self._czy_ten_sam_gatunek(target_tile.get_organizm()):
            self._rozmnoz(target_tile.get_organizm())
            return False
        elif target_tile.get_organizm().kolizja(self):
            self.ruch(target_tile)
            return False
        return False

    @abstractmethod
    def _czy_ten_sam_gatunek(self, organizm):
        pass

    def _rozmnoz(self, partner):
        szansa = random.randint(0, 1)
        tile = None
        if szansa == 0:
            tile = self.get_tile().get_losowy_pusty_sasiad()
            if tile is None:
                tile = partner.get_tile().get_losowy_pusty_sasiad()
        else:
            tile = partner.get_tile().get_losowy_pusty_sasiad()
            if tile is None:
                tile = self.get_tile().get_losowy_pusty_sasiad()

        if tile is None:
            return False
        dziecko = self.stworz_kopie()
        self._swiat.dodaj_organizm(dziecko)
        dziecko.set_tile(tile)
        dziecko.set_pozycja(tile.get_pozycja())
        tile.set_organizm(dziecko)
        print(str(partner) + " oraz " + str(self) + " maja dziecko: " + str(dziecko))
        print()
        return True

    def czy_roll(self):
        return random.random() <= self._szansa_roll

    def _dodge_attack(self, organizm):
        return False

    def kolizja(self, organizm):
        if self.get_sila() > organizm.get_sila():
            if not organizm.czy_sparowal(self):
                organizm.umrzyj(self)
            return False
        else :
            if self._dodge_attack(organizm):
                print(str(self) + "uciekl od ataku " + str(organizm))
                return True
            elif self.czy_sparowal(organizm):
                print(str(self) + " sparowal atak " + str(organizm))
                return False
            else:
                self.umrzyj(organizm)
                return True