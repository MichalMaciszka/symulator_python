from .abstract_zwierze import AbstractZwierze
import pygame
import random


class Antylopa(AbstractZwierze):

    __nazwa = "Antylopa"
    __sila = 4
    __inicjatywa = 4
    __zasieg_ruchu = 2
    __szansa_roll = 1
    __kolor = (137, 137, 255)
    __tekstura = None
    __tekstura_path = "antylopa.png"
    __szansa_dodge = 0.5

    def __init__(self, swiat, tile, pozycja, wiek=1):
        if self.__tekstura is None and self.__tekstura_path:
            self.__tekstura = pygame.image.load(self.__tekstura_path)
        super().__init__(swiat, tile, pozycja, self.__kolor, self.__nazwa, self.__tekstura, self.__sila, self.__inicjatywa, self.__zasieg_ruchu, self.__szansa_roll, wiek)

    def stworz_kopie(self):
        return Antylopa(self._swiat, self.get_tile(), self.get_pozycja())

    def _czy_ten_sam_gatunek(self, organizm):
        return isinstance(organizm, Antylopa)

    def _dodge_attack(self, organizm):
        if not isinstance(organizm, AbstractZwierze):
            return False
        if not random.random() <= self.__szansa_dodge:
            return False
        tile = self.get_tile().get_losowy_pusty_sasiad()
        if tile is None:
            return False
        else:
            return self.ruch(tile)
