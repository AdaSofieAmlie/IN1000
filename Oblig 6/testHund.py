

#Oppgave 5
from Hund import Hund       #importerer klassen fra filen

def hovedprogram():                 #Definerer hovedprogram
    pluto = Hund(2,2)                   #Lager et objekt i klasse hund
    scooby = Hund(5,4)                  #lager et annet objekt i klasse hund
    print("Plutos vekt: " + str(pluto.hentVekt()))      #Skriver ut hvert objekt sin vekt fra hent vekt
    print("Scoobys vekt: " + str(scooby.hentVekt()))
    print("")

    pluto.spring()          #kaller på metoden spring fra klassen
    print("Plutos vekt etter 1 spring: " + str(pluto.hentVekt()))   #PRinter ut vekten for å se endringen
    pluto.mat(1)            #KAller på metoden mat med 1 som argument
    print("Plutos vekt etter første måtlid: " + str(pluto.hentVekt()))  #printer ut vekt for å se endringen

    scooby.spring()      #kaller på metoden spring fra klassen
    print("Scooby vekt etter 1 spring: " + str(scooby.hentVekt()))      #Printer ut vekten for å se endringen
    scooby.mat(1)           #KAller på metoden mat med 1 som argument
    print("Scooby vekt etter første måltid: " + str(scooby.hentVekt()))     #Printer ut vekten for å se endringen
    scooby.mat(1)           #KAller på metoden mat med 1 som argument
    print("Scooby vekt etter andre måltid: " + str(scooby.hentVekt()))      #Printer ut vekten for å se endringen

    print("")
    print("Plutos vekt til slutt: " + str(pluto.hentVekt()))       #Printer ut vektens sluttresultat
    print("Scoobys vekt  til slutt: " + str(scooby.hentVekt()))         #Printer ut vektens sluttresultat

hovedprogram()          #kaller på hovedprogrammet
