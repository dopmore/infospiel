from figuren import SpielFigur

class Spielerlogik:
  def __init__(self):
    self.spieler = SpielFigur(0, 0, 80)
    self.speed = 2
    self.leben = 3

    self.SpielerZuruecksetzen()

  def SpielerZuruecksetzen(self):
    self.leben = 3
    self.shrinks = 0
    self.schrunpfenCooldown = 0
    self,schrumpfenTimer = 0
    self.spieler.GroesseSetzen(80)
    self.spieler.PositionSetzen(400, 300)

  def spielerLogik(self, tastenStatus):
      self._bewegen(tastenStatus)
      self.schrumpfenlogik()

  def _bewegen(self, tastenStatus):
    dx = dy = 0
    if tastenStatus["w"]: dy -= self.speed
    if tastenStatus["s"]: dy += self.speed
    if tastenStatus["a"]: dx -= self.speed
    if tastenStatus["d"]: dx += self.speed

    # Spieler im Zeichenfester halten
    min_x = self.spieler.groesse * 0.4
    max_x = 800 - self.spieler.groesse * 0.4
    min_y = self.spieler.groesse * 0.3
    max_y = 600 - self.spieler.groesse * 0.3

    new_x = max(min_x, min(self.spieler.x + dx, max_x))
    new_y = max(min_y, min(self.spieler.y + dy, max_y))

    self.spieler.PositionSetzen(new_x, new_y)

  def _schrumpfen(self, tastenStatus):
    if tastenStatus["space"] and self.schrunpfenCooldown == 0 and self.shrinks > 0:
        print("Schrumpfen aktiviert!")
        self.shrinks -= 1
        self.spieler.GroesseSetzen(40)
        self.schrumpfenTimer = 1800  # 1.5 seconds
        self.schrunpfenCooldown = 600  # prevent immediate reuse

  def schrumpfenlogik(self, tastenStatus):
      self.schrumpfen(tastenStatus)
      self.update_shrink_icons()

      if self.schrumpfenTimer > 0:
          self.schrumpfenTimer -= 1
          if self.schrumpfenTimer == 0:
              self.spieler.GroesseSetzen(self.spieler.originalGroesse)

      if self.schrunpfenCooldown > 0:
          self.schrunpfenCooldown -= 1
