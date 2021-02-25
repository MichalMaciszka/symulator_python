from .abstract_roslinatrujaca import AbstractRoslinaTrujaca
from ..zwierzeta import AbstractZwierze


class BarszczSosnowskiego(AbstractRoslinaTrujaca):
    __sila = 10
    __kolor = (255, 60, 30)
    __nazwa = "BarszczSosnowskiego"
    __tekstura = None
    __tekstura_path = ""

    def __init__(self, swiat, tile, pozycja, wiek=1):
        super().__init__(swiat, tile, pozycja, self.__kolor, self.__nazwa, self.__tekstura, self.__sila, wiek)

    def stworz_kopie(self):
        return BarszczSosnowskiego(self._swiat, self.get_tile(), self.get_pozycja())

    def akcja(self):
        if not self.czy_zywy():
            return
        sasiedzi = self.get_tile().get_zajeci_sasiedzi()
        for tile in sasiedzi:
            organizm = tile.get_organizm()
            if isinstance(organizm, AbstractZwierze):
                organizm.umrzyj(self)

    def kolizja(self, organizm):
        from ..zwierzeta.cyber_owca import CyberOwca
        if isinstance(organizm, CyberOwca):
            self.umrzyj(organizm)
            return True
        else:
            super().kolizja(organizm)
