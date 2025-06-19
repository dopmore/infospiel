from figuren import feuerball
from random import randint, choice

class Feuerballlogik:

  def __init__(self, spieler):
    self.spieler = spieler # Spielerobjekt, das die Feuerbaelle beeinflusst

    self.feuerbaelle = []
    self.welleInterval = 120  # Zeit in Takten bis zur nächsten Welle

    self.FeuerbaelleZuruecksetzen()

  def FeuerbaelleZuruecksetzen(self):
    self.welleTimer = 0

    for f in self.feuerbaelle:
            f.Entfernen()
    self.feuerbaelle.clear()
      
  def feuerballlogik(self):
    kollisionErgebnis, feuerball = self.spieler.kollision(self.feuerbaelle)

    if kollisionErgebnis:
        feuerball.Entfernen()
        self.feuerbaelle.remove(feuerball)
        self.spieler.leben -= 1
        if self.spieler.leben <= 0:
            print("Game Over! All hearts lost.")
            return True

    self.feuerbaellebewegen()

    self.welleTimer += 1
    if self.welleTimer >= int(self.welleInterval):
        self.welleTimer = 0
        self.welleErschaffen()

  def welleErschaffen(self):
      size = 80

      seiten = [ # oben, unten, links, rechts
          (choice([randint(15, 785), self.spieler.x]), -size, 80, 270),
          (choice([randint(15, 785), self.spieler.x]), 600 + size, 80, 90),
          (-size, choice([randint(15, 585), self.spieler.y]), 80, 0),
          (800 + size, choice([randint(15, 585), self.spieler.y]), 80 ,180)
      ]
      
      for f in seiten:
          self.feuerbaelle.append(feuerball(*f))

  def feuerbaellebewegen(self):
      for feuerball in self.feuerbaelle:
          feuerball.Gehen(feuerball.speed)

          if not (-100 <= feuerball.x <= 1000 and -100 <= feuerball.y <= 700):
              feuerball.Entfernen()
              self.feuerbaelle.remove(feuerball) # Feuerbaelle ausserhalb entfernen 