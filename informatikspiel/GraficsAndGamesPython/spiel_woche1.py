from graphics_and_games_klassen import Zeichenfenster, Figur

### Woche 1: Fenster und Test Figur erstellen

if __name__ == "__main__":
    # Fenster = Zeichenfenster() # wird automatisch erstellt
    figur = Figur(x=100, y=100, groesse=50, sichtbar=True)
    figur.FigurteilFestlegenRechteck(-25, -25, 50, 50, "blau") # Spieler zeichnet Richard bis nächste Stunde
   