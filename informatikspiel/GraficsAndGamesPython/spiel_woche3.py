from graphics_and_games_klassen import Ereignisbehandlung
from figuren import spielerFigur, feuerballFigur

### Woche 3: Verbesserte Spielerbewegung und Kollisionen

FENSTERBREITE = 800
FENSTERHOEHE = 600

class Spieler(spielerFigur):
    def __init__(self):
        super().__init__(FENSTERBREITE//2, FENSTERHOEHE//2, 80)
        self.geschwindigkeit = 1  # Geschwindigkeit des Spielers
    
class Spiel(Ereignisbehandlung):
    def __init__(self):
        super().__init__()
        self.spieler = Spieler()
        self.TaktdauerSetzen(100 / 60)  # 60 FPS
        self.tasten_status = {taste: False for taste in ["w", "a", "s", "d"]} # Tastenzustände initialisieren
        self.feuerball = feuerballFigur(50, 50, 80, 0)  # Initialisiert einen Feuerball außerhalb des Fensters

    def TasteGedrueckt(self, taste):
        if taste in self.tasten_status:
            self.tasten_status[taste] = True

    def TasteLosgelassen(self, taste): # Klasse in graphics_and_games_klassen neu implementiert
        if taste in self.tasten_status:
            self.tasten_status[taste] = False
        

    def AktionAusfuehren(self):
        dx = dy = 0 # bewegegunsänderung in x und y Richtung
        if self.tasten_status["w"]: dy -= self.spieler.geschwindigkeit
        if self.tasten_status["s"]: dy += self.spieler.geschwindigkeit
        if self.tasten_status["a"]: dx -= self.spieler.geschwindigkeit
        if self.tasten_status["d"]: dx += self.spieler.geschwindigkeit

        # Spieler im Fenster halten, 
        min_x = self.spieler.groesse * 0.4 # sozusagen 4 pixel der Spielergröße
        max_x = FENSTERBREITE - self.spieler.groesse * 0.4

        min_y = self.spieler.groesse * 0.3
        max_y = FENSTERHOEHE - self.spieler.groesse * 0.3

        neu_x = max(min_x, min(self.spieler.x + dx, max_x)) # ermöglicht nur Positionen innerhab des Fensters
        neu_y = max(min_y, min(self.spieler.y + dy, max_y))
        self.spieler.PositionSetzen(neu_x, neu_y)

        if self.spieler.BeruehrtObjekt(self.feuerball):
            print("Kollision erkannt!")
            self.feuerball.Gehen(250)
            self.feuerball.Drehen(-90) 

if __name__ == "__main__":
    spiel = Spiel()
    spiel.Starten()  # Startet das Spiel
   