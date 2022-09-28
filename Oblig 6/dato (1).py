

"""
Dette er et program som definerer en klasse og en del metoder objekten i klassen har nytte av
"""
#Oppgave 1 og 2
class Dato:                                             #Lager en klasse
    def __init__(self, nyDag, nyMaaned, nyAar):         #Lager en konduktør med tre parametre
        self._nyDag = int(nyDag)                            #definerer self._nyDag fra nyDag parametre
        self._nyMaaned = int(nyMaaned)                      #definerer self._nyMaaned fra nyMaaned paramteren
        self._nyAar = int(nyAar)                            #definerer self._nyAar fra nyAar parametrener
    def lesAar(self):                                   #Lager en matode
        return self._nyAar                                  #returnerer self._nyAar
    def lesDag(self):                                   #Lager en metode
        return self._nyDag                                  #returnerer self._nyDag
    def skrivUt(self):                                  #LAger en metode
        print("Datoen er: " + str(self._nyDag) + ". " + str(self._nyMaaned) + ". " + str(self._nyAar))  #skriver ut dette i terminalen
    def skjekk(self, dag):      #LAger en skjekk variabel
        svar = ""           #Lager en tom variabel
        if dag == self._nyDag:      #om datoen er den samme
            svar += "Det er riktig"     #setter svar = riktig
        else:                       #Om ikke
            svar += "Det er feil"         #svar = feil
        return svar     #Returnerer feil

#Ferdig med klasssen
