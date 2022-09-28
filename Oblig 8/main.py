"""
Dette er hovedprogrammet, det importerer spill klassen.
Hovedprogrammet lar brukeren bestemme dimensjonene til spillet og lar brukeren spille det så lenge
han/hun ikke trykker q.
For hver nye generasjon skriver hovedprogrammet ut selve brettet, gen nr og antall levende.
"""

from spillebrett import Spillebrett     #importerer spillebrett klassen

def main():
    print("Skriv in dimmensjonene til ditt Game of Life!")
    rad = int(input("Antall rader: "))
    kolonne = int(input("Antall kolonner: "))

    spill = Spillebrett(rad, kolonne)       #lager spillet med dimensjonene bruker har oppgitt
    print()
    spill.tegnBrett()       #skriever ut brettet  terminalem
    print("Generasjon: " + str(spill._genNr))   #skriver ut generasjons nummeret
    levende = spill.finnAntallLevende()         #finner antall levende
    print("Antall levende celler: " + str(levende))     #skriver ut antall levende
    print()

    svar = input("Trykk enter for å gå til neste generasjon, eller q og enter for å avslutte: ")    #gir videre instruksjoner til bruker
    while svar != "q":      #så lenge bruker fortsetter, aka ikke skriver in q
        spill.oppdatering()     #oppdateres spillet
        print()
        spill.tegnBrett()       #det nye spillet skrives ut
        print("Generasjon: " + str(spill._genNr))   #skriver ut det nye generasjons nummeret
        levende = spill.finnAntallLevende()     #finner det nye antall levende
        print("Antall levende celler: " + str(levende)) #skriver ut det nye antall levende
        #print()
        svar = input("Trykk enter for å gå til neste generasjon, eller q og enter for å avslutte: ")    #gir instruksjoner igjenn

# starte hovedprogrammet
main()
