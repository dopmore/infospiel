from graphics_and_games_klassen import Text
from figuren import Herz, ShrinkPowerup

class Anzeige:
    def __init__(self):
        self.herzen = [Herz(25 + i * 30, 20, 50) for i in range(3)]
        self.shrink_icons = [ShrinkPowerup(720 + i * 30, 20, 40) for i in range(3)]

        self.highscore_text = Text(x=10, y=30, textgroesse=20, farbe="weiß", sichtbar=True)
        self.score_text = Text(x=10, y=60, textgroesse=20, farbe="weiß", sichtbar=True)

        self.anzeigeAktualisieren(0)

    def anzeigeAktualisieren(self, highscore, score=0, leben=3, shrinks=0, ):
        self.highscore_text.TextSetzen(f"Highscore: {highscore}")
        self.score_text.TextSetzen(f"Score: {score}")
        for i in range(3):
            self.shrink_icons[i].SichtbarkeitSetzen(i < shrinks)
        for i in range(3):
            self.herzen[i].SichtbarkeitSetzen(i < leben)

if __name__ == "__main__":
    # Anzeige Testen
    anzeige = Anzeige()


