from .abstract_zwierze import AbstractZwierze
import pygame


class Lis(AbstractZwierze):
    __nazwa = "Lis"
    __sila = 3
    __inicjatywa = 7
    __zasieg_ruchu = 1
    __szansa_roll = 1
    __kolor = (169, 104, 61)
    __tekstura = None
    __tekstura_path = "lis.png"

    def __init__(self, swiat, tile, pozycja, wiek=1):
        if self.__tekstura is None and self.__tekstura_path:
            self.__tekstura = pygame.image.load(self.__tekstura_path)
        super().__init__(swiat, tile, pozycja, self.__kolor, self.__nazwa, self.__tekstura, self.__sila, self.__inicjatywa, self.__zasieg_ruchu, self.__szansa_roll, wiek)


    def stworz_kopie(self):
        return Lis(self._swiat, self.get_tile(), self.get_pozycja())

    def _czy_ten_sam_gatunek(self, organizm):
        return isinstance(organizm, Lis)

    def get_target_tile(self):
        return self.get_tile().get_losowy_slabszy_sasiad(self.get_sila())
