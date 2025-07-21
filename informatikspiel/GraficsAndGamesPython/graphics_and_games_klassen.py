# -- coding: utf-8 --
"""
Created on Wed May  27 10:00:00 2020
@author: Klaus Reinold
"""

from intern.zeichenfenster import *
import time


class Dreieck:
    """
    Wrapperklasse zur Beschreibung von Objekten des Typs Dreieck
    """


    def __init__(self, x = 60, y = 10, winkel = 0, breite = 1001, hoehe = 100, farbe = "rot", sichtbar = True):
        """
        Die Initalisierungsmethode sorgt für die Anfangsbelegung der Attribute für Position und Aussehen.
        -- Parameter x anfängliche x-Position der Spitze (Standardwert: 60)
        -- Parameter y anfängliche y-Position der Spitze (Standardwert: 10)
        -- Parameter winkel anfänglicher Winkel (Standardwert: 0)
        -- Parameter breite anfängliche Breite des Objekts der Klasse Dreieck (Standardwert: 100)
        -- Parameter hoehe anfängliche Höhe des Objekts der Klasse Dreieck (Standardwert: 100)
        -- Parameter farbe anfängliche Farbe des Objekts der Klasse Dreieck (Standardwert: "rot")
        -- Parameter sichtbar anfängliche Sichtbarkeit (Standardwert: True)
        """

        Zeichenfenster()
        self.x = x
        # x-Position der Spitze

        self.y = y
        # y-Position der Spitze

        self.winkel = winkel
        # Winkel

        self.breite = breite
        # Breite des Dreiecks

        self.hoehe = hoehe
        # Höhe des Dreiecks

        self.farbe = farbe
        # Farbe des Dreiecks

        self.sichtbar = sichtbar
        # Sichtbarkeit des Dreiecks (True oder False)

        self.symbol = DreieckIntern(self.farbe, self.x, self.y, self.breite, self.hoehe, self.winkel, self.sichtbar)
        # Referenz auf das Dreieckssymbol

    def PositionSetzen(self, x, y):
        """
        Setzt die Position (der Spitze) des Dreiecks.
        -- Parameter x x-Position der Spitze
        -- Parameter y y-Position der Spitze
        """
        self.x = x
        self.y = y
        self.symbol.PositionSetzen(self.x - self.breite/2, self.y)


    def Verschieben(self, deltaX, deltaY):
        """
         Verschiebt das Dreieck um die angegebenen Werte.
        -- Parameter deltaX Verschiebung in x-Richtung
        -- Parameter deltaY Verschiebung in y-Richtung
        """
        self.x += deltaX
        self.y += deltaY
        self.symbol.PositionSetzen(self.x - self.breite/2, self.y)


    def Drehen(self, grad):
        """
         Dreht das Dreieck.
        -- Parameter grad Drehwinkel (mathematisch positiver Drehsinn) im Gradmaß
        """
        self.winkel = (self.winkel+grad)%360
        self.symbol.WinkelSetzen(self.winkel)


    def WinkelSetzen(self, winkel):
        """
        Setzt den Drehwinkel des Dreiecks.
        Die Winkelangabe ist in Grad,positive Werte drehen gegen den Uhrzeigersinn, negative Werte drehen im Uhrzeigersinn (mathematisch positiver Drehsinn).
        -- Parameter winkel der (neue) Drehwinkel des Dreiecks

        """
        self.winkel = winkel%360
        self.symbol.WinkelSetzen(self.winkel)


    def GroesseSetzen (self, breite, hoehe):
        """
        Setzt die Größe des Dreiecks.
        -- Parameter breite (neue) Breite
        -- Parameter hoehe (neue) Höhe
        """
        self.breite = breite
        self.hoehe = hoehe
        self.symbol.GroesseSetzen(self.breite, self.hoehe)
        self.symbol.PositionSetzen(self.x - self.breite/2, self.y)


    def FarbeSetzen(self, farbe):
        """
        Setzt die Farbe des Dreiecks.
        Erlaubte Farben sind:
        "weiß", "weiss", "rot", "grün", "gruen", "blau", "gelb", "magenta", "cyan", "hellgelb", "hellgrün", "hellgruen","orange", "braun", "grau", "schwarz", "transparent"
        Außerdem sind rgb-Farbwerte erlaubt in der Form (r, g, b), die Zahlen jeweils aus dem Bereich 0.255
        -- Parameter farbe (neue) Farbe

        """
        self.farbe = farbe
        self.symbol.FarbeSetzen(self.farbe)



    def SichtbarkeitSetzen(self, sichtbar):
        """
        Schaltet die Sichtbarkeit des Dreiecks ein oder aus.
        Erlaubte Parameterwerte: true, false
        -- Parameter sichtbar (neue) Sichtbarkeit des Dreiecks
        """
        self.sichtbar = sichtbar
        self.symbol.SichtbarkeitSetzen(self.sichtbar)


    def Entfernen(self):
        """
        Entfernt das Dreieck aus dem Zeichenfenster.
        """
        self.symbol.Entfernen()
        del self


    def NachVorneBringen(self):
        """
        Bringt das Dreieck eine Ebene nach vorn.
        """
        self.symbol.NachVorneBringen()


    def GanzNachVornBringen(self):
        """
        Bringt das Dreieck in die vorderste Ebene.
        """
        self.symbol.GanzNachVornBringen()


    def NachHintenBringen(self):
        """
        Bringt das Dreieck eine Ebene nach hinten.
        """
        self.symbol.NachHintenBringen()


    def GanzNachHintenBringen(self):
        """
        Bringt das Dreieck in die hinterste Ebene.
        """
        self.symbol.GanzNachHintenBringen()




class Ereignisbehandlung:
    """
    Klasse zur Beschreibung der Ereignisbehandlung (Taktimpulse, Mausklicks, Tastaturereignisse, die vom Zeichenfenster registriert wurden)
    """

    def __init__(self):
        """
        Der Konstruktor meldet das Objekt als Beobachter beim Zeichenfenster an.
        """
        self.zeichenfenster = Zeichenfenster()
        self.zeichenfenster.BeobachterRegistrieren(self)


    def AktionAusfuehren(self):
        """
        Aktionsmethode, die bei jedem Taktschlag ausgeführt wird.
        Muss bei Bedarf von einer Unterklasse überschrieben werden.
        """
        #print("Tick")
        pass


    def TasteGedrueckt(self, taste):
        """
        Aktionsmethode, die bei jedem Tastendruck ausgelöst wird.
        Muss bei Bedarf von einer Unterklasse überschrieben werden.
        -- Parameter taste gedrückte Taste
        """
        #print("Taste gedrückt: ", taste)
        pass

    def TasteLosgelassen(self, taste):
        """
        Aktionsmethode, die bei jedem Loslassen einer Taste ausgelöst wird.
        Muss bei Bedarf von einer Unterklasse überschrieben werden.
        -- Parameter taste losgelassene Taste
        """
        #print("Taste losgelassen: ", taste)
        pass


    def MausGeklickt(self, posX, posY, button):
        """
        Aktionsmethode, die bei jedem Mausklick ausgelöst wird.
        Muss bei Bedarf von einer Unterklasse überschrieben werden.
        -- Parameter posX Position des Mausklicks
        -- Parameter posY Position des Mausklicks
        -- Parameter button Maustaste (1-links, 2-Mausrad, 3-rechts, 4-Mausrad nach oben, 5-Mausrad nach unten)
        """
        #print("Maustaste: ", button, " an x-Position: ", posX, ", y-Position: ", posY)
        pass

    def Starten(self):
        """
        Methode zum Starten des Taktgebers
        """
        time.sleep(1)
        button = self.zeichenfenster.ButtonGeben()
        if not button is None:
            button.inBetriebsmodusWechseln()
        else:
            self.zeichenfenster.nichtGestoppt = True

    def Anhalten(self):
        """
        Methode zum Stoppen des Taktgebers
        """
        button = self.zeichenfenster.ButtonGeben()

        if not button is None:
            button.inStopmodusWechseln()


    def TaktdauerSetzen(self, ms):
        """
        Methode zum Setzen der Taktdauer
        -- Parameter ms Taktdauer in Millisekunden (Wertebereich 4 (schnell)..1000 (langsam))
        """
        schieberegler = self.zeichenfenster.SchieberGeben()
        time.sleep(1)
        if not schieberegler is None:
            if ms < 4:
                ms = 4
            if ms > 1000:
                ms = 1000
            schieberegler.WertSetzen(int(round(1000/ms)))
        self.zeichenfenster.FPS = int(round(1000/ms))



    def FensterNeuZeichnen(self):
        """
        Das gesamte Fenster wird neu gezeichnet.
        Dies passiert nach einem Durchlauf der Hauptroutine des Programms automatisch.
        Will man innerhalb einer Methode ein Neuzeichnen veranlassen (z. B. um nach Bewegung eines Objekts auf Berührung zu testen), so kann diese Methode ein Neuzeichnen zu anderer Zeit bewirken.
        """
        Zeichenfenster().FensterNeuZeichnen()



class Figur:
    """
    Wrapperklasse zur Beschreibung der Figur
    """

    def __init__(self, x = 100, y = 200, winkel = 0, groesse = 40, sichtbar = True):
        """
        Die Initalisierungsmethode sorgt für die Anfangsbelegung der Attribute für Position und Aussehen.
        -- Parameter x anfängliche x-Position der Mitte der Figur (Standardwert: 100)
        -- Parameter y anfängliche y-Position der Mitte der Figur (Standardwert: 200)
        -- Parameter winkel anfänglicher Winkel (Standardwert: 0)
        -- Parameter groesse anfängliche Größe des Objekts der Klasse Figur (Standardwert: 40)
        -- Parameter sichtbar anfängliche Sichtbarkeit  (Standardwert: True)
        """

        self.x = x
        # x-Position der Figurenmitte

        self.y = y
        # y-Position der Figurenmitte

        self.winkel = winkel
        # Drehwinkel (0<=winkel<=360)

        self.groesse = groesse
        # Größe der quadratischen Figur

        self.sichtbar = sichtbar
        # Sichtbarkeit der Figur (True oder False)

        self.symbol = FigurIntern(self.x, self.y, self.groesse, self.winkel, self.sichtbar)
        # Referenz auf das Symbol

        Zeichenfenster().BeobachterRegistrieren(self)


    def AktionAusfuehren(self):
        """
        Aktionsmethode, die bei jedem Taktschlag ausgeführt wird.
        Muss bei Bedarf in einer Unterklasse überschrieben werden.
        """
        pass


    def TasteGedrueckt(self, taste):
        """
        Aktionsmethode, die bei jedem Tastendruck ausgelöst wird.
        Muss bei Bedarf in einer Unterklasse überschrieben werden.
        -- Parameter taste gedrückte Taste
        """
        #print("Taste gedrueckt: ", taste)
        pass

    def TasteLosgelassen(self, taste):
        """
        Aktionsmethode, die bei jedem Loslassen einer Taste ausgelöst wird.
        Muss bei Bedarf von einer Unterklasse überschrieben werden.
        -- Parameter taste losgelassene Taste
        """
        #print("Taste losgelassen: ", taste)
        pass


    def MausGeklickt(self, posX, posY, button):
        """
        Aktionsmethode, die bei jedem Mausklick ausgelöst wird.
        Muss bei Bedarf von einer Unterklasse überschrieben werden.
        -- Parameter posX Position des Mausklicks
        -- Parameter posY Position des Mausklicks
        -- Parameter button Maustaste (1-links, 2-Mausrad, 3-rechts, 4-Mausrad nach oben, 5-Mausrad nach unten)
        """
        #print("Maustaste: ", button, " an Position: ", posX, ", ", posY)
        pass


    def PositionSetzen(self, x, y):
        """
        Setzt die Position der Figur.
        -- Parameter x x-Position der Mitte der Figur
        -- Parameter y y-Position der Mitte der Figur
        """
        self.x = x
        self.y = y
        self.symbol.PositionSetzen(self.x, self.y)


    def Gehen(self,laenge):
        """
        Verschiebt die Figur in die Richtung ihres Winkels.
        -- Parameter laenge Anzahl der Längeneinheiten
        """
        self.symbol.Gehen(laenge)
        self.x = self.symbol.x
        self.y = self.symbol.y
        Zeichenfenster().FensterNeuZeichnen()


    def Drehen(self, grad):
        """
        Dreht die Figur
        -- Parameter grad Drehwinkel (mathematisch positiver Drehsinn) im Gradmass
        """
        self.winkel = (self.winkel+grad)%360
        self.symbol.WinkelSetzen(self.winkel)


    def WinkelSetzen(self, winkel):
        """
        Setzt den Drehwinkel der Figur.
        Die Winkelangabe ist in Grad, positive Werte drehen gegen den Uhrzeigersinn, negative Werte drehen im Uhrzeigersinn (mathematisch positiver Drehsinn). 0°: rechts; 90°: oben; 180°: links; 270° unten
        -- Parameter winkel der (neue) Drehwinkel der Figur
        """
        self.winkel = winkel%360
        self.symbol.WinkelSetzen(self.winkel)


    def GroesseSetzen (self, groesse):
        """
        Setzt die Größe der Figur.
        -- Parameter groesse Größe des umgebenden Quadrats
        """
        self.groesse = groesse
        self.symbol.GroesseSetzen(groesse)


    def SichtbarkeitSetzen(self, sichtbar):
        """
        Schaltet die Sichtbarkeit der Figur ein oder aus.
        Erlaubte Parameterwerte: true, false
        -- Parameter sichtbar (neue) Sichtbarkeit der Figur
        """
        self.sichtbar = sichtbar
        self.symbol.SichtbarkeitSetzen(self.sichtbar)


    def Entfernen(self):
        """
        Entfernt die Figur aus dem Zeichenfenster.
        """
        self.symbol.Entfernen()
        Zeichenfenster().BeobachterEntfernen(self)
        del self


    def NachVorneBringen(self):
        """
        Bringt die Figur eine Ebene nach vorn.
        """
        self.symbol.NachVorneBringen()


    def GanzNachVornBringen(self):
        """
        Bringt die Figur in die vorderste Ebene.
        """
        self.symbol.GanzNachVornBringen()


    def NachHintenBringen(self):
        """
        Bringt die Figur eine Ebene nach hinten.
        """
        self.symbol.NachHintenBringen()


    def GanzNachHintenBringen(self):
        """
        Bringt die Figur in die hinterste Ebene.
        """
        self.symbol.GanzNachHintenBringen()


    def ZumStartpunktGehen(self):
        """
        Bringt die Figur zu ihrem Startpunkt.
        """
        self.symbol.ZumStartpunktGehen()
        self.x = self.symbol.x
        self.y = self.symbol.y
        self.winkel = self.symbol.winkel


    def WinkelGeben(self):
        """
        Liefert den Winkel der Figur.
        -- return Winkel
        """
        return self.winkel


    def XPositionGeben(self):
        """
        Liefert die x-Position der Figur.
        -- return x-Position
        """
        return self.x


    def YPositionGeben(self):
        """
        Liefert die y-Position der Figur.
        -- return y-Position
        """
        return self.y


    def Beruehrt(self):
        """
        Testet, ob die Figur eine Grafik-Figur berührt.
        -- return true, wenn die Figur und eine Grafikfigur überlappen
        """
        return self.symbol.Beruehrt()


    def BeruehrtFarbe(self, farbe):
        """
        Testet, ob die Figur eine Objekt berührt, das die gegebene Farbe enthält.
        (die Farbe muss nicht unbedingt sichtbar oder direkt berührt werden)
        -- Parameter farbe Farbe, auf die getestet werden soll.
        -- return true wenn ein Objekt mit der Farbe berührt wird.
        """
        return self.symbol.BeruehrtFarbe(farbe)


    def BeruehrtObjekt(self, objekt):
        """
        Testet, ob die Figur eine Objekt berührt.
        -- Parameter objekt Objekt, mit dem eine Überschneidung geprüft werden soll.
        -- return true wenn das übergebene Objekt mit der Farbe berührt.
        """
        return self.symbol.BeruehrtObjekt(objekt)


    def FigurteilFestlegenRechteck(self, x, y, breite, hoehe, farbe):
        """
        Erzeugt ein neues, rechteckiges Element einer eigenen Darstellung der Figur.
        Alle Werte beziehen sich auf eine Figur der Größe 100x100 und den Koordinaten (0|0) in der Mitte des Quadrats
        -- Parameter x x-Wert der linken oberen Ecke des Rechtecks innerhalb der Figur (-50<=x<=50)
        -- Parameter y y-Wert der linken oberen Ecke des Rechtecks innerhalb der Figur (-50<=y<=50)
        -- Parameter breite Breite des Rechtecks innerhalb der Figur (0<=breite<=50-x)
        -- Parameter hoehe Höhe des Rechtecks innerhalb der Figur (0<=hoehe<=50-x)
        -- Parameter farbe Farbe des Figurelements
        """
        self.symbol.FigurteilFestlegenRechteck(x,y,breite, hoehe, farbe)


    def FigurteilFestlegenEllipse(self, x, y, breite, hoehe, farbe):
        """
        Erzeugt ein neues, elliptisches Element einer eigenen Darstellung der Figur.
        Alle Werte beziehen sich auf eine Figur der Größe 100x100 und den Koordinaten (0|0) in der Mitte des Quadrats
        -- Parameter x x-Wert der linken oberen Ecke des Rechtecks, das die Ellipse umgibt, innerhalb der Figur (-50<=x<=50)
        -- Parameter y y-Wert der linken oberen Ecke des Rechtecks, das die Ellipse umgibt, innerhalb der Figur (-50<=y<=50)
        -- Parameter breite Breite des Rechtecks, das die Ellipse umgibt, innerhalb der Figur (0<=breite<=50-x)
        -- Parameter hoehe Höhe des Rechtecks, das die Ellipse umgibt, innerhalb der Figur (0<=hoehe<=50-x)
        -- Parameter farbe Farbe des Figurelements
        """
        self.symbol.FigurteilFestlegenEllipse(x,y,breite, hoehe, farbe)


    def FigurteilFestlegenDreieck(self, x1, y1 ,x2, y2, x3, y3, farbe):
        """
        Erzeugt ein neues, dreieckiges Element einer eigenen Darstellung der Figur.
        Die Werte müssen passend zur Größe der Figur gewählt werden (Standardwert: 40)
        -- Parameter x1 x-Wert des ersten Punktes innerhalb der Figur (-50<=x1<=50)
        -- Parameter y1 y-Wert des ersten Punktes innerhalb der Figur (-50<=y1<=50)
        -- Parameter x2 x-Wert des zweiten Punktes innerhalb der Figur (-50<=x2<=50)
        -- Parameter y2 y-Wert des zweiten Punktes innerhalb der Figur (-50<=y2<=50)
        -- Parameter x3 x-Wert des dritten Punktes innerhalb der Figur (-50<=x3<=50)
        -- Parameter y3 y-Wert des dritten Punktes innerhalb der Figur (-50<=y3<=50)
        -- Parameter farbe Farbe des Figurelements
        """
        self.symbol.FigurteilFestlegenDreieck(x1, y1 ,x2, y2, x3, y3, farbe)


    def EigeneFigurLoeschen(self):
        """
        Setzt die Figur wieder auf die Standarddarstellung zurück
        """
        self.symbol.StandardfigurErzeugen()


    def Darstellen(self):
        """
        Stellt das Symbol neu dar.
        """
        self.symbol.Darstellen()


    def FensterNeuZeichnen(self):
        """
        Das gesamte Fenster wird neu gezeichnet.
        Dies passiert nach einem Durchlauf der Hauptroutine des Programms automatisch.
        Will man innerhalb einer Methode ein Neuzeichnen veranlassen (z. B. um nach Bewegung eines Objekts auf Berührung zu testen), so kann diese Methode ein Neuzeichnen zu anderer Zeit bewirken.
        """
        self.symbol.FensterNeuZeichnen()


class Kreis:
    """
     Wrapperklasse zur Beschreibung von Objekten der Klasse Kreis
    """

    def __init__(self, x = 60, y = 60, radius = 50, winkel = 0, farbe = "rot", sichtbar = True):
        """
        Die Initalisierungsmethode sorgt für die Anfangsbelegung der Attribute für Position und Aussehen.
        -- Parameter x anfängliche x-Position des Mittelpunkts (Standardwert: 60)
        -- Parameter y anfängliche y-Position des Mittelpunkts (Standardwert: 60)
        -- Parameter radius anfänglicher Radius des Kreises (Standardwert: 50)
        -- Parameter winkel anfänglicher Winkel (Standardwert: 0)
        -- Parameter farbe anfängliche Farbe Kreises (Standardwert: "rot")
        -- Parameter sichtbar anfängliche Sichtbarkeit (Standardwert: True)
        """
        self.x = x
        #x-Position des Mittelpunkts

        self.y = y
        #y-Position des Mittelpunkts

        self.radius = radius
        #Radius des Kreises

        self.winkel = winkel
        #Drehwinkel (0<=winkel<=360)

        self.farbe = farbe
        #Farbe des Kreises

        self.sichtbar = sichtbar
        #Sichtbarkeit des Kreises (True oder False)        """

        self.symbol = KreisIntern(self.farbe, self.x-self.radius, self.y-self.radius, self.radius, self.winkel, self.sichtbar)
        #Referenz auf das Rechteckssymbol

    def PositionSetzen(self, x, y):
        """
        Setzt die Position des Mittelpunktes.
        -- Parameter x x-Position des Mittelpunkts
        -- Parameter y y-Position des Mittelpunkts
        """
        self.x = x
        self.y = y
        self.symbol.PositionSetzen(self.x-self.radius, self.y-self.radius)


    def Verschieben(self, deltaX, deltaY):
        """
        Verschiebt den Kreis um die angegebenen Werte.
        -- Parameter deltaX Verschiebung in x-Richtung
        -- Parameter deltaY Verschiebung in y-Richtung
        """
        self.x += deltaX
        self.y += deltaY
        self.symbol.PositionSetzen(self.x-self.radius, self.y-self.radius)


    def Drehen(self, grad):
        """
        Dreht den Kreis.
        -- Parameter grad Drehwinkel (mathematisch positiver Drehsinn) im Gradmass
        """
        self.winkel = (self.winkel+grad)%360
        self.symbol.WinkelSetzen(self.winkel)


    def WinkelSetzen(self, winkel):
        """
        Setzt den Drehwinkel des Kreises.
        Die Winkelangabe ist in Grad,positive Werte drehen gegen den Uhrzeigersinn, negative Werte drehen im Uhrzeigersinn (mathematisch positiver Drehsinn).
        -- Parameter winkel der (neue) Drehwinkel des Kreises
        """
        self.winkel = winkel%360
        self.symbol.WinkelSetzen(self.winkel)


    def RadiusSetzen (self, radius):
        """
        Setzt den Radius des Kreises.
        -- Parameter radius (neuer) Radius
        """
        self.radius = radius
        self.symbol.GroesseSetzen(self.radius * 2, self.radius * 2)
        self.symbol.PositionSetzen(self.x - radius, self.y - radius)


    def FarbeSetzen(self, farbe):
        """
        Setzt die Farbe des Kreises.
        Erlaubte Farben sind:
        "weiß", "weiss", "rot", "grün", "gruen", "blau", "gelb", "magenta", "cyan", "hellgelb", "hellgrün", "hellgruen","orange", "braun", "grau", "schwarz", "transparent"
        Außerdem sind rgb-Farbwerte erlaubt in der Form (r, g, b), die Zahlen jeweils aus dem Bereich 0.255
        -- Parameter farbe (neue) Farbe
        """
        self.farbe = farbe
        self.symbol.FarbeSetzen(self.farbe)


    def SichtbarkeitSetzen(self, sichtbar):
        """
        Schaltet die Sichtbarkeit des Kreises ein oder aus.
        Erlaubte Parameterwerte: true, false
        -- Parameter sichtbar (neue) Sichtbarkeit des Kreises
        """
        self.sichtbar = sichtbar
        self.symbol.SichtbarkeitSetzen(self.sichtbar)


    def Entfernen(self):
        """
        Entfernt den Kreis aus dem Zeichenfenster.
        """
        self.symbol.Entfernen()
        del self


    def NachVorneBringen(self):
        """
        Bringt den Kreis eine Ebene nach vorn.
        """
        self.symbol.NachVorneBringen()


    def GanzNachVornBringen(self):
        """
        Bringt den Kreis in die vorderste Ebene.
        """
        self.symbol.GanzNachVornBringen()


    def NachHintenBringen(self):
        """
        Bringt den Kreis eine Ebene nach hinten.
        """
        self.symbol.NachHintenBringen()


    def GanzNachHintenBringen(self):
        """
        Bringt den Kreis in die hinterste Ebene.
        """
        self.symbol.GanzNachHintenBringen()




class Rechteck:
    """
    Wrapperklasse zur Beschreibung von Objekten der Klasse Rechteck
    """

    def __init__(self, x = 10, y = 10, winkel = 0, breite = 100, hoehe = 200, farbe = "rot", sichtbar = True):
        """
        Die Initalisierungsmethode sorgt für die Anfangsbelegung der Attribute für Position und Aussehen.
        -- Parameter x anfängliche x-Position der linken oberen Ecke (Standardwert: 10)
        -- Parameter y anfängliche y-Position der linken oberen Ecke (Standardwert: 10)
        -- Parameter winkel anfänglicher Winkel (Standardwert: 0)
        -- Parameter breite anfängliche Breite (Standardwert: 100)
        -- Parameter hoehe anfängliche Höhe (Standardwert: 200)
        -- Parameter farbe anfängliche Farbe (Standardwert: "rot")
        -- Parameter sichtbar anfängliche Sichtbarkeit (Standardwert: True)
        """
        self.x = x
        # x-Position der linken oberen Ecke

        self.y = y
        # y-Position der linken oberen Ecke

        self.winkel = winkel
        # Drehwinkel (0<=winkel<=360)

        self.breite = breite
        # Breite des Rechteck

        self.hoehe = hoehe
        # Höhe des Rechtecks

        self.farbe = farbe
        #Farbe des Rechtecks

        self.sichtbar = sichtbar
        # Sichtbarkeit des Rechtecks (True oder False)

        self.symbol = RechteckIntern(self.farbe, self.x, self.y, self.breite, self.hoehe, self.winkel, self.sichtbar)
        # Referenz auf das Rechteckssymbol

    def PositionSetzen(self, x, y):
        """
        Setzt die Position der linken oberen Ecke des Rechtecks.
        -- Parameter x x-Position der Spitze
        -- Parameter y y-Position der Spitze
        """
        self.x = x
        self.y = y
        self.symbol.PositionSetzen(self.x, self.y)


    def Verschieben(self, deltaX, deltaY):
        """
        Verschiebt das Rechteck um die angegebenen Werte.
        -- Parameter deltaX Verschiebung in x-Richtung
        -- Parameter deltaY Verschiebung in y-Richtung
        """
        self.x += deltaX
        self.y += deltaY
        self.symbol.PositionSetzen(self.x, self.y)


    def Drehen(self, grad):
        """
        Dreht das Rechteck.
        -- Parameter grad Drehwinkel (mathematisch positiver Drehsinn) im Gradmass
        """
        self.winkel = (self.winkel+grad)%360
        self.symbol.WinkelSetzen(self.winkel)


    def WinkelSetzen(self, winkel):
        """
        Setzt den Drehwinkel des Rechtecks.
        Die Winkelangabe ist in Grad,positive Werte drehen gegen den Uhrzeigersinn, negative Werte drehen im Uhrzeigersinn (mathematisch positiver Drehsinn).
        -- Parameter winkel der (neue) Drehwinkel des Rechtecks
        """
        self.winkel = winkel%360
        self.symbol.WinkelSetzen(self.winkel)


    def GroesseSetzen (self, breite, hoehe):
        """
        Setzt die Größe des Rechtecks.
        -- Parameter breite (neue) Breite
        -- Parameter hoehe (neue) Höhe
        """
        self.breite = breite
        self.hoehe = hoehe
        self.symbol.GroesseSetzen(self.breite, self.hoehe)


    def FarbeSetzen(self, farbe):
        """
        Setzt die Farbe des Rechtecks.
        Erlaubte Farben sind:
        "weiß", "weiss", "rot", "grün", "gruen", "blau", "gelb", "magenta", "cyan", "hellgelb", "hellgrün", "hellgruen","orange", "braun", "grau", "schwarz", "transparent"
        Außerdem sind rgb-Farbwerte erlaubt in der Form (r, g, b), die Zahlen jeweils aus dem Bereich 0.255
        -- Parameter farbe (neue) Farbe
        """
        self.farbe = farbe
        self.symbol.FarbeSetzen(self.farbe)


    def SichtbarkeitSetzen(self, sichtbar):
        """
        Schaltet die Sichtbarkeit des Rechtecks ein oder aus.
        Erlaubte Parameterwerte: true, false
        -- Parameter sichtbar (neue) Sichtbarkeit des Rechtecks
        """
        self.sichtbar = sichtbar
        self.symbol.SichtbarkeitSetzen(self.sichtbar)


    def Entfernen(self):
        """
        Entfernt das Rechteck aus dem Zeichenfenster.
        """
        self.symbol.Entfernen()
        del self


    def NachVorneBringen(self):
        """
        Bringt das Rechteck eine Ebene nach vorn.
        """
        self.symbol.NachVorneBringen()


    def GanzNachVornBringen(self):
        """
        Bringt das Rechteck in die vorderste Ebene.
        """
        self.symbol.GanzNachVornBringen()


    def NachHintenBringen(self):
        """
        Bringt das Rechteck eine Ebene nach hinten.
        """
        self.symbol.NachHintenBringen()


    def GanzNachHintenBringen(self):
        """
        Bringt das Rechteck in die hinterste Ebene.
        """
        self.symbol.GanzNachHintenBringen()



class Text:
    """
    Wrapperklasse zur Beschreibung eines Textes
    """

    def __init__(self, x = 10, y = 10, winkel = 0, textgroesse = 12, farbe = "schwarz", sichtbar = True):
        """
        Die Initalisierungsmethode sorgt für die Anfangsbelegung der Attribute für Position und Aussehen.
        -- Parameter x anfängliche x-Position der linken oberen Ecke des Textfeldes (Standardwert: 10)
        -- Parameter y anfängliche y-Position der linken oberen Ecke des Textfeldes (Standardwert: 10)
        -- Parameter winkel anfänglicher Winkel (Standardwert: 0)
        -- Parameter textgroesse anfängliche Textgröße (Standardwert: 12)
        -- Parameter farbe anfängliche Schriftfarbe  (Standardwert: "schwarz")
        -- Parameter sichtbar anfängliche Sichtbarkeit (Standardwert: True)
        """

        self.x = x
        # x-Position der linken oberen Ecke

        self.y = y
        # y-Position der linken oberen Ecke

        self.winkel = winkel
        # Drehwinkel (0<=winkel<=360)

        self.textgroesse = textgroesse
        # Schriftgröße

        self.farbe = farbe
        # Farbe des Textes

        self.sichtbar = sichtbar
        # Sichtbarkeit des Textes (True oder False)

        self.symbol = TextIntern(self.farbe, self.x, self.y, self.textgroesse, self.winkel, self.sichtbar)
        # Referenz auf das Symbol

    def PositionSetzen(self, x, y):
        """
        Setzt die Position der linken oberen Ecke des Textes.
        -- Parameter x x-Position der Spitze
        -- Parameter y y-Position der Spitze
        """
        self.x = x
        self.y = y
        self.symbol.PositionSetzen(self.x, self.y)


    def TextSetzen(self, text):
        """
        Legt den dargestellten Text fest.
        -- Parameter text dargestellter Text
        """
        self.symbol.TextSetzen(text)


    def TextGroesseSetzen(self, groesse):
        """
        Legt die Schriftgröße fest.
        -- Parameter groesse Schriftgröße
        """
        self.textgroesse = groesse
        self.symbol.TextGroesseSetzen(groesse)


    def TextVergroessern(self):
        """
        Erhöht die Schriftgröße.
        """
        self.symbol.TextVergroessern()
        self.textgroesse = self.symbol.groesse


    def TextVerkleinern(self):
        """
        Verkleinert die Schriftgröße.
        """
        self.symbol.TextVergroessern()
        self.textgroesse = self.symbol.groesse


    def Verschieben(self, deltaX, deltaY):
        """
        Verschiebt die Schrift.
        -- Parameter deltaX Verschiebung in x-Richtung
        -- Parameter deltaY Verschiebung in y-Richtung
        """
        self.x += deltaX
        self.y += deltaY
        self.symbol.PositionSetzen(self.x, self.y)


    def Drehen(self, grad):
        """
        Dreht das Textfeld.
        -- Parameter grad Drehwinkel (mathematisch positiver Drehsinn) im Gradmass
        """
        self.winkel = (self.winkel+grad)%360
        self.symbol.WinkelSetzen(self.winkel)


    def WinkelSetzen(self, winkel):
        """
        Setzt den Drehwinkel des Textfeldes.
        Die Winkelangabe ist in Grad,positive Werte drehen gegen den Uhrzeigersinn, negative Werte drehen im Uhrzeigersinn (mathematisch positiver Drehsinn).
        -- Parameter winkel der (neue) Drehwinkel des Textfeldes
        """
        self.winkel = winkel%360
        self.symbol.WinkelSetzen(self.winkel)


    def GroesseSetzen (self, breite, hoehe):
        """
        Legt die Größe des Textfeldes fest.
        -- Parameter breite Breite des Textfeldes
        -- Parameter hoehe Höhe des Textfeldes
        """
        self.breite = breite
        self.hoehe = hoehe
        self.symbol.GroesseSetzen(self.breite, self.hoehe)


    def FarbeSetzen(self, farbe):
        """
        Setzt die Farbe des Textes.
        Erlaubte Farben sind:
        "weiß", "weiss", "rot", "grün", "gruen", "blau", "gelb", "magenta", "cyan", "hellgelb", "hellgrün", "hellgruen","orange", "braun", "grau", "schwarz", "transparent"
        Außerdem sind rgb-Farbwerte erlaubt in der Form (r, g, b), die Zahlen jeweils aus dem Bereich 0.255
        -- Parameter farbe (neue) Farbe
        """
        self.farbe = farbe
        self.symbol.FarbeSetzen(self.farbe)


    def SichtbarkeitSetzen(self, sichtbar):
        """
        Schaltet die Sichtbarkeit des Textes ein oder aus.
        Erlaubte Parameterwerte: true, false
        -- Parameter sichtbar (neue) Sichtbarkeit des Texts
        """
        self.sichtbar = sichtbar
        self.symbol.SichtbarkeitSetzen(self.sichtbar)


    def Entfernen(self):
        """
        Entfernt den Text aus dem Zeichenfenster.
        """
        self.symbol.Entfernen()
        del self


    def NachVorneBringen(self):
        """
        Bringt den Text eine Ebene nach vorn.
        """
        self.symbol.NachVorneBringen()


    def GanzNachVornBringen(self):
        """
        Bringt den Text in die vorderste Ebene.
        """
        self.symbol.GanzNachVornBringen()


    def NachHintenBringen(self):
        """
        Bringt den Text eine Ebene nach hinten.
        """
        self.symbol.NachHintenBringen()


    def GanzNachHintenBringen(self):
        """
        Bringt den Text in die hinterste Ebene.
        """
        self.symbol.GanzNachHintenBringen()



class Turtle:
    """
    Wrapperklasse zur Beschreibung der Turtle
    """


    def __init__(self, x = 100, y = 200, winkel = 0, farbe = "schwarz", sichtbar = True, stiftUnten = True):
        """
         Die Initalisierungsmethode sorgt für die Anfangsbelegung der Attribute für Position und Aussehen.
        -- Parameter x anfängliche x-Position der Schwanzspitze (Standardwert: 100)
        -- Parameter y anfängliche y-Position der Schwanzspitze (Standardwert: 200)
        -- Parameter winkel anfänglicher Winkel (Standardwert: 0)
        -- Parameter farbe anfängliche Farbe des Objekts (Standardwert: "schwarz")
        -- Parameter sichtbar anfängliche Sichtbarkeit (Standardwert: True)
        -- Parameter stiftUnten gibt an, ob der Stift unten ist (Zeichenmodus) (Standardwert: True)
        """
        self.x = x
        # x-Position der Schwanzspitze

        self.y = y
        # y-Position der Schwanzspitze

        self.winkel = winkel
        # Drehwinkel (0<=winkel<=360)

        self.farbe = farbe
        # Stiftfarbe der Turtle (auch Augen- und Schwanzfarbe)

        self.groesse = 40
        # Größe der Turtle

        self.sichtbar = sichtbar
        # Sichtbarkeit der Turtle (True oder False)

        self.stiftUnten = stiftUnten
        # Gibt an, ob die Turtle im Zeichenmodus oder ob der Stift angehoben ist.

        self.symbol = TurtleIntern(self.farbe, self.x, self.y, self.groesse, self.winkel, self.sichtbar)
         # Referenz auf das Symbol

        Zeichenfenster().BeobachterRegistrieren(self)


    def AktionAusfuehren(self):
        """
        Aktionsmethode, die bei jedem Taktschlag ausgeführt wird.
        Muss bei Bedarf in einer Unterklasse überschrieben werden.
        """
        pass


    def TasteGedrueckt(self, taste):
        """
        Aktionsmethode, die bei jedem Tastendruck ausgelöst wird.
        Muss bei Bedarf in einer Unterklasse überschrieben werden.
        -- Parameter taste gedrückte Taste
        """
        #print("Taste gedrueckt: ", taste)
        pass

    def TasteLosgelassen(self, taste):
        """
        Aktionsmethode, die bei jedem Loslassen einer Taste ausgelöst wird.
        Muss bei Bedarf von einer Unterklasse überschrieben werden.
        -- Parameter taste losgelassene Taste
        """
        #print("Taste losgelassen: ", taste)
        pass


    def MausGeklickt(self, posX, posY, button):
        """
        Aktionsmethode, die bei jedem Mausklick ausgelöst wird.
        Muss bei Bedarf von einer Unterklasse überschrieben werden.
        -- Parameter posX Position des Mausklicks
        -- Parameter posY Position des Mausklicks
        -- Parameter button Maustaste (1-links, 2-Mausrad, 3-rechts, 4-Mausrad nach oben, 5-Mausrad nach unten)
        """
        #print("Maustaste: ", button, " an Position: ", posX, ", ", posY)        pass
        pass


    def Gehen(self,laenge):
        """
        Verschiebt die Turtle in die Richtung ihres Winkels.
        -- Parameter laenge Anzahl der Längeneinheiten
        """
        self.symbol.Gehen(laenge)
        self.x = self.symbol.x
        self.y = self.symbol.y


    def PositionSetzen(self, x, y):
        """
        Setzt die Position der Turtle (Position der Schwanzspitze). Bei der Positionsänderung wird auch bei abgesenktem Stift keine Linie gezeichnet.
        -- Parameter x x-Position der Schwanzspitze
        -- Parameter y y-Position der Schwanzspitze
        """
        self.x = x
        self.y = y
        self.symbol.PositionSetzen(self.x, self.y)


    def Drehen(self, grad):
        """
        Dreht die Figur
        -- Parameter grad Drehwinkel (mathematisch positiver Drehsinn) im Gradmass
        """
        self.winkel = (self.winkel+grad)%360
        self.symbol.WinkelSetzen(self.winkel)


    def WinkelSetzen(self, winkel):
        """
        Setzt den Drehwinkel der Turtle.
        Die Winkelangabe ist in Grad, positive Werte drehen gegen den Uhrzeigersinn, negative Werte drehen im Uhrzeigersinn (mathematisch positiver Drehsinn). 0°: rechts; 90°: oben; 180°: links; 270° unten
        -- Parameter winkel der (neue) Drehwinkel der Turtle
        """
        self.winkel = winkel%360
        self.symbol.WinkelSetzen(self.winkel)



    def FarbeSetzen(self, farbe):
        """
        Setzt die Stiftfarbe der Turtle.
        -- Parameter farbe Stiftfarbe der Turtle
        """
        self.farbe = farbe
        self.symbol.FarbeSetzen(self.farbe)


    def Entfernen(self):
        """
        Entfernt die Turtle aus dem Zeichenfenster.
        """
        self.symbol.Entfernen()
        Zeichenfenster().BeobachterEntfernen(self)
        del self


    def NachVorneBringen(self):
        """
        Bringt die Turtle eine Ebene nach vorn.
        """
        self.symbol.NachVorneBringen()


    def GanzNachVornBringen(self):
        """
        Bringt die Turtle in die vorderste Ebene.
        """
        self.symbol.GanzNachVornBringen()


    def NachHintenBringen(self):
        """
        Bringt die Turtle eine Ebene nach hinten.
        """
        self.symbol.NachHintenBringen()


    def GanzNachHintenBringen(self):
        """
        Bringt die Turtle in die hinterste Ebene.
        """
        self.symbol.GanzNachHintenBringen()


    def ZumStartpunktGehen(self):
        """
        Bringt die Turtle zu ihrem Startpunkt. Die Zeichnung wird dabei gelöscht.
        """
        self.symbol.ZumStartpunktGehen()
        self.x = self.symbol.x
        self.y = self.symbol.y
        self.winkel = self.symbol.winkel


    def StiftHeben(self):
        """
        Turtle bewegt sich danach, ohne zu zeichnen.
        """
        self.stiftUnten = False
        self.symbol.StiftHeben()


    def StiftSenken(self):
        """
        Turtle wechselt in den Zeichenmodus.
        """
        self.stiftUnten = True
        self.symbol.StiftSenken()


    def SichtbarkeitSetzen(self, sichtbar):
        """
        Schaltet die Sichtbarkeit der Zeichnung ein oder aus.
        Erlaubte Parameterwerte: true, false
        -- Parameter sichtbar (neue) Sichtbarkeit der Zeichenfläche
        """
        self.sichtbar = sichtbar
        self.symbol.SichtbarkeitSetzen(self.sichtbar)


    def SichtbarkeitZeichenflaecheSetzen(self, sichtbar):
        """
        Schaltet die Sichtbarkeit der Zeichenfläche ein oder aus.
        Erlaubte Parameterwerte: true, false
        -- Parameter sichtbar (neue) Sichtbarkeit der Zeichenfläche der Turtle
        """
        self.symbol.SichtbarkeitZeichenflaecheSetzen(sichtbar)


    def WinkelGeben(self):
        """
        Liefert den Winkel der Turtle.
        -- return Winkel
        """
        return self.winkel


    def XPositionGeben(self):
        """
        Liefert die x-Position der Turtle.
        -- return x-Position
        """
        return self.x


    def YPositionGeben(self):
        """
        Liefert die y-Position der Turtle.
        -- return y-Position
        """
        return self.y


    def Beruehrt(self):
        """
        Testet, ob die Turtle ein Grafikelement berührt.
        -- return true, wenn die Turtle und eine Grafikfigur überlappen
        """
        return self.symbol.Beruehrt()


    def BeruehrtFarbe(self, farbe):
        """
        Testet, ob die Turtle mit der Schwanzspitze eine gegebene Farbe berührt
        -- Parameter farbe Farbe, auf die getestet werden soll.
        -- return true wenn ein Objekt mit der Farbe berührt wird.
        """
        return self.symbol.BeruehrtFarbe(farbe)


    def BeruehrtObjekt(self, objekt):
        """
        Testet, ob die Turtle eine Objekt berührt.
        -- Parameter objekt Objekt, mit dem eine Überschneidung geprüft werden soll.
        -- return true wenn das übergebene Objekt mit der Farbe berührt.
        """
        return self.symbol.BeruehrtObjekt(objekt)


    def Loeschen(self):
        """
        Leert die Zeichenfläche der Turtle.
        """
        self.symbol.Loeschen()


    def FensterNeuZeichnen(self):
        """
        Das gesamte Fenster wird neu gezeichnet.
        Dies passiert nach einem Durchlauf der Hauptroutine des Programms automatisch.
        Will man innerhalb einer Methode ein Neuzeichnen veranlassen (z. B. um nach Bewegung eines Objekts auf Berührung zu testen), so kann diese Methode ein Neuzeichnen zu anderer Zeit bewirken.
        """
        self.symbol.FensterNeuZeichnen()