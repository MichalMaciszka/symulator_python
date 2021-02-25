from .abstract_zwierze import AbstractZwierze
import pygame


class Owca(AbstractZwierze):

    __nazwa = "Owca"
    __sila = 4
    __inicjatywa = 4
    __zasieg_ruchu = 1
    __szansa_roll = 1
    __kolor = (255, 255, 255)
    __tekstura = None
    __tekstura_path = "owca.png"

    def __init__(self, swiat, tile, pozycja, wiek=1):
        if self.__tekstura is None and self.__tekstura_path:
            self.__tekstura = pygame.image.load(self.__tekstura_path)
        super().__init__(swiat, tile, pozycja, self.__kolor, self.__nazwa, self.__tekstura, self.__sila, self.__inicjatywa, self.__zasieg_ruchu, self.__szansa_roll, wiek)


    def stworz_kopie(self):
        return Owca(self._swiat, self.get_tile(), self.get_pozycja())

    def _czy_ten_sam_gatunek(self, organizm):
        return isinstance(organizm, Owca)
