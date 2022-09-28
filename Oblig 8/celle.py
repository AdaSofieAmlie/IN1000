
"""
Dette programmet er kun en klasse som heter Celle. Den tar ikke in en parameter.
Klassen har metoder som endrer statusen på cellen, skjekker statusen og henter
ut teget etter hvilken status cellen har.
"""

class Celle:
    def __init__(self):             #Konstruktøren tar ikke inn noen parametere
        self._status = "død"            #Celle objektet starter alltid dødt

    def settDoed(self):             #Metode som gjør cellen død
        self._status = "død"

    def settLevende(self):          #Metode som gjør cellen levende
        self._status = "levende"

    def erLevende(self):            #Metode som skjekker om cellen er levende
        if (self._status == "levende"):
            return True
        return False

    def hentStatusTegn(self):       #Metode som skriver ut cellen, med riktig status
        if self.erLevende() == True:
            return "O"
        return "."
