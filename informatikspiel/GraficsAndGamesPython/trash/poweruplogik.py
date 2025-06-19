from figuren import Herz, Plus, ShrinkPowerup
from random import randint, choice

class Poweruplogik:
    def __init__(self, spieler):
        self.powerups = []
        self.spieler = spieler  # Spielerobjekt, das die Powerups beeinflusst
        
    def PowerupsZuruecksetzen(self):
        for powerup in self.powerups:
            powerup.Entfernen()

        self.powerups.clear()

    def spawn_powerups(self):
      if randint(1, 10) == 1 and len(self.powerups) < 3:
          art = choice(["Plus", "Shrink", "Heart"])
          x, y = randint(15, 785), randint(15, 585)
          if art == "Shrink":
              self.powerups.append(ShrinkPowerup(x, y, 80))
          elif art == "Plus":
              self.powerups.append(Plus(x, y, 80))
          elif art == "Heart":
              self.powerups.append(Herz(x, y, 80))

    def check_powerup_collisions(self):
        kollisionsErgebnis, powerup = self.spieler.kollision(self.powerups)

        if kollisionsErgebnis:
            if isinstance(powerup, Plus):
                scoreincrease = 1000
            elif isinstance(powerup, ShrinkPowerup) and self.spieler.shrinks < 3:
                self.spieler.shrinks += 1
            elif isinstance(powerup, Herz) and self.spieler.leben < 3:
                self.spieler.leben += 1

            powerup.Entfernen()
            self.powerups.remove(powerup)
            return scoreincrease

    def poweruplogik(self):
        self.spawn_powerups()
            
            