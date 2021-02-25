from .abstract_roslinatrujaca import AbstractRoslinaTrujaca
import pygame

class WilczaJagoda(AbstractRoslinaTrujaca):
    __sila = 99
    __kolor = (137, 30, 137)
    __nazwa = "WliczaJagoda"
    __tekstura = None
    __tekstura_path = "wilcza_jagoda.png"

    def __init__(self, swiat, tile, pozycja, wiek=1):
        if self.__tekstura is None and self.__tekstura_path:
            self.__tekstura = pygame.image.load(self.__tekstura_path)
        super().__init__(swiat, tile, pozycja, self.__kolor, self.__nazwa, self.__tekstura, self.__sila, wiek)

    def stworz_kopie(self):
        return WilczaJagoda(self._swiat, self.get_tile(), self.get_pozycja())
