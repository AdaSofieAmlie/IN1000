"""
Dette er et program som omhandler nøstede lister; en ordbo med lister som innholdsverdi.
Programmet skriver også ut mat infoen om en pasient ettersom brukeren spurte etter det.
"""

#Oppgave 1
beboer = {                                          #lager en ordbok
    "Knut Dahl": ["Grøt", "Salat", "Biff"],         #nøkkelverdi; innholdsverdi som liste med mat
    "Ole Hauger": ["Brød", "Frukt", "Pasta"],
    "Hanne Moss": ["Mussli", "Smørbrød", "Sushi"],
}

#Oppgave 2
def sykehjemUtskrift():                                 #Prosedyre
    print("Her er alle beboerne på sykehjemmet: ")          #skriver ut tekst
    print("Knut Dahl")              #Skriver ut navnene
    print("Ole Hauger")
    print("Hanne Moss")
    #print(beboer.keys())
    navn = input("Skriv in navnet på en beboer i sykehjemet: ")     #spør bruker om hvem sin info som skal skrives ut
    if navn in beboer:                                      #Skjekker om navnet er i ordboken
        print("Her er " + navn + " sin matplan:")       #skriver ut i navnet i terminalen
        print(" Frokost: " + beboer[navn][0])           #skriver ur forkost
        print(" Lunsj: " + beboer[navn][1])             #Skriver ut lunsj
        print(" Middag: " + beboer[navn][2])            #skriver ut middag
    else:                                                   #Vis ikke
        print("Beboeren er ikke registrert")            #Skriv ut beboer er ikke registrert

sykehjemUtskrift()          #kaller på prosedyren

"""Oppgave 3
    a) jeg ville brukt en ordbok om man skal linke brukernavn med navn, men en liste om det bare er brukernavn.
    b) Jeg ville brukt en ordbok, for å kunne ha brukernavn som nøkkelverdier og poengen som innholdsverdiene
    c) Jeg ville brukt liste, fordi det bare er et element (nanvet på vinneren) som skal tas vare på.
    d) Jeg ville brukt en mengde, sånn at om noen er alergiske mot det samme blir det bare tat vare på en gang
    og det er bedre oversikt.
"""
