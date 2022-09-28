
"""
Dette er et program som henter en klasse og bruker objektene self i en anne klassen.
Klassen spilleliste tar in et parameter listenavn.
I klassen er det en metode som henter in data fra en fil, og lager sang objekter av dem fra sang klassen og legger dem til i sang listen
I klassen er det hver sin emtode som legger til eller tar vekk en sang.
Derretter er det to metoder, e som psiller av en sang, og en annen som spiller av alleData
Så er det en metode som finner en sang, gitt tittelene
Og til slutt er det en metode som henter ut alle sangene av samme artist, gitt artistnavnet.
"""
from sang import Sang       #Importerer sang klassen fra sang filen

class Spilleliste:
    def __init__(self, listenavn):      #Konduktør
        self._sanger = []
        self._navn = listenavn          #note to self: ikke en liste, men navnet på spillelisten
    def lesFraFil(self, filnavn):       #metode m en parameter
        fil = open(filnavn)                 #åpner fil
        for linje in fil:                   #går igjennom filen
            alleData = linje.strip().split(';')         #finner artist og tittel
            tittel = alleData[0]
            #print(tittel)
            artist = alleData[1]
            #print(artist)
            sang = Sang(artist,tittel)      #lager sang objekt
            (self._sanger).append(sang)         #Legger til objektet i listen
        fil.close()
        #print(self._sanger)
    def leggTilSang(self, nySang):      #metode m en parameter
        self._sanger.append(nySang)     #legger til ny sang objekt i listen
    def fjernSang(self, sang):
        self._sanger.remove(sang)           #tar vekk sang
    def spillSang(self, sang):          #metode m en parameter
        sang.spill()        #spill() fra sang klassen
    def spillAlle(self):
        for i in range(len(self._sanger)):
            self._sanger[i].spill()         #Spill() fra snag klassen, spiller alle klassene
    def finnSang(self, tittel):     #metode m en parameter
        svar = None         #none om ikke tittelen finned i listen
        for i in range(len(self._sanger)):
            if (self._sanger[i].sjekkTittel(tittel) == True):       #skjekker om tittelen brukeren spør om er i listen
                svar = self._sanger[i]      #endrer svar til sang objektet
        return svar
    def hentArtistUtvalg(self, artistnavn): #metode m en parameter
        artistSangListe = []            #tom liste
        for i in range(len(self._sanger)):
            if self._sanger[i].sjekkArtist(artistnavn) == True:     #Skjekker om hver artisten er i listen og om de er mer en 1
                artistSangListe.append(self._sanger[i])     #LEgger til sang objektet i listen
        return artistSangListe
