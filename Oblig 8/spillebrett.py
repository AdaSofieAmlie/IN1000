
"""
Dette programmet er en klasse som tar i bruk klassen Celle fra celle.py
Klassen heter spillebrett og tegnet opp et spillebrett i konstruktøren med engang den blir kalt på.
I tillegg kaller konstruktøren på en metode som gjør at spilbrettet blir generert.
Klasssen har en metode som tegner brettet i terminalen, en metode som oppdaterer spillebrettet til neste generasjon,
en metode som finner antall levende, og en som finner naboen til hver celle.
"""
import random                       #impoerterer random
from random import randint          #Importerer randint
from celle import Celle             #Importerer celle klassen

class Spillebrett:
    def __init__(self, rader, kolonner):        #konstruktør som tar in to parametere, rader og kolonner
        self._rader = int(rader)
        self._kolonner = int(kolonner)
        self._rutenett = []                 #Lager en tom liste som skal blir spilbrettet/ rutenettet
        for rad in range(self._rader):          #Løkke som går like mange ganger som antall rader
            self._rutenett.append([])           #LEgger til en rad i rutenettet
            for kolonne in range(self._kolonner):   #Løkke som går like mange ganger som antall kolonner
                self._rutenett[rad].append(Celle())     #Legger til like mange celler i en rad som kolonner
        self._genNr = 0         #Generasjons nr
        self._generer()         #Kaller på _generer

    def tegnBrett(self):            #metode som tegner spill brettet, uten parametere
        for rad in self._rutenett:      #løkke som går igjennom rad(listene) inni self._rutenett listen
            #print(rad)
            for kolonne in rad:             #Løkke som går igjennom elementene i rad listene
                print(kolonne.hentStatusTegn(), end = "")   #Skriver ut tegnet på elementet i rutenettet
            print()     #print blank for å få ny linje

    def oppdatering(self):      #metode oppdatering, uten parametere
        tilDoedListe = []           #tomme lister
        tilLevendeListe = []

        for rad in range(self._rader):                  #løkke går antall rader ganger
            for kolonne in range(self._kolonner):           #løkke går antall kolonner ganger
                naboerL = self.finnNabo(rad,kolonne)        #Finner naboen til hvert element etter som løkken går videre ved hjelp av finnNabo
                dødeNaboerAnt = 0      #Starter med 0 døde naboer
                levendeNaboerAnt = 0    #starter med 0 levende naboer

                for nabo in naboerL:        #løkke wsom går igjennom naboene i listen med naboer fra finnNabo metoden
                    if nabo.erLevende():        #om naboen er levende
                        levendeNaboerAnt += 1       #legger til ant levende naboer
                    else:                            #om ikke
                        dødeNaboerAnt += 1      #legger til død nabo

                if self._rutenett[rad][kolonne].erLevende():        #Om cellen det er snakk om er levende
                    if levendeNaboerAnt > 2:            #om det er ferre enn 2 levende naboer
                        tilDoedListe.append(self._rutenett[rad][kolonne])   #legger til celle elementet i tilDoed listen
                    elif (levendeNaboerAnt == 2) or (levendeNaboerAnt == 3):    #om det er 2 eller 3 levende naboer
                        tilLevendeListe.append(self._rutenett[rad][kolonne])    #legger til celle objektet i tilLevende listen
                    else:       #ellers
                        tilDoedListe.append(self._rutenett[rad][kolonne])   #legger til objektet i tildoed listen
                else:                                       #om cellen det er snakk om er død
                    if levendeNaboerAnt == 3:       #om det er 3 levende naboer
                        tilLevendeListe.append(self._rutenett[rad][kolonne])    #legger til objektet i til Levende

        for celle in tilLevendeListe:   #Går igjennom tilLevende listen
            celle.settLevende()     #endrer statusen til objektene
        for c in tilDoedListe:      #går igjennom tilDoed listen
            c.settDoed()            #endrer statusen til død på objektene

        self._genNr += 1    #legger til 1 på gerasjons nr

    def finnAntallLevende(self):        #metode fin antall levende
        antLevende = 0      #Starter med 0
        for rad in self._rutenett:  #Går igjennom rad (listene) i self._rutnettt listen
            for kolonne in rad:         #går igjennom elementen i rad listene
                if kolonne.erLevende():     # om elementer er levende
                    antLevende += 1             #legger til 1 på antLevende
        return antLevende   #returnerer antall levende

    def _generer(self):     #metode _generer
        for rad in self._rutenett:      #går igjennom rad listene i self._rutenett
            for kolonne in rad:     #går igjennom elementene i rd listene
                if random.randint(0,2) == 0:    #om et random tall fra 0 til 2 er 0, så det er 33% sannsynlighet
                    kolonne.settLevende()   #Sett elementet til levende
                else:       #ellers
                    kolonne.settDoed()  #sett elementet til doed

    def finnNabo(self, rad, kolonne):   #finnNabo metode med to elementer
        naboListe = []      #Starter med tom liste med naboer
        for i in range(-1,2):       #Går igjennom fra -1 til 2 for å få naboene før og etter
            for j in range(-1,2):       #Går igjennom fra -1 til 2 for å få naboene før og etter
                naboRad = rad + i           #rad nr til anboen
                naboKol = kolonne + j       #kolonne nr til naboe

                aktuelt = True  #Starter ved å anta at alle naboene er aktuelle

                if (i == 0) and (j == 0):       #om i == 0 og j == 0 er vi på indeksen til cellen vi ønsker å finne naboer til, dermed er den ikke aktuell som nabo
                    aktuelt = False           #naboen er ikke aktuell
                if (naboRad < 0) or (naboRad >= self._rader):   #om naboen er uttenfor rutenettet (ved rader) er det ikke en aktuell nabo
                    aktuelt = False             #naboen er ikke aktuell
                if (naboKol < 0) or (naboKol >= self._kolonner):    #om naboen er uttenfor rutenettet (ved kolonner) er det ikke e aktuell nabo
                    aktuelt = False
                      #naboen er ikke aktuell
                if aktuelt:     #om naboen er aktuell
                    naboListe.append(self._rutenett[naboRad][naboKol])  #Legger til naboen i nabo listen
        return(naboListe)   #returnerer listen
