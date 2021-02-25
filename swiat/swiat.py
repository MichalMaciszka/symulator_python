from mapa import Mapa
import pygame
from pygame.locals import *
import pygame.locals
import random
from Point import Point
from organizmy import *
from mapa import Kierunek
from.menu import Menu

class Swiat:
    __empty_kolor = (70, 70, 70)
    __save_file_extension = ".sav"
    __save_file_path = "saves/"

    def __init__(self, x, y, ekran, rozmiar_komorki, margines, domyslny_tytul):
        self._mapa = Mapa(x, y)
        self._repaint = False
        self._organizmy = list()
        self._nowe_organizmy = list()
        self._tura = 1
        self._czlowiek = None
        self._wymiar_komorki = rozmiar_komorki
        self._margines_komorki = margines
        self._ekran = ekran
        self._domyslny_tytul = domyslny_tytul
        self._obecny_tytul = domyslny_tytul
        self._cmd_input = False
        self._init()
        self._type_present = {}
        self._menu = Menu(self, rozmiar_komorki, margines, ekran)

    def _skaluj_ekran(self):
        komorka = self._wymiar_komorki + self._margines_komorki
        pygame.display.set_mode((komorka * self.get_szerokosc() + self._margines_komorki, komorka * self.get_wysokosc() + self._margines_komorki))

    def _init(self):
        self._skaluj_ekran()
        for x in range(self.get_szerokosc()):
            for y in range(self.get_wysokosc()):
                i = random.randint(0, 60)
                if i <= 10:
                    tile = self._mapa.get_tile(x, y)
                    organizm = None
                    pozycja = Point(x, y)
                    if i == 0:
                        organizm = Lis(self, tile, pozycja)
                    elif i == 1:
                        organizm = Trawa(self, tile, pozycja)
                    elif i == 2:
                        organizm = Mlecz(self, tile, pozycja)
                    elif i == 3:
                        organizm = Guarana(self, tile, pozycja)
                    elif i == 4:
                        organizm = WilczaJagoda(self, tile, pozycja)
                    elif i == 5:
                        organizm = Wilk(self, tile, pozycja)
                    elif i == 6:
                        organizm = Zolw(self, tile, pozycja)
                    elif i == 7:
                        organizm = Owca(self, tile, pozycja)
                    elif i == 8:
                        organizm = BarszczSosnowskiego(self, tile, pozycja)
                    elif i == 9:
                        organizm = Antylopa(self, tile, pozycja)
                    elif i == 10:
                        organizm = CyberOwca(self, tile, pozycja)
                    tile.set_organizm(organizm)
                    self._organizmy.append(organizm)
        while True:
            x = random.randint(0, self._mapa.get_szerokosc() - 1)
            y = random.randint(0, self._mapa.get_wysokosc() - 1)
            tile = self._mapa.get_tile(x, y)
            if tile.empty():
                self._czlowiek = Czlowiek(self, tile, Point(x, y))
                tile.set_organizm(self._czlowiek)
                self._organizmy.append(self._czlowiek)
                break
        self._sortuj_organizmy()

    def nastepna_tura(self):
        print("&&& Runda " + str(self._tura) + " zaczyna sie! &&&")
        for organizm in self._organizmy:
            organizm.akcja()
            organizm.inkrementuj_wiek()
        self._usun_martwe_organizmy()
        self._zaladuj_nowe_organizmy()
        self._sortuj_organizmy()
        print("&&& Runda " + str(self._tura) + " skonczyla sie &&&")
        print()
        self._tura += 1
        self._type_present.clear()

    def _usun_martwe_organizmy(self):
        for i in range(len(self._organizmy) -1, -1, -1):
            if not self._organizmy[i].czy_zywy():
                del self._organizmy[i]

    def _sortuj_organizmy(self):
        self._organizmy.sort(key=lambda organizm: (organizm.get_inicjatywe(), organizm.get_wiek()), reverse=True)


    def rysuj_swiat(self, ekran, wymiar_komorki, margines):
        self._wymiar_komorki = wymiar_komorki
        self._margines_komorki = margines
        self._rysuj_kratke(ekran, wymiar_komorki, margines)
        for organizm in self._organizmy:
            organizm.rysuj(ekran, wymiar_komorki, margines)
        self._menu.rysuj()

    def _rysuj_kratke(self, ekran, wymiar_komorki, margines):
        rect = Rect(-wymiar_komorki, -wymiar_komorki, wymiar_komorki, wymiar_komorki)
        for y in range(self.get_wysokosc()):
            rect.y += wymiar_komorki + margines
            rect.x = - wymiar_komorki
            for x in range(self.get_szerokosc()):
                rect.x += wymiar_komorki + margines
                pygame.draw.rect(ekran, self.__empty_kolor, rect)

    #
    def dodaj_organizm(self, organizm):
        self._nowe_organizmy.append(organizm)

    def dodaj_organizm_od_razu(self, organizm):
        self._organizmy.append(organizm)
        self._sortuj_organizmy()

    def key_pressed(self, event):
        pass

    def _zaladuj_nowe_organizmy(self):
        for organizm in self._nowe_organizmy:
            self._organizmy.append(organizm)

        self._nowe_organizmy.clear()
        self._sortuj_organizmy()

    #
    def needs_repaint(self):
        if self._repaint:
            self._repaint = False
            return True
        return False

    #
    def nowy_swiat(self, szerokosc, wysokosc):
        if szerokosc <= 0 or wysokosc <= 0:
            return False

        self._organizmy.clear()
        self._nowe_organizmy.clear()

    def zapisz_swiat(self, save_name):
        file = open(self.__save_file_path + save_name + self.__save_file_extension, "w")
        file.write("& " + str(self.get_szerokosc()) + " " + str(self.get_wysokosc()) + " " + str(self._tura) + "\n")
        for organizm in self._organizmy:
            file.write(organizm.get_serialized() + "\n")
        file.close()

    def zaladuj_swiat(self, save_name):
        file = open(self.__save_file_path + save_name + self.__save_file_extension, "r")
        for line in file:
            words = line.split()
            if words[0] == "&":
                szerokosc = int(words[1])
                wysokosc = int(words[2])
                tura = int(words[3])
                self._clear(szerokosc, wysokosc)
            elif words[0] in ["Antylopa", "Lis", "Czlowiek", "Owca", "CyberOwca", "Zolw", "Wilk", "WliczaJagoda", "BarszczSosnowskiego", "Trawa", "Guarana", "Mlecz"]:
                x = int(words[1])
                y = int(words[2])
                sila = int(words[3])
                wiek = int(words[4])
                tile = self._mapa.get_tile(x, y)
                organizm = None
                if words[0] == "Czlowiek":
                    organizm = Czlowiek(self, tile, tile.get_pozycja(), wiek)
                    pozostaly_czas = int(words[4])
                    cooldown = int(words[5])
                    organizm.set_pozostaly_czas(pozostaly_czas)
                    organizm.set_cooldown(cooldown)
                    self._czlowiek = organizm

                elif words[0] == "Antylopa":
                    organizm = Antylopa(self, tile, tile.get_pozycja(), wiek)
                elif words[0] == "Lis":
                    organizm = Lis(self, tile, tile.get_pozycja(), wiek)
                elif words[0] == "Owca":
                    organizm = Owca(self, tile, tile.get_pozycja(), wiek)
                elif words[0] == "Zolw":
                    organizm = Zolw(self, tile, tile.get_pozycja(), wiek)
                elif words[0] == "Wilk":
                    organizm = Wilk(self, tile, tile.get_pozycja(), wiek)
                elif words[0] == "CyberOwca":
                    organizm = CyberOwca(self, tile, tile.get_pozycja(), wiek)

                elif words[0] == "WliczaJagoda":
                    organizm = WilczaJagoda(self, tile, tile.get_pozycja(), wiek)
                elif words[0] == "BarszczSosnowskiego":
                    organizm = BarszczSosnowskiego(self, tile, tile.get_pozycja(), wiek)
                elif words[0] == "Trawa":
                    organizm = Trawa(self, tile, tile.get_pozycja(), wiek)
                elif words[0] == "Guarana":
                    organizm = Guarana(self, tile, tile.get_pozycja(), wiek)
                elif words[0] == "Mlecz":
                    organizm = Mlecz(self, tile, tile.get_pozycja(), wiek)

                tile.set_organizm(organizm)
                organizm.zwieksz_sile(sila - organizm.get_sila())
                self._organizmy.append(organizm)
        self._skaluj_ekran()

    def get_szerokosc(self):
        return self._mapa.get_szerokosc()

    def get_wysokosc(self):
        return self._mapa.get_wysokosc()

    def pixel_to_tile(self, event):
        pass

    def _clear(self, szerokosc, wysokosc):
        self._mapa.set_rozmiar(szerokosc, wysokosc)
        self._tura = 1
        self._organizmy.clear()
        self._nowe_organizmy.clear()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and not self._cmd_input:
            # next turn
            if event.key is K_SPACE:
                self.nastepna_tura()
            # player movement
            elif event.key is K_w:
                self._czlowiek.set_kierunek(Kierunek.NORTH)
            elif event.key is K_d:
                self._czlowiek.set_kierunek(Kierunek.EAST)
            elif event.key is K_s:
                self._czlowiek.set_kierunek(Kierunek.SOUTH)
            elif event.key is K_a:
                self._czlowiek.set_kierunek(Kierunek.WEST)
            elif event.key is K_f:
                self._czlowiek.aktywuj_umiejetnosc()
            elif event.key is K_F5:
                self.zapisz_swiat("quick_save")
            elif event.key is K_F9:
                self.zaladuj_swiat("quick_save")
            elif event.key is K_SEMICOLON:
                self._cmd_input = True
                self._obecny_tytul = ":"
                pygame.display.set_caption(self._obecny_tytul)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            tile = self._pixel_to_tile(event)
            print(tile)
            self._menu.handle_event(event, tile)
        # CMD input
        elif event.type == pygame.KEYDOWN and self._cmd_input:
            # enter CMD
            if event.key == pygame.K_RETURN:
                self._komenda(self._obecny_tytul)
                return
            # backspace
            elif event.key == pygame.K_BACKSPACE and len(self._obecny_tytul) > 1:
                self._obecny_tytul = self._obecny_tytul[:-1]
            # backspace on last char, exit CMD mode without sending anything
            elif event.key == pygame.K_BACKSPACE and len(self._obecny_tytul) == 1:
                self._obecny_tytul = self._domyslny_tytul
                self._cmd_input = False
            # add character to cmd
            else:
                self._obecny_tytul += event.unicode
            # update title
            pygame.display.set_caption(self._obecny_tytul)

    def _pixel_to_tile(self, mouse_event):
        if mouse_event.type == pygame.MOUSEBUTTONDOWN and (mouse_event.button == 1 or mouse_event.button == 3):
            x = mouse_event.pos[0] // (self._margines_komorki + self._wymiar_komorki)
            y = mouse_event.pos[1] // (self._margines_komorki + self._wymiar_komorki)
            return self._mapa.get_tile(x, y)
        else:
            return None

    def _komenda(self, input_cmd):
        cmd = input_cmd[1:].split()
        main_command = cmd[0]
        if main_command == "new":
            if len(cmd) == 3:
                szerokosc = int(cmd[1])
                wysokosc = int(cmd[2])
                self.nowy_swiat(szerokosc, wysokosc)
                self._exit_cmd_mode()
            else:
                self._blad_cmd()
        elif main_command == "save":
            if len(cmd) == 2:
                self.zapisz_swiat(cmd[1])
                self._exit_cmd_mode()
            else:
                self._blad_cmd()
        elif main_command == "load":
            if len(cmd) == 2:
                self.zaladuj_swiat(cmd[1])
                self._exit_cmd_mode()
            else:
                self._blad_cmd()
        else:
            self._blad_cmd()

    def _blad_cmd(self):
        pygame.display.set_caption("NIEPRAWIDLOWA KOMENDA")

    def _exit_cmd_mode(self):
        self._obecny_tytul = self._domyslny_tytul
        self._update_title()
        self._cmd_input = False

    def _update_title(self):
        pygame.display.set_caption(self._obecny_tytul)

    def is_type_of_organism_present(self, organism_type):
        if organism_type in self._type_present:
            return self._type_present[organism_type]

        for orgaznim in self._organizmy:
            if isinstance(orgaznim, organism_type):
                self._type_present[organism_type] = True
                return True
            self._type_present[organism_type] = False
        return False
