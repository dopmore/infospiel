from graphics_and_games_klassen import Ereignisbehandlung

from infospiel.informatikspiel.GraficsAndGamesPython.trash.anzeige import Anzeige
from figuren import *
from feuerballlogik import Feuerballlogik
from poweruplogik import Poweruplogik

class Spiel(Ereignisbehandlung):
    def __init__(self):      
        super().__init__()
        self.spieler = Spieler(500, 300, 80)
        self.anzeige = Anzeige()
        self.feuerballlogik = Feuerballlogik(self.spieler)
        self.poweruplogik = Poweruplogik(self.spieler)

        self.tasten_status = {t: False for t in ["w", "a", "s", "d", "q", "e", "space"]}
        self.TaktdauerSetzen(100 / 60)

        self.Spielzuruecksetzen()

    def Spielzuruecksetzen(self):
        self.anzeige.Zuruecksetzen()
        self.feuerballlogik.FeuerbaelleZuruecksetzen()
        self.spieler.Zuruecksetzen()
        self.poweruplogik.PowerupsZuruecksetzen()


    def TasteGedrueckt(self, taste):
        if taste in self.tasten_status:
            self.tasten_status[taste] = True
        if taste == "escape":
            self.Anhalten()

    def TasteLosgelassen(self, taste):
        if taste in self.tasten_status:
            self.tasten_status[taste] = False

    def AktionAusfuehren(self):        
        self.poweruplogik.poweruplogik()
        if self.feuerballlogik.feuerballlogik():
            self.Spielzuruecksetzen()
        self.anzeige.update_herzen(self.spieler.leben)
        self.anzeige.update_shrink_icons(self.spieler.shrinks)
        self.spieler.spielerlogik(self.tasten_status)
        self.anzeige.scoreErhoehen(self.poweruplogik.check_powerup_collisions() or 1)



if __name__ == "__main__":
    spiel = Spiel()
    spiel.Starten()