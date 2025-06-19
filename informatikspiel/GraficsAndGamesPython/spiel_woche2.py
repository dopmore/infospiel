from graphics_and_games_klassen import Ereignisbehandlung
from figuren import spielerFigur

### Woche 2: Spieler und Bewegung

class Spiel(Ereignisbehandlung):
    def __init__(self):
        super().__init__()
        self.spieler = spielerFigur(x=500, y=300, groesse=80)
        self.TaktdauerSetzen(100 / 60)  # 60 FPS
        self.tasten_status = {taste: False for taste in ["w", "a", "s", "d"]} # Tastenzustände initialisieren

    def TasteGedrueckt(self, taste):
        for t in self.tasten_status.keys():
            self.tasten_status[t] = False  # Alle Tasten zurücksetzen
        if taste in self.tasten_status:
            self.tasten_status[taste] = True # neuste Taste gedrückt
        

    def AktionAusfuehren(self):
        if self.tasten_status["w"]: self.spieler.PositionSetzen(self.spieler.x, self.spieler.y - 1)
        if self.tasten_status["s"]: self.spieler.PositionSetzen(self.spieler.x, self.spieler.y + 1)
        if self.tasten_status["a"]: self.spieler.PositionSetzen(self.spieler.x - 1, self.spieler.y)
        if self.tasten_status["d"]: self.spieler.PositionSetzen(self.spieler.x + 1, self.spieler.y)
        
        # spieler sollte diagonal laufen / stehen bleiben können, und innerhalb des Fensters bleiben

if __name__ == "__main__":
    spiel = Spiel()
    spiel.Starten()  # Startet das Spiel
   