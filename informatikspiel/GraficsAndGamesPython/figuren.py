from graphics_and_games_klassen import Figur

class spielerFigur(Figur):
    def __init__(self, x, y, groesse):
        super().__init__(x=x, y=y, groesse=groesse, sichtbar=True)
        self.FigurteilFestlegenRechteck(-35, 20, 5, 5, (32,18,77))
        self.FigurteilFestlegenRechteck(-30, 25, 60, 5, (32,18,77))
        self.FigurteilFestlegenRechteck(-40, -5, 5, 25, (32,18,77))
        self.FigurteilFestlegenRechteck(-35, -15, 5, 10, (32,18,77))
        self.FigurteilFestlegenRechteck(-30, -20, 5, 5, (32,18,77))
        self.FigurteilFestlegenRechteck(-25, -25, 5, 5, (32,18,77))
        self.FigurteilFestlegenRechteck(-20, -30, 40, 5, (32,18,77))
        self.FigurteilFestlegenRechteck(25, -20, 5, 5, (32,18,77))
        self.FigurteilFestlegenRechteck(20, -25, 5, 5, (32,18,77))
        self.FigurteilFestlegenRechteck(30, -15, 5, 10, (32,18,77))
        self.FigurteilFestlegenRechteck(35, -5,5, 25, (32,18,77))
        self.FigurteilFestlegenRechteck(30, 20, 5, 5, (32,18,77))
        self.FigurteilFestlegenRechteck(-30, 20, 60, 5, (37,76,129))
        self.FigurteilFestlegenRechteck(-35, -5, 70, 25, (37,76,129))
        self.FigurteilFestlegenRechteck(-15, -25, 30, 45, (66,131,223))
        self.FigurteilFestlegenRechteck(-20, -25, 40, 5, (66,131,223))
        self.FigurteilFestlegenRechteck(-25, -20, 50, 35, (66,131,223))
        self.FigurteilFestlegenRechteck(-30, -15, 60, 25, (66,131,223))
        self.FigurteilFestlegenRechteck(-15, -5, 5, 10, "schwarz")
        self.FigurteilFestlegenRechteck(10, -5, 5, 10, "schwarz")
        self.FigurteilFestlegenRechteck(-5, 5, 10, 5, "schwarz")

class feuerballFigur(Figur):
    def __init__(self, x, y, groesse, winkel):
        super().__init__(x=x, y=y, groesse=groesse, sichtbar=True)
        self.FigurteilFestlegenRechteck(-20,-15,55,30, (240,9,9))
        self.FigurteilFestlegenRechteck(10,-20,20,40, (240,9,9))
        self.FigurteilFestlegenRechteck(-20,-10,55,20, (240,148,9))
        self.FigurteilFestlegenRechteck(15,-15,15,30, (240,148,9))
        self.FigurteilFestlegenRechteck(35,-10,5,20, (240,9,9))
        self.FigurteilFestlegenRechteck(-30,-15,15,10, (240,9,9))
        self.FigurteilFestlegenRechteck(-40,-15,10,5, (240,9,9))
        self.FigurteilFestlegenRechteck(-20,-5,10,5, (240,9,9))
        self.FigurteilFestlegenRechteck(-25,0,5,5, (240,9,9))
        self.FigurteilFestlegenRechteck(-30,5,20,5, (240,9,9))
        self.FigurteilFestlegenRechteck(10, -5, 20, 10, (240,213,9))
        self.FigurteilFestlegenRechteck(20, -10, 5, 20, (240,213,9))
        self.FigurteilFestlegenRechteck(0, 0, 10, 5, (240,213,9))
        self.Drehen(winkel)

class plusFigur(Figur):  
    def __init__(self, x, y, groesse):
            super().__init__(x=x, y=y, groesse=groesse, sichtbar=True)
            self.FigurteilFestlegenRechteck(-25, -15, 50, 30, "schwarz")  
            self.FigurteilFestlegenRechteck(-15, -25, 30, 50, "schwarz") 
            self.FigurteilFestlegenRechteck(-20, -10, 40, 20, "grün")  
            self.FigurteilFestlegenRechteck(-10, -20, 20, 40, "grün")

class herzFigur(Figur):
    def __init__(self, x, y, groesse):
        super().__init__(x=x, y=y, groesse=groesse, sichtbar=True)
        self.FigurteilFestlegenRechteck(-15, -15, 40, 30, "schwarz")
        self.FigurteilFestlegenRechteck(-15, -15, 30, 40, "schwarz")
        self.FigurteilFestlegenRechteck(-10, -10, 30, 20, "rot")
        self.FigurteilFestlegenRechteck(-10, -10, 20, 30, "rot")
        self.Drehen(135)

class schrumpfFigur(Figur):
    def __init__(self, x, y, groesse):
        super().__init__(x=x, y=y, groesse=groesse, sichtbar=False)
        self.FigurteilFestlegenRechteck(-5, -25, 15, 35, "schwarz")

        self.FigurteilFestlegenRechteck(-15, 10, 35, 10, "schwarz")
        self.FigurteilFestlegenRechteck(-10, 20, 25, 5, "schwarz")
        self.FigurteilFestlegenRechteck(-5, 25, 15, 5, "schwarz")
        self.FigurteilFestlegenRechteck(0, 30, 5, 5, "schwarz")

        self.FigurteilFestlegenRechteck(0, -20, 5, 35, "blau")
        self.FigurteilFestlegenRechteck(-10, 15, 25, 5, "blau")
        self.FigurteilFestlegenRechteck(-5, 20, 15, 5, "blau")
        self.FigurteilFestlegenRechteck(0, 25, 5, 5, "blau")

if __name__ == "__main__":
    # Design testen
    spieler = spielerFigur(100, 100, 100)
    herz = herzFigur(100, 200, 100)
    feuerball = feuerballFigur(100, 300, 100, 0)
    plus = plusFigur(100, 400, 100)
    pfeil = schrumpfFigur(100, 500, 100)