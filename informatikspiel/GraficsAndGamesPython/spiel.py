from graphics_and_games_klassen import Ereignisbehandlung, Text
from figuren import *
import random

FENSTERBREITE = 800
FENSTERHOEHE = 600

class Anzeige:
	def __init__(self):
		self.herzenAnzeige = [herzFigur(25 + i * 30, 20, 50) for i in range(3)]
		self.schrumpfPowerupAnzeige = [schrumpfFigur(720 + i * 30, 20, 40) for i in range(3)]
		
		self.highscoreText = Text(10, 30, textgroesse=25)
		self.scoreText = Text(10, 60, textgroesse=25)
		
		self.anzeigeAktualisieren()

	def anzeigeAktualisieren(self, highscore=0, punkte=0, leben=3, schrumpfen=0):
		self.highscoreText.TextSetzen(f"Highscore: {highscore}")
		self.scoreText.TextSetzen(f"Score: {punkte}")
		
		for i in range(3):
			self.schrumpfPowerupAnzeige[i].SichtbarkeitSetzen(i < schrumpfen) # Für leben = 2 : 0 < 2 -> True; 1 < 2 -> True; 2 < 2 -> False 
			self.herzenAnzeige[i].SichtbarkeitSetzen(i < leben)

class Feuerball(feuerballFigur):
	def __init__(self, seite, spielerX, spielerY):
		x, y, winkel = self.startPositionErmitteln(seite, spielerX, spielerY)
		super().__init__(x, y, 80, winkel)
		self.geschwindigkeit = 2

	def startPositionErmitteln(self, seite, spielerX, spielerY):
		if seite == "links":
			return -80, random.choice([random.randint(15, FENSTERHOEHE-15), spielerY]), 0 # zufällige Y-Koordinate oder die Y-Koordinate des Spielers
		elif seite == "rechts":
			return FENSTERBREITE+80, random.choice([random.randint(15, FENSTERHOEHE-15), spielerY]), 180
		elif seite == "oben":
			return random.choice([random.randint(15, FENSTERBREITE-15), spielerX]), -80, 270
		else:  # unten
			return random.choice([random.randint(15, FENSTERBREITE-15), spielerX]), FENSTERHOEHE+80, 90

	def aktualisieren(self):
		self.Gehen(self.geschwindigkeit)

class Spieler(spielerFigur):
	def __init__(self):
		super().__init__(FENSTERBREITE//2, FENSTERHOEHE//2, 80)
		self.zuruecksetzen()

	def zuruecksetzen(self):
		self.leben = 3
		self.schrumpfen = 0
		self.punkte = 0
		self.ist_geschrumpft = False
		self.schrumpf_timer = 0
		self.geschwindigkeit = 2
		self.GroesseSetzen(80)
		self.PositionSetzen(FENSTERBREITE//2, FENSTERHOEHE//2)

	def schrumpfenAusloesen(self):
		if self.schrumpfen > 0 and not self.ist_geschrumpft:
			self.GroesseSetzen(40)
			self.ist_geschrumpft = True
			self.schrumpf_timer = 500
			self.schrumpfen -= 1

	def aktualisieren(self, dx, dy):
		# Spieler im Fenster halten
		minX = self.groesse * 0.4 # Experimentel bestimmt
		maxX = FENSTERBREITE - self.groesse * 0.4
		minY = self.groesse * 0.3
		maxY = FENSTERHOEHE - self.groesse * 0.3

		neuX = max(minX, min(self.x + dx, maxX)) # Nimmt spieler position, wenn sie kleiner als maxX und groesser als minX ist
		neuY = max(minY, min(self.y + dy, maxY))
		self.PositionSetzen(neuX, neuY)

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
		self.tastenStatus = {"a": False, "d": False, "w": False, "s": False}

	def feuerbaelleErstellen(self):
		for seite in ["links", "rechts", "oben", "unten"]:
			self.feuerbaelle.append(Feuerball(seite, self.spieler.x, self.spieler.y))

	def powerupErstellen(self):
		x,y = random.randint(50, FENSTERBREITE - 50), random.randint(50, FENSTERHOEHE - 50)
		typ = random.choice(["plus", "herz", "schrumpfen"])

		if typ == "plus":
			self.powerups.append(plusFigur(x, y, groesse=80))
		elif typ == "herz":
			self.powerups.append(herzFigur(x, y, groesse=80))
		else: # typ == "schrumpfen"
			self.powerups.append(schrumpfFigur(x, y, groesse=80))

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

		dx = dy = 0 # delta X/Y zurücksetzen
		if self.tastenStatus["w"]: dy -= self.spieler.geschwindigkeit
		if self.tastenStatus["a"]: dx -= self.spieler.geschwindigkeit
		if self.tastenStatus["s"]: dy += self.spieler.geschwindigkeit
		if self.tastenStatus["d"]: dx += self.spieler.geschwindigkeit

		self.spieler.aktualisieren(dx, dy)
		
		if self.takt % 120 == 0: # Alle 120 Takte 
			self.feuerbaelleErstellen()
			
		if len(self.powerups) < 3 and random.randint(1, 100)==1: # Jeden Takt 0,1% Chance, 
			self.powerupErstellen()

		for fb in self.feuerbaelle:
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

		for pu in self.powerups:
			if self.spieler.BeruehrtObjekt(pu):
				if isinstance(pu, herzFigur) and self.spieler.leben < 3:
					self.spieler.leben += 1
				elif isinstance(pu, schrumpfFigur) and self.spieler.schrumpfen < 3:
					self.spieler.schrumpfen += 1
				else:
					self.spieler.punkte += 1000
				pu.Entfernen()
				self.powerups.remove(pu)

		self.overlay.anzeigeAktualisieren(self.highscore, self.spieler.punkte, self.spieler.leben, self.spieler.schrumpfen)

	def TasteGedrueckt(self, taste):
		if taste in self.tastenStatus:
			self.tastenStatus[taste] = True

		elif taste == "space":
			self.spieler.schrumpfenAusloesen()

	def TasteLosgelassen(self, taste): # Neu implemetiert um Bewegung mit stoppen zu ermöglichen, wenn keine Taste gedrückt ist
		if taste in self.tastenStatus:
			self.tastenStatus[taste] = False


if __name__ == "__main__":
	spiel = Spiel()
	spiel.TaktdauerSetzen(100/60) # 60fps
	spiel.Starten()