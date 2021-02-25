from Point import Point
import pygame
import sys
from pygame.locals import *
from mapa import Mapa
from organizmy import Organizm
from swiat import Swiat


szerokosc = 20
wysokosc = 20
szerokosc = int(input("Podaj szerokosc "))
wysokosc = int(input("Podaj wysokosc "))
rozmiar_komorki = 20
margines = 5
background = (40, 40, 40)
default_title = "Michal Maciszka 180522"

pygame.init()
pygame.font.init()
ekran = pygame.display.set_mode(((rozmiar_komorki + margines) * szerokosc + margines, (rozmiar_komorki + margines) * wysokosc + margines))

pygame.display.set_caption(default_title)
ekran.fill(background)

swiat = Swiat(szerokosc, wysokosc, ekran, rozmiar_komorki, margines, default_title)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type is QUIT or (event.type == pygame.KEYDOWN and event.key is K_q):
            sys.exit()
        swiat.handle_event(event)

    ekran.fill(background)
    swiat.rysuj_swiat(ekran, rozmiar_komorki, margines)
    pygame.display.update()
    pygame.time.delay(16)
