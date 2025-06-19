# Importierte Module (übersetzt)
from graphics_and_games_klassen import Ereignisbehandlung, Text
from figuren import *
import random

# Konstanten
FENSTERBREITE = 800
FENSTERHOEHE = 600
SCHRUMPF_DAUER = 100
MAX_LEBEN = 3
MAX_SCHRUMPFEN = 3

class Anzeige:
	def __init__(self):
		self.herzen = [herzFigur(25 + i * 30, 20, 50) for i in range(3)]
		self.schrumpf_icons = [schrumpfFigur(720 + i * 30, 20, 40) for i in range(3)]
		
		self.highscore_text = Text(10, 30, textgroesse=20, farbe="weiß", sichtbar=True)
		self.punktestand_text = Text(10, 60, textgroesse=20, farbe="weiß", sichtbar=True)
		
		self.anzeigeAktualisieren(0)

	def anzeigeAktualisieren(self, highscore, punkte=0, leben=3, schrumpfen=0):
		self.highscore_text.TextSetzen(f"Highscore: {highscore}")
		self.punktestand_text.TextSetzen(f"Punkte: {punkte}")
		
		for i in range(3):
			self.schrumpf_icons[i].SichtbarkeitSetzen(i < schrumpfen)
			
		for i in range(3):
			self.herzen[i].SichtbarkeitSetzen(i < leben)

class Feuerball(feuerballFigur):
	def __init__(self, seite, spielerX, spielerY):
		x, y, winkel = self.startDaten(seite, spielerX, spielerY)
		super().__init__(x, y, 80, winkel)
		self.geschwindigkeit = 2

	def startDaten(self, seite, spielerX, spielerY):
		if seite == "links":
			return -80, random.choice([random.randint(15, FENSTERHOEHE-15), spielerY]), 0
		elif seite == "rechts":
			return FENSTERBREITE+80, random.choice([random.randint(15, FENSTERHOEHE-15), spielerY]), 180
		elif seite == "oben":
			return random.choice([random.randint(15, FENSTERBREITE-15), spielerX]), -80, 270
		else:  # unten
			return random.choice([random.randint(15, FENSTERBREITE-15), spielerX]), FENSTERHOEHE+80, 90

	def aktualisieren(self):
		self.Gehen(self.geschwindigkeit)

class PlusPowerup(plusFigur):
	def __init__(self):
		super().__init__(random.randint(50, FENSTERBREITE - 50), random.randint(50, FENSTERHOEHE - 50), 80)

class HerzPowerup(herzFigur):
	def __init__(self):
		super().__init__(random.randint(50, FENSTERBREITE - 50), random.randint(50, FENSTERHOEHE - 50), 80)

class SchrumpfPowerup(schrumpfFigur):
	def __init__(self):
		super().__init__(random.randint(50, FENSTERBREITE - 50), random.randint(50, FENSTERHOEHE - 50), 80)

class Spieler(spielerFigur):
	def __init__(self):
		super().__init__(FENSTERBREITE//2, FENSTERHOEHE//2, 80)
		self.zuruecksetzen()

	def zuruecksetzen(self):
		self.leben = MAX_LEBEN
		self.schrumpfen = 0
		self.punkte = 0
		self.ist_geschrumpft = False
		self.schrumpf_timer = 0
		self.geschwindigkeit = 2
		self.GroesseSetzen(80)
		self.PositionSetzen(FENSTERBREITE//2, FENSTERHOEHE//2)

	def schrumpfen_ausloesen(self):
		if self.schrumpfen > 0 and not self.ist_geschrumpft:
			self.GroesseSetzen(40)
			self.ist_geschrumpft = True
			self.schrumpf_timer = SCHRUMPF_DAUER
			self.schrumpfen -= 1

	def aktualisieren(self):
		if self.ist_geschrumpft:
			self.schrumpf_timer -= 1
			if self.schrumpf_timer <= 0:
				self.ist_geschrumpft = False
				self.GroesseSetzen(80)
		self.punkte += 1

class Spiel(Ereignisbehandlung):
	def __init__(self):
		super().__init__()
		self.overlay = Anzeige()
		self.spieler = Spieler()
		self.feuerbaelle = []
		self.powerups = []
		self.takt = 0
		self.highscore = 0
		self.tasten_status = {"a": False, "d": False, "w": False, "s": False}

	def feuerball_spawnen(self):
		for seite in ["links", "rechts", "oben", "unten"]:
			self.feuerbaelle.append(Feuerball(seite, self.spieler.x, self.spieler.y))

	def powerup_spawnen(self):
		typ = random.choice(["plus", "herz", "schrumpfen"])
		if typ == "plus":
			self.powerups.append(PlusPowerup())
		elif typ == "herz":
			self.powerups.append(HerzPowerup())
		else:
			self.powerups.append(SchrumpfPowerup())

	def spiel_zuruecksetzen(self):
		if self.spieler.punkte > self.highscore:
			self.highscore = self.spieler.punkte

		self.overlay.anzeigeAktualisieren(self.highscore)

		for fb in self.feuerbaelle:
			fb.Entfernen()

		for pu in self.powerups:
			pu.Entfernen()
			
		self.feuerbaelle = []
		self.powerups = []
		self.spieler.zuruecksetzen()

	def AktionAusfuehren(self):
		self.takt += 1
		self.spieler.aktualisieren()

		# Bewegung
		dx = dy = 0
		if self.tasten_status["w"]: dy -= self.spieler.geschwindigkeit
		if self.tasten_status["s"]: dy += self.spieler.geschwindigkeit
		if self.tasten_status["a"]: dx -= self.spieler.geschwindigkeit
		if self.tasten_status["d"]: dx += self.spieler.geschwindigkeit

		# Spieler im Fenster halten
		min_x = self.spieler.groesse * 0.4
		max_x = FENSTERBREITE - self.spieler.groesse * 0.4
		min_y = self.spieler.groesse * 0.3
		max_y = FENSTERHOEHE - self.spieler.groesse * 0.3

		neu_x = max(min_x, min(self.spieler.x + dx, max_x))
		neu_y = max(min_y, min(self.spieler.y + dy, max_y))
		self.spieler.PositionSetzen(neu_x, neu_y)

		if self.takt % 120 == 0:
			self.feuerball_spawnen()
			
		if random.randint(1, 1000) == 1 and len(self.powerups) < 3:
			self.powerup_spawnen()

		for fb in self.feuerbaelle[:]:
			fb.aktualisieren()
			if self.spieler.BeruehrtObjekt(fb):
				fb.Entfernen()
				self.feuerbaelle.remove(fb)
				self.spieler.leben -= 1
				if self.spieler.leben <= 0:
					self.spiel_zuruecksetzen()
					return
			if fb.x < -80 or fb.x > 880 or fb.y < -80 or fb.y > 680:
				fb.Entfernen()
				self.feuerbaelle.remove(fb)

		for pu in self.powerups[:]:
			if self.spieler.BeruehrtObjekt(pu):
				if isinstance(pu, PlusPowerup):
					self.spieler.punkte += 100
				elif isinstance(pu, HerzPowerup) and self.spieler.leben < MAX_LEBEN:
					self.spieler.leben += 1
				elif isinstance(pu, SchrumpfPowerup) and self.spieler.schrumpfen < MAX_SCHRUMPFEN:
					self.spieler.schrumpfen += 1
				pu.Entfernen()
				self.powerups.remove(pu)

		self.overlay.anzeigeAktualisieren(self.highscore, self.spieler.punkte, self.spieler.leben, self.spieler.schrumpfen)

	def TasteGedrueckt(self, taste):
		if taste in self.tasten_status:
			self.tasten_status[taste] = True
		elif taste == "space":
			self.spieler.schrumpfen_ausloesen()

	def TasteLosgelassen(self, taste):
		if taste in self.tasten_status:
			self.tasten_status[taste] = False

if __name__ == "__main__":
	spiel = Spiel()
	spiel.TaktdauerSetzen(100/60)
	spiel.Starten()