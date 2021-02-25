from .abstract_roslina import AbstractRoslina
import pygame

class Mlecz(AbstractRoslina):
    __sila = 0
    __kolor = (165, 156, 30)
    __proby_rozmnozenia = 3
    __nazwa = "Mlecz"
    __tekstura = None
    __tekstura_path = "mlecz.png"

    def __init__(self, swiat, tile, pozycja, wiek=1):
        if self.__tekstura is None and self.__tekstura_path:
            self.__tekstura = pygame.image.load(self.__tekstura_path)
        super().__init__(swiat, tile, pozycja, self.__kolor, self.__nazwa, self.__tekstura, self.__sila, wiek)

    def akcja(self):
        for i in range(0, self.__proby_rozmnozenia):
            super().akcja()

    def stworz_kopie(self):
        return Mlecz(self._swiat, self.get_tile(), self.get_pozycja())
