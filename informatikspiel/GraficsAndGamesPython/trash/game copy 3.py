from graphics_and_games_klassen import Ereignisbehandlung, Text
from poweruplogik import Poweruplogik
from feuerballlogik import Feuerballlogik
from infospiel.informatikspiel.GraficsAndGamesPython.trash.spielerlogik import Spielerlogik
from figuren import Herz, ShrinkPowerup # Icons

class Spiel(Ereignisbehandlung):
    def __init__(self):      
        super().__init__()
        self.powerupsLogik = Poweruplogik(self)
        self.feuerballLogik = Feuerballlogik(self)
        self.spielerLogik = Spielerlogik(self)

        self.herzIcons = [Herz(25 + i * 30, 20, 50) for i in range(3)]

        self.shrinkIcons = [ShrinkPowerup(720 + i * 30, 20, 40) for i in range(3)]

        self.tasten_status = {t: False for t in ["w", "a", "s", "d", "q", "e", "space"]}
        self.TaktdauerSetzen(100 / 60)

        self.score = 0
        self.highscore = 0

        self.highscore_text = Text(x=10, y=30, textgroesse=20, farbe="weiß", sichtbar=True)
        self.highscore_text.TextSetzen("Highscore: 0")

        self.score_text = Text(x=10, y=60, textgroesse=20, farbe="weiß", sichtbar=True)


        self.Spielzuruecksetzen()

    def Spielzuruecksetzen(self):
        self.spielerLogik.SpielerZuruecksetzen()
        self.powerupsLogik.PowerupsZuruecksetzen()
        self.feuerballLogik.FeuerbaelleZuruecksetzen()


        if self.score > self.highscore:
            self.highscore = self.score
            self.highscore_text.TextSetzen(f"Highscore: {self.highscore}")

        self.score = 0
        self.score_text.TextSetzen("Score: 0")

        for herz in self.herzIcons:
            herz.SichtbarkeitSetzen(True)

    def TasteGedrueckt(self, taste):
        if taste in self.tasten_status:
            self.tasten_status[taste] = True
        if taste == "escape":
            self.Anhalten()

    def TasteLosgelassen(self, taste):
        if taste in self.tasten_status:
            self.tasten_status[taste] = False

    def update_shrink_icons(self):
        for i in range(3):
            self.shrinkIcons[i].SichtbarkeitSetzen(i < self.shrinks)


    def scorelogik(self):
        self.score += 1
        self.score_text.TextSetzen(f"Score: {self.score}")

    def AktionAusfuehren(self):        
        self.scorelogik()



if __name__ == "__main__":
    spiel = Spiel()
    spiel.Starten()