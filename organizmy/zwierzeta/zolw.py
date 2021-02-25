from .abstract_zwierze import AbstractZwierze
import pygame

class Zolw(AbstractZwierze):

    __nazwa = "Zolw"
    __sila = 2
    __inicjatywa = 1
    __zasieg_ruchu = 1
    __szansa_roll = 0.5
    __paruj_dla_sily_mniejszej = 5
    __kolor = (70, 255, 70)
    __tekstura = None
    __tekstura_path = "zolw.png"

    def __init__(self, swiat, tile, pozycja, wiek=1):
        if self.__tekstura is None and self.__tekstura_path:
            self.__tekstura = pygame.image.load(self.__tekstura_path)
        super().__init__(swiat, tile, pozycja, self.__kolor, self.__nazwa, self.__tekstura, self.__sila, self.__inicjatywa, self.__zasieg_ruchu, self.__szansa_roll, wiek)


    def stworz_kopie(self):
        return Zolw(self._swiat, self.get_tile(), self.get_pozycja())

    def _czy_ten_sam_gatunek(self, organizm):
        return isinstance(organizm, Zolw)

    def czy_sparowal(self, organizm):
        return self.__paruj_dla_sily_mniejszej > organizm.get_sila()
