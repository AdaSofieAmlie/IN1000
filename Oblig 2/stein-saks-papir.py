
"""
Oppgavetekst:
I denne oppgaven skal du lage et program som lar brukeren spille Stein , Saks, Papir med maskinen.
Brukeren skal selv skrive inn sitt valg, også finne ut om brukeren vant eller ikke.
Du kan sette maskinens valg til Saks, eller gjøre så det blir forskjellig hver gang.
"""

#pcValg = "Saks"        eks. på hvordan man kan hardkode inn maskinens valg under får jeg et tilfeldig valg fra maskinen

alternativer = ["stein", "saks", "papir"]       #Alternativene maskinen kan velge mellom
import random
tilfeldigTall = random.randint(0,2)             #Finner et tilfeldig tall som skal kalle på et av alternativene i alernativ arrayen

#print( tilfeldigTall)              Skjekker at det ble riktig
pcValg = alternativer[tilfeldigTall]        #Kaller på et av alternativene tilfeldigvis, ved hjelp av array og random tall
#print(pcValg)          Skjekker at det ble riktig
pcValgUtskrift = "Maskinen valgte " + pcValg        #Lager en variabel som skal skrives ut senere

print("*  *   *   STEIN, SAKS, PAPIR  *   *   *")           #Oppgave teksent for brukeren
print("Du skal velge endten Stein, Saks, eller Papir.")
print("Du spiller mot maskinen.")
print("Lykke til!")
print()

brukerValg = input("Hva velger du? ")                 #Brukeren velger Stein, Saks, eller Papir

if  brukerValg == pcValg:                    #Sjekker om det er likt mellom dem
    print(pcValgUtskrift)                           #Skrier ut variabelen jeg skrev tidligere i koden
    print("Det ble likt!")                          #Skriver ut resultatet
elif brukerValg == "stein":                 #Sjekker om bruker valgte stein
    if pcValg == "papir":                       #Sjekker om pc valgte papir
        print(pcValgUtskrift)                       #Skrier ut variabelen jeg skrev tidligere i koden
        print("Du tapte")                           #Skriver ut resultatet
    else:                                       # Om pc ikke valgte papir eller stein
        print(pcValgUtskrift)                       #Skrier ut variabelen jeg skrev tidligere i koden
        print("Du vant!")                           #Skrier ut resultatet
elif brukerValg == "papir":                 #Sjekker om bruker valgte papir
    if pcValg == "saks":                        #Sjekker om pc valgte saks
        print(pcValgUtskrift)
        print("Du tapte")
    else:                                       #Sjekk om pc valgte noe annet enn papir og saks, altså valgt stein
        print(pcValgUtskrift)
        print("Du vant!")
elif brukerValg == "saks":                  #Sjekker om bruker valgte saks
    if pcValg == "stein":                       #Sjekker om pc valgte stein
        print(pcValgUtskrift)
        print("Du tapte")
    else:                                       #Sjekker om pc valgte  annet enn saks og stein, altså papir
        print(pcValgUtskrift)
        print("Du vant!")
else:                                       #Sjekker om brukeren skrev et valg som ikke er mulig
    print("Det forsto jeg ikke")                #Sier ifra at det brukeren skrev ikke godkjennes av systemet
