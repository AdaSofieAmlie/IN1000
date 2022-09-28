

"""
Dette er et program som definerer en klasse og en del metoder objekten i klassen har nytte av
"""

#Oppgave 1,2,3,4
class Motorsykkel:                                          #lager en klasse
    def __init__(self, merke, regNr, kmAvstand):            #Lager en konduktør, med tre ekstre parametre
        self._merke = merke                                     #definerer merke til self._merke
        self._regNr = regNr                                     #definerer regNr til self._regNr
        self._kmAvstand = int(kmAvstand)                        #definerer kmAvstand til self._kmAvstand
    def kjor(self, km):                                     #lager en metode som tar in km
        self._kmAvstand = self._kmAvstand + int(km)             #Legger til km på self._kmAvstand
    def hentKilometerstand(self):                           #lager en metode til, denne tar ikke inn noen parametre
        return self._kmAvstand                                  #returnerer self._kmAvstand
    def skrivUt(self):                                      #lager en metode til som ikke tar in parametre
        print("Merke: " + self._merke)                          #skriver ut merke
        print("Registrerigs nummer: " + str(self._regNr))            #Skriver ut regNr
        print("Kilometer avstand: " + str(self._kmAvstand))     #skriver ut kmAvstand

#Ferdig med klassen :)
