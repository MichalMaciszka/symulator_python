import Point
from abc import ABC, abstractmethod
import pygame


class Organizm(ABC):
    def __init__(self, swiat, tile, pozycja, kolor, nazwa, tekstura, sila, inicjatywa, wiek=1):
        self._swiat = swiat
        self._tile = tile
        self._pozycja = pozycja
        self._sila = sila
        self._inicjatywa = inicjatywa
        self._wiek = wiek
        self._czy_zywy = True
        self._kolor = kolor
        self._nazwa = nazwa
        self._tekstura = tekstura

    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def kolizja(self, organizm):
        pass

    def rysuj(self, ekran, wymiar_komorki, margines):
        if not self._czy_zywy:
            return
        x = margines + self._pozycja.x * (wymiar_komorki + margines)
        y = margines + self._pozycja.y * (wymiar_komorki + margines)
        self.rysuj_ikone(self, ekran, x, y, wymiar_komorki)

    @staticmethod
    def rysuj_ikone(self, ekran, x, y, wymiar_komorki):
        tekstura = self._tekstura
        if tekstura is None:
            pygame.draw.rect(ekran, self._kolor, (x, y, wymiar_komorki, wymiar_komorki))
        else:
            ekran.blit(tekstura, (x, y))

    def get_pozycja(self):
        return self._pozycja

    def set_pozycja(self, point):
        self._pozycja = point

    def get_sila(self):
        return self._sila

    def zwieksz_sile(self, delta):
        self._sila += delta

    def get_inicjatywe(self):
        return self._inicjatywa

    def get_tile(self):
        return self._tile

    def set_tile(self, tile):
        self._tile = tile

    def ruch(self, tile):
        if not tile.empty():
            return False
        self._tile.set_organizm(None)
        self.set_tile(tile)
        tile.set_organizm(self)
        self._pozycja = tile.get_pozycja()
        return True

    def czy_zywy(self):
        return self._czy_zywy

    def umrzyj(self, organizm):
        print(str(self) + " zostal zabity przez " + str(organizm))
        self._czy_zywy = False
        self._tile.set_organizm(None)
        self._tile = None
        return True

    def czy_sparowal(self, organizm):
        return False

    def get_kolor(self):
        return self._kolor

    @abstractmethod
    def stworz_kopie(self):
        pass

    def __str__(self):
        return self._nazwa + "[" + str(self._pozycja.x) + ", " + str(self._pozycja.y) + "](" + str(self._sila) + ")"

    def get_nazwa(self):
        return self._nazwa

    def get_tekstura(self):
        return self._tekstura

    def get_serialized(self):
        return self._nazwa + " " + str(self._pozycja.x) + " " + str(self._pozycja.y) + " " + str(self._sila) + " " + str(self._wiek)

    def get_wiek(self):
        return self._wiek
    def inkrementuj_wiek(self):
        self._wiek += 1

