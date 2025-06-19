from graphics_and_games_klassen import *
from random import randint, choice

class Spieler(Figur):
    def __init__(self, x, y, groesse):
        super().__init__(x=x, y=y, groesse=groesse, sichtbar=True)
        self.original_groesse = groesse

        farbe_1 = (32, 18, 77)
        farbe_2 = (37, 76, 129)
        farbe_3 = (66, 131, 223)

        # Körperteile – Rechtecke der Spielfigur
        for coords, farbe in [
            ((-35, 20, 5, 5), farbe_1),
            ((-30, 25, 60, 5), farbe_1),
            ((-40, -5, 5, 25), farbe_1),
            ((-35, -15, 5, 10), farbe_1),
            ((-30, -20, 5, 5), farbe_1),
            ((-25, -25, 5, 5), farbe_1),
            ((-20, -30, 40, 5), farbe_1),
            ((25, -20, 5, 5), farbe_1),
            ((20, -25, 5, 5), farbe_1),
            ((30, -15, 5, 10), farbe_1),
            ((35, -5, 5, 25), farbe_1),
            ((30, 20, 5, 5), farbe_1),
            ((-30, 20, 60, 5), farbe_2),
            ((-35, -5, 70, 25), farbe_2),
            ((-15, -25, 30, 45), farbe_3),
            ((-20, -25, 40, 5), farbe_3),
            ((-25, -20, 50, 35), farbe_3),
            ((-30, -15, 60, 25), farbe_3),
            ((-15, -5, 5, 10), "schwarz"),
            ((10, -5, 5, 10), "schwarz"),
            ((-5, 5, 10, 5), "schwarz")
        ]:
            self.FigurteilFestlegenRechteck(*coords, farbe)


class Enemy(Figur):
    def __init__(self, x, y, groesse):
        super().__init__(x=x, y=y, groesse=groesse, sichtbar=True)
        teile = [
            (-20, -15, 55, 30, (240, 9, 9)),
            (10, -20, 20, 40, (240, 9, 9)),
            (-20, -10, 55, 20, (240, 148, 9)),
            (15, -15, 15, 30, (240, 148, 9)),
            (35, -10, 5, 20, (240, 9, 9)),
            (-30, -15, 15, 10, (240, 9, 9)),
            (-40, -15, 10, 5, (240, 9, 9)),
            (-20, -5, 10, 5, (240, 9, 9)),
            (-25, 0, 5, 5, (240, 9, 9)),
            (-30, 5, 20, 5, (240, 9, 9)),
            (10, -5, 20, 10, (240, 213, 9)),
            (20, -10, 5, 20, (240, 213, 9)),
            (0, 0, 10, 5, (240, 213, 9)),
        ]
        for t in teile:
            self.FigurteilFestlegenRechteck(*t)
        self.Drehen(180)


class Spiel(Ereignisbehandlung):
    def __init__(self):
        super().__init__()

        self.p1 = Spieler(50, 300, 80)
        self.tasten_status = {t: False for t in ["w", "a", "s", "d", "q", "e", "space"]}
        self.TaktdauerSetzen(100 / 60)
        self.Spielzuruecksetzen()

    def Spielzuruecksetzen(self):
        self.speed = 1
        self.schrumpfen_cooldown = 0
        self.schrumpfen_timer = 0

        self.p1.PositionSetzen(50, 300)
        self.p1.GroesseSetzen(self.p1.original_groesse)

    def TasteGedrueckt(self, taste):
        if taste in self.tasten_status:
            self.tasten_status[taste] = True
        elif taste == "escape":
            self.Anhalten()

    def TasteLosgelassen(self, taste):
        if taste in self.tasten_status:
            self.tasten_status[taste] = False

    def bewegen(self, p):
        dx = dy = 0
        if self.tasten_status["w"]: dy -= self.speed
        if self.tasten_status["s"]: dy += self.speed
        if self.tasten_status["a"]: dx -= self.speed
        if self.tasten_status["d"]: dx += self.speed

        min_x, max_x = p.groesse * 0.4, 800 - p.groesse * 0.4
        min_y, max_y = p.groesse * 0.3, 600 - p.groesse * 0.3

        new_x = max(min_x, min(p.x + dx, max_x))
        new_y = max(min_y, min(p.y + dy, max_y))

        p.PositionSetzen(new_x, new_y)

    def schrumpfen(self, p):
        if self.tasten_status["e"] and self.schrumpfen_cooldown == 0 and self.schrumpfen_timer == 0:
            p.GroesseSetzen(40)
            self.schrumpfen_timer = 1800
            self.schrumpfen_cooldown = 3000

    def schrumpfenlogik(self, p):
        if self.schrumpfen_timer > 0:
            self.schrumpfen_timer -= 1
            if self.schrumpfen_timer == 0:
                p.GroesseSetzen(p.original_groesse)
        if self.schrumpfen_cooldown > 0:
            self.schrumpfen_cooldown -= 1

    def collision(self, p, enemys):
        for e in enemys:
            if p.BeruehrtObjekt(e):
                return True

    def AktionAusfuehren(self):
        self.bewegen(self.p1)
        self.schrumpfen(self.p1)
        self.schrumpfenlogik(self.p1)

if __name__ == "__main__":
    spiel = Spiel()
    spiel.Starten()
