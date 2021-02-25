from .abstract_zwierze import AbstractZwierze
from path_finding.breadth_first_search import breadth_first_search as bfs_find_path
import pygame


class CyberOwca(AbstractZwierze):
    __nazwa = "CyberOwca"
    __sila = 11
    __inicjatywa = 4
    __zasieg_ruchu = 1
    __szansa_roll = 1
    __kolor = (255, 0, 255)
    __tekstura = None
    __tekstura_path = "cyber_owca.png"

    def __init__(self, swiat, tile, pozycja, wiek=1):
        if self.__tekstura is None and self.__tekstura_path:
            self.__tekstura = pygame.image.load(self.__tekstura_path)
        super().__init__(swiat, tile, pozycja, self.__kolor, self.__nazwa, self.__tekstura, self.__sila, self.__inicjatywa, self.__zasieg_ruchu, self.__szansa_roll, wiek)

    def stworz_kopie(self):
        return CyberOwca(self._swiat, self.get_tile(), self.get_pozycja())

    def _czy_ten_sam_gatunek(self, organizm):
        return isinstance(organizm, CyberOwca)

    def get_target_tile(self):
        from ..rosliny import BarszczSosnowskiego
        if not self._swiat.is_type_of_organism_present(BarszczSosnowskiego):
            return super().get_target_tile()
        path = bfs_find_path(self.get_tile(), BarszczSosnowskiego)

        if len(path) == 0:
            return super().get_target_tile()
        else:
            return path[0]

    def umrzyj(self, organizm):
        from ..rosliny import BarszczSosnowskiego
        if isinstance(organizm, BarszczSosnowskiego):
            return False
        else:
            return super().umrzyj(organizm)
