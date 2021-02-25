from .abstract_roslina import AbstractRoslina

class AbstractRoslinaTrujaca(AbstractRoslina):
    def __init__(self, swiat, tile, pozycja, kolor, nazwa, tekstura, sila, wiek=1):
        super().__init__(swiat, tile, pozycja, kolor, nazwa, tekstura, sila, wiek)

    def kolizja(self, organizm):
        if not self.czy_zywy():
            return True
        organizm.umrzyj(self)
        return False

