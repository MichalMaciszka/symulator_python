from .abstract_roslina import AbstractRoslina
import pygame


class Trawa(AbstractRoslina):

    __sila = 0
    __kolor = (30, 180, 70)
    __nazwa = "Trawa"
    __tekstura = None
    __tekstura_path = "trawa.png"

    def __init__(self, swiat, tile, pozycja, wiek=1):
        if self.__tekstura is None and self.__tekstura_path:
            self.__tekstura = pygame.image.load(self.__tekstura_path)

        super().__init__(swiat, tile, pozycja, self.__kolor, self.__nazwa, self.__tekstura, self.__sila, wiek)

    def stworz_kopie(self):
        return Trawa(self._swiat, self.get_tile(), self.get_pozycja())
