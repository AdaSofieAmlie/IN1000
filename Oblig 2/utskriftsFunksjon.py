"""Dette er et program som kommuniserer med brukeren"""

def informasjon():              #Prosedyre
    navn = input("Skriv inn navn: ")            #Spør om navn ved hjelp av input
    boSted = input("Hvor kommer du fra? ")          #Spør om hvor brukeren er bra ved hjelp av input
    print("Hei, " + navn + "! Du er fra " + boSted + ".")       #Printer ut deres navn og hvor de er fra i aen melding
    print("")       #Mellom linje mellom de tre forksjellige brukerne

informasjon()           #Kaller på prosedyren tre ganger
informasjon()
informasjon()
