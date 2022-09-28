

"""
Dette programmet samler inn input fra brukeren for å telle forekomster.
Det er en funsjoner som teller antal bokstaver og en som legger til de forksjellige ordene i en ordbok og teller om det er skrevet før.
Deretter spør jeg brukeren om en tekst og bruker fuksjonene i en forløkke.
"""

#Oppgave 1
def antallBokstaver(ord):               #Deffinerer en funksjon med en parameter
    antB = len(ord)                     #Teller hvor mange bokstaver som er i ordet
    return antB                         #Returnerer antallet

#Oppgave 2

ordBok = {}                             #Tom ordbok
def ordOrdbok(setning):                 #Deffinerer en funksjon med en parameter
    ord = setning.split()               #Gjør om setningen til en liste med ord
    for i in ord:                       #skjører like lenge som antall elementer i ord listen
        #print(i)                               #Skjekk for å forsikre meg om hva i er
        if i not in ordBok:             #Om i ikke er i ordbok fra før av
            ordBok[i] = 0                   #legger det til i ordboken
        ordBok[i] += 1                  #Legger til et antall i ordboken
    return ordBok                      #returnerer ordboken

#Oppgave 3
tekst = input("Skriv inn en setning (med tegnsetting med mellomrom mellom): ").lower()          #Spør om en setning
tekstSplit = tekst.split()                                                                      #gjør om setning til lise med ord
print("Det er " + str(len(tekstSplit)) + " ord i setningen din")            #Skriver ut hvor mange ord det er i setningen,langden av ord listen

ordBokPrint = ordOrdbok(tekst)         #En variabel som er like retur verdien av funksjonen ordOrdbok med teskt som argument

for i in ordBokPrint:                   #Går igjennom like mange ganger som lengden på ordBokPrint'en
    antBokstaverPrint = antallBokstaver(i)          #finner antall bokstaver i hvert ord
    print("Ordet " + i + " forekommer " + str(ordBokPrint[i]) + " ganger, og har " + str(antBokstaverPrint) + " bokstaver.")
        #Printer ut i terminalen.
            # i er nøkkel verdien fra ordboken
            #ordbokPrint(i) er antall ord, aka innholdsverdien
            #antBokstaverPrint er antall bokstaver i det ordet (fra lnje 34)
