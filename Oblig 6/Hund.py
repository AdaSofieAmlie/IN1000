

"""
Dette er et program som definerer en klasse og en del metoder objekten i klassen har nytte av
"""
#Oppgave 1,2,3,4
class Hund:                             #lager en klasse
    def __init__(self, alder, vekt):        #lager en konduktør med alder og vekt som paramtre
        self._alder = int(alder)                #Definerer alder til self._alder
        self._vekt = int(vekt)                  #definerer vekt til self._vekt
        self._metthet = 10                      #Setter self._metthet til verdien 10
    def hentAlder(self):                    #Lager en mentode: hent Alder
        return (self._alder)                    #returnerer self._alder
    def hentVekt(self):                     #lager en metode: hent Vekt
        return (self._vekt)                     #returnerer self._vekt
    def spring(self):                       #Lager en metode spring
        self._metthet = self._metthet - 1       #trekker fra 1 på self._metthet
        if self._metthet < 5:                   #om self.metghet er mindre en 5
            self._vekt = self._vekt - 1             #Trekker vek 1 fra self.vekt
    def mat(self, matTall):                 #lager en metode mat, som tar in matTall som parameter
        self._metthet = self._metthet +1        #Legger til 1 på self._metthet
        if self._metthet > 7:                   #om metther er større en 7
            self._vekt = self._vekt + 1             #LEgger til 1 på self._vekt
#Ferdig med klassen
