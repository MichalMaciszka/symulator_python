from .abstract_zwierze import AbstractZwierze
import pygame


class Wilk(AbstractZwierze):

    __nazwa = "Wilk"
    __sila = 9
    __inicjatywa = 5
    __zasieg_ruchu = 1
    __szansa_roll = 1
    __kolor = (137, 137, 137)
    __tekstura = None
    __tekstura_path = "wilk.png"

    def __init__(self, swiat, tile, pozycja, wiek=1):
        if self.__tekstura is None and self.__tekstura_path:
            self.__tekstura = pygame.image.load(self.__tekstura_path)
        super().__init__(swiat, tile, pozycja, self.__kolor, self.__nazwa, self.__tekstura, self.__sila, self.__inicjatywa, self.__zasieg_ruchu, self.__szansa_roll, wiek)

    def stworz_kopie(self):
        return Wilk(self._swiat, self.get_tile(), self.get_pozycja())

    def _czy_ten_sam_gatunek(self, organizm):
        return isinstance(organizm, Wilk)
