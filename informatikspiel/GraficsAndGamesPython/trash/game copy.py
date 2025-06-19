from graphics_and_games_klassen import *
from random import randint, choice

class Spieler(Figur):
    def __init__(self, x, y, groesse):
        super().__init__(x=x, y=y, groesse=groesse, sichtbar=True)
        self.original_groesse = groesse

        # Körperteile
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

class Enemy(Figur):
    def __init__(self):
        super().__init__(x=0, y=0, groesse=80, sichtbar=False)
        self.aktiv = False
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
        self.Drehen(180)

    def reaktivieren(self, x, y, groesse):
        self.PositionSetzen(x, y)
        self.GroesseSetzen(groesse)
        self.SichtbarkeitSetzen(True)
        self.aktiv = True

    def deaktivieren(self):
        self.SichtbarkeitSetzen(False)
        self.aktiv = False

class Spiel(Ereignisbehandlung):
    def __init__(self):
        super().__init__()
        self.p1 = Spieler(50, 300, 80)
        self.feuerbaelle = []
        self.enemy_pool = []

        self.muster_matrix = self.muster_matrix = [
            # Phase 1 – Einführung (leicht)
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,0,0],
            [0,0,0,1,0,0,0,0,0,0,0],
            [0,0,1,1,1,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [],

            # Phase 2 – gleichmäßiger Rhythmus
            [1,0,0,0,0,0,0,0,0,0,1],
            [0,1,0,0,0,0,0,0,0,1,0],
            [0,0,1,0,0,0,0,0,1,0,0],
            [0,0,0,1,0,0,0,1,0,0,0],
            [0,0,0,0,1,0,1,0,0,0,0],
            [0,0,0,1,0,0,0,1,0,0,0],
            [0,0,1,0,0,0,0,0,1,0,0],
            [],

            # Phase 3 – schnelle Folge
            [0,0,0,0,1,1,1,0,0,0,0],
            [0,1,0,1,0,1,0,1,0,1,0],
            [1,0,1,0,1,0,1,0,1,0,1],
            [0,1,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,1,0,0,0,0,0],
            [],

            # Phase 4 – Wellen und asymmetrisch
            [1,0,0,1,0,0,1,0,0,1,0],
            [0,1,0,0,1,0,0,1,0,0,1],
            [0,0,1,0,0,1,0,0,1,0,0],
            [1,1,0,0,0,0,0,0,0,1,1],
            [0,0,0,1,1,1,1,1,0,0,0],
            [],

            # Phase 5 – Musterpausen und Schockmuster
            [0,0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1], # volle Reihe
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,1,0,1,0,1,0,1,0,1,0],
            [1,0,1,0,1,0,1,0,1,0,1],
            [],

            # Phase 6 – Chaos
            [1,0,1,1,0,1,1,0,1,1,1],
            [0,1,1,1,1,0,1,1,1,1,0],
            [1,0,1,0,1,0,1,0,1,0,1],
            [0,1,0,1,0,1,0,1,0,1,0],
            [1,1,1,1,0,0,0,1,1,1,1],
            [0,0,0,0,0,1,0,0,0,0,0],
            [],

            # Phase 7 – Rückgang und Überraschung
            [0,0,0,0,1,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,1,0,0,0],
            [0,1,0,0,0,0,0,0,1,0,0],
            [1,0,0,0,0,0,0,0,0,1,0],
            [0,0,0,0,0,0,0,0,0,0,1],
            [],

            # Phase 8 – Endphase
            [1,1,1,0,0,0,1,1,1,0,0],
            [0,0,1,1,1,0,0,1,1,1,0],
            [0,0,0,1,1,1,0,0,1,1,1],
            [0,0,0,0,1,1,1,0,0,1,1],
            [0,0,0,0,0,1,1,1,0,0,1],
            [0,0,0,0,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0],
            [0,0,0,0,0,0,0,0,1,1,1],
            [0,0,0,0,0,0,0,0,0,1,1],
            [0,0,0,0,0,0,0,0,0,0,1],
        ]

        self.muster_index = 0

        self.tasten_status = {t: False for t in ["w", "a", "s", "d", "q", "e", "space"]}
        self.TaktdauerSetzen(100 / 60)
        self.Spielzuruecksetzen()

    def get_enemy_from_pool(self):
        for enemy in self.enemy_pool:
            if not enemy.aktiv:
                return enemy
        enemy = Enemy()
        self.enemy_pool.append(enemy)
        return enemy

    def Spielzuruecksetzen(self):
        self.speed = 4
        self.feuerball_speed = 1
        self.welle_timer = 0
        self.welle_interval = 90
        self.schwierigkeit = 1
        self.schrumpfen_cooldown = 0
        self.schrumpfen_timer = 0
        self.muster_index = 0

        self.p1.PositionSetzen(50, 300)
        self.p1.GroesseSetzen(self.p1.original_groesse)

        for f in self.feuerbaelle:
            f.deaktivieren()
        self.feuerbaelle.clear()

    def TasteGedrueckt(self, taste):
        if taste in self.tasten_status:
            self.tasten_status[taste] = True
        if taste == "escape":
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

        min_x = p.groesse * 0.4
        max_x = 800 - p.groesse * 0.4
        min_y = p.groesse * 0.3
        max_y = 600 - p.groesse * 0.3

        new_x = max(min_x, min(p.x + dx, max_x))
        new_y = max(min_y, min(p.y + dy, max_y))

        p.PositionSetzen(new_x, new_y)

    def schrumpfen(self, p):
        if self.tasten_status["e"] and self.schrumpfen_cooldown == 0 and self.schrumpfen_timer == 0:
            p.GroesseSetzen(40)
            self.schrumpfen_timer = 180
            self.schrumpfen_cooldown = 600

    def feuerbaellebewegen(self):
        for f in self.feuerbaelle:
            f.Gehen(self.feuerball_speed)
            if f.x < 100:
                f.deaktivieren()
        self.feuerbaelle = [f for f in self.feuerbaelle if f.aktiv]

    def welle_erschaffen(self):
        y_positionen = [y for y in range(27, 600, 50)]
        anzahl = min(randint(2, int(2 + self.schwierigkeit)), len(y_positionen))
        used_y = []

        for _ in range(anzahl):
            available = [y for y in y_positionen if y not in used_y]
            if not available:
                break
            y = choice(available)
            used_y.append(y)
            enemy = self.get_enemy_from_pool()
            enemy.reaktivieren(900, y, 80)
            self.feuerbaelle.append(enemy)

    def muster_welle_erschaffen(self):
        if self.muster_index >= len(self.muster_matrix):
            return  # Kein Muster mehr übrig

        muster_zeile = self.muster_matrix[self.muster_index]
        y_positionen = [y for y in range(15, 700, 57)]

        for idx, wert in enumerate(muster_zeile):
            if wert == 1 and idx < len(y_positionen):
                y = y_positionen[idx]
                enemy = self.get_enemy_from_pool()
                enemy.reaktivieren(900, y, 80)
                self.feuerbaelle.append(enemy)

        self.muster_index += 1

    def wellenlogik(self):
        self.welle_timer += 1
        if self.welle_timer >= self.welle_interval:
            self.welle_timer = 0
            self.schwierigkeit += 0.05
            if self.muster_index < len(self.muster_matrix):
                self.muster_welle_erschaffen()
            else:
                self.zufällige_welle_erschaffen()

    def collision(self, p, enemys):
        return any(p.BeruehrtObjekt(e) for e in enemys)

    def schrumpfenlogik(self, p):
        if self.schrumpfen_timer > 0:
            self.schrumpfen_timer -= 1
            if self.schrumpfen_timer == 0:
                p.GroesseSetzen(p.original_groesse)

        if self.schrumpfen_cooldown > 0:
            self.schrumpfen_cooldown -= 1

    def AktionAusfuehren(self):
        self.bewegen(self.p1)
        self.schrumpfen(self.p1)
        self.schrumpfenlogik(self.p1)
        self.feuerbaellebewegen()
        self.wellenlogik()

        if self.collision(self.p1, self.feuerbaelle):
            self.Spielzuruecksetzen()
            print("Game Over! You were hit by a feuerball!")

if __name__ == "__main__":
    Spiel().Starten()
