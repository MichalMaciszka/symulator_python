from .abstract_zwierze import AbstractZwierze
import pygame
from mapa import Kierunek
import random


class Czlowiek(AbstractZwierze):

    __nazwa = "Czlowiek"
    __sila = 5
    __inicjatywa = 4
    __zasieg_ruchu = 1
    __szansa_roll = 1
    __kolor = (0, 0, 0)
    __tekstura = None
    __tekstura_path = "czlowiek.png"

    __czas_trwania_umiejetnosci = 5
    __cooldown_umiejetnosci = 5

    def __init__(self, swiat, tile, pozycja, wiek=1):
        if self.__tekstura is None and self.__tekstura_path:
            self.__tekstura = pygame.image.load(self.__tekstura_path)
        super().__init__(swiat, tile, pozycja, self.__kolor, self.__nazwa, self.__tekstura, self.__sila, self.__inicjatywa, self.__zasieg_ruchu, self.__szansa_roll, wiek)
        self.__cooldown = 0
        self._pozostaly_czas = 0
        self._kierunek = Kierunek.NORTH

    def stworz_kopie(self):
        return None

    def _czy_ten_sam_gatunek(self, organizm):
        return False

    def get_target_tile(self):
        return self.get_tile().get_sasiad(self._kierunek)

    def __umiejetnosc(self):
        if self._pozostaly_czas == 0:
            self._zasieg_ruchu = 1
            return
        if self._pozostaly_czas > 2:
            self._zasieg_ruchu = 2
        elif self._pozostaly_czas > 0:
            szansa = random.randint(0, 1)
            if szansa == 0:
                self._zasieg_ruchu = 1
            else:
                self._zasieg_ruchu = 2

    def aktywuj_umiejetnosc(self):
        if self.__cooldown > 0 or self._pozostaly_czas > 0 or not self._czy_zywy:
            return False
        self.__cooldown = self.__cooldown_umiejetnosci
        self._pozostaly_czas = self.__czas_trwania_umiejetnosci
        print("&&& Aktywowano umiejetnosc &&&")
        self.__umiejetnosc()

    def set_kierunek(self, kierunek):
        self._kierunek = kierunek

    def __tick(self):
        if self._pozostaly_czas > 0:
            self._pozostaly_czas -= 1
            if self._pozostaly_czas == 0:
                print("&&& Skonczyla sie umiejetnosc specjalna &&&")
        elif self.__cooldown > 0:
            self.__cooldown -= 1
            if self.__cooldown == 0:
                print("(Umiejetnosc gotowa do uzycia)")

    def akcja(self):
        if not self.czy_zywy():
            return
        self.__umiejetnosc()
        super().akcja()
        self.__umiejetnosc()
        self.__tick()

    def set_cooldown(self, cooldown):
        self.__cooldown = cooldown

    def set_pozostaly_czas(self, pozostaly_czas):
        self._pozostaly_czas = pozostaly_czas

    def get_serialized(self):
        return super().get_serialized() + " " + str(self._pozostaly_czas) + " " + str(self.__cooldown)
