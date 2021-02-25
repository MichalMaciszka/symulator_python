class Kolor:
    def __init__(self, R, G, B):
        self.R=R
        self.G=G
        self.B=B

    def __str__(self):
        return "Kolor("+self.R+", "+self.G+", "+self.B+")"