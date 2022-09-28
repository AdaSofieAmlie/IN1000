
"""
Dette en en klasse som tar in to parametre og har fire metoder som kan gjøre endringer/skjekker objektet
I denne kladden er det en metode som spiller sangen, ved å skrive d ut i terminalen
Det er en metode som skjekker at en gitt artist er artisten, eller en av artistene til sangen
Det er en metode som skjekker at en gitt tittel er tittelen til sangen
Til slutt er det en som skjekker både tittel og artist
"""

class Sang:         #Definerer en klasse som heter sang
    def __init__(self, artist, tittel):         #Lager en konduktør som tar in to parametre
        self._artist = artist                       #Definerer self._artist til artist
        self._tittel = tittel                       #Definerer self._tittel til tittel
    def spill(self):                            #Lager en metode som heter spill
        print ("Spiller " + self._tittel + " av " + self._artist + ".")      #Skriver ut hvilke sang s0om spilles og hvem som har laget den
    def sjekkArtist(self, navn):                #Lager en metode som heter sjekkArtist som tar in en parameter
        navnListe = navn.split()                    #Splitter parameteren i tilfelle det ble sendt inn flere en ett ord
        for i in range(len(navnListe)):             #For løkke som går like mange ganger som ord i navnet som ble sent inn i parameteren
            if navnListe[i] in (self._artist.split()):      #Om et av navnene er i artist navnet som objektet først ble laget med
                    return True                                #Returnerer TRUE
        return False                #Ellers returnerer FALSE
    def sjekkTittel(self, tittel):          #Lager en metode som heter sjekkTittel som tar in en parameter
        if self._tittel.lower() == tittel.lower():      #Om tittelen til objektet er de samme som tittel parameteren, forklarer mer under
            return True                             #Returnerer TRUE
        return False        #Returnerer FALSE
    def sjekkArtistOgTittel(self, artist, tittel):          #Lager en metodesjekkArtistOgTittel som tar in to  parametere
        if (self.sjekkArtist(artist) == True) and (self.sjekkTittel(tittel) == True):   #Forklarer under
            return True         #Returnerer TRUE
        return False    #ellers Returnerer false
"""
Linje 19: Jeg gjorde dem om til små bokstaver for å bare måle om det er likt når begge er
små bokstaver, fordi da har de like bokstav
Linje 22: Om objektest kall på metode sjekkArtist med artist som parameter er true og
objektest kall på metode sjekkTittel med tittel som parameterer true
"""
