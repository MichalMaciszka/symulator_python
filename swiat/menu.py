import pygame
from organizmy import *
from Point import Point
from pygame.locals import *


class Menu:
    __rzedy = 3
    __kolumny = 3
    __kolor_tla = (30, 30, 30)
    __kolor_ramki = (110, 110, 110)

    def __init__(self, swiat, wymiar_komorki, margines, ekran):
        self._swiat = swiat
        self._wymiar_komorki = wymiar_komorki
        self._margines = margines
        self._ekran = ekran
        # self._ikony = [[None for  x in range(self.__kolumny)] for y in range(self.__rzedy)]
        pos = Point(-1, -1)
        self._ikony = [
            [Antylopa(swiat, None, pos), CyberOwca(swiat, None, pos), Lis(swiat, None, pos)],
            [Owca(swiat, None, pos), Zolw(swiat, None, pos), Wilk(swiat, None, pos)],
            [WilczaJagoda(swiat, None, pos), BarszczSosnowskiego(swiat, None, pos), Trawa(swiat, None, pos)],
            [Guarana(swiat, None, pos), Mlecz(swiat, None, pos)]
        ]
        print(self._ikony)
        self._wlaczone = False
        self._ostatnie_x = 0
        self._ostatnie_y = 0
        self.tile = None

    def rysuj(self):
        if self._wlaczone:
            wysokosc = (self._wymiar_komorki + self._margines) * len(self._ikony) + self._margines
            szerokosc = (self._wymiar_komorki + self._margines) * len(self._ikony[0]) + self._margines
            pygame.draw.rect(self._ekran, self.__kolor_ramki, (self._ostatnie_x - 1, self._ostatnie_y - 1, szerokosc+2, wysokosc+2), 6)
            for y in range(len(self._ikony)):
                for x in range(len(self._ikony[y])):
                    x_pos = self._ostatnie_x + x * (self._wymiar_komorki + self._margines) + self._margines
                    y_pos = self._ostatnie_y + y * (self._wymiar_komorki + self._margines) + self._margines
                    Organizm.rysuj_ikone(self._ikony[y][x], self._ekran, x_pos, y_pos, self._wymiar_komorki)

    def wlaczone(self):
        return self._wlaczone

    def wylacz(self):
        self._wlaczone = False

    def handle_event(self, event, clicked_tile):
        if event.type == MOUSEBUTTONDOWN and event.button == 3:
            if not self._wlaczone:
                self._wlaczone = True

                self._ostatnie_x, self._ostatnie_y = self.czy_menu_miesci_sie_na_ekranie(event.pos)
                self._tile = clicked_tile
            else:
                x = (event.pos[0] - self._ostatnie_x) // (self._wymiar_komorki + self._margines)
                y = (event.pos[1] - self._ostatnie_y) // (self._wymiar_komorki + self._margines)
                print("Wybrano: " + str(x) + " " + str(y))
                if y in range(0, len(self._ikony)) and x in range(0, len(self._ikony[y])):
                    target_tile = self._tile
                    if target_tile is not None and target_tile.empty():
                        organizm = self._ikony[y][x].stworz_kopie()
                        organizm.set_tile(target_tile)
                        organizm.set_pozycja(target_tile.get_pozycja())
                        target_tile.set_organizm(organizm)
                        print("Tworzenie " + str(organizm) + " na " + str(target_tile))
                        self._swiat.dodaj_organizm_od_razu(organizm)

                self._wlaczone = False

    def czy_menu_miesci_sie_na_ekranie(self, pos):
        (x, y) = pos
        ekran_w, ekran_s = self._ekran.get_height(), self._ekran.get_width()
        komorka = self._wymiar_komorki + self._margines
        menu_w = komorka * len(self._ikony) + self._margines + 4
        menu_s = komorka * len(self._ikony) + self._margines + 4
        fit_x = ekran_s - menu_s - x
        fit_y = ekran_w - menu_w - y
        if fit_x < 0:
            x += fit_x
        if fit_y < 0:
            y += fit_y

        return x, y
