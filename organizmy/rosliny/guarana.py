from .abstract_roslina import AbstractRoslina
import pygame


class Guarana(AbstractRoslina):
    __sila = 0
    __kolor = (180, 30, 30)
    __nazwa = "Guarana"
    __tekstura = None
    __tekstura_path = "guarana.png"
    __zyskiwana_sila = 3

    def __init__(self, swiat, tile, pozycja, wiek=1):
        if self.__tekstura is None and self.__tekstura_path:
            self.__tekstura = pygame.image.load(self.__tekstura_path)
        super().__init__(swiat, tile, pozycja, self.__kolor, self.__nazwa, self.__tekstura, self.__sila, wiek)

    def stworz_kopie(self):
        return Guarana(self._swiat, self.get_tile(), self.get_pozycja())

    def kolizja(self, organizm):
        organizm.zwieksz_sile(self.__zyskiwana_sila)
        return super().kolizja(organizm)
