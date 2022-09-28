"""
Dette programmet regner ut summen av to tall.
I tillegg teller det forekomster av en bokstav i en streng med tekst fra brukeren og skriver ut resultatet.
"""

#Oppgave 1
def adder(tall1, tall2):                #Lager en funksjon som tar inn to parametere
    sum = tall1 + tall2                     #Adderer sammen de to parameterer
    return sum                              #Returnerer summen

adder(4,6)              #Kaller på funksjonen, med 4 og 6 som hvert sitt argument
adder(12,6)             #Samme som over, men m 12 og 6

print("4 + 6 = " + (str(adder(4,6))))       #Skriver ut i terminalen
print("12 + 6 = " + (str(adder(12,6))))         #Skriver ut i terminalen

#Oppgave 2
print()
#Skriver ut instrukser til bruker
print("Her skal du skrive inn en streng med bokstaver, både store og små.")
print("Så skal du skrive inn en bokstav for å se hvor mange ganger den forekommer i strengen i sitt format(stor eller liten)")
"""
*** Dette blir byttet ut med det jeg gjorde i oppgave 3 ***
streng = input("Skriv inn en streng med bokstaver:")
bokstav = input("Skriv inn en bokstav:")

if bokstav in streng:
    #print("ja")
    svar = streng.count(bokstav)
    print("Det er " +  str(svar) +" forekomster av " + bokstav + " i strengen du skrev ut")
else:
    print("den bokstaven er ikke i strengen du skrev inn.")
"""
#Oppgave 3
streng = input("Skriv inn en tekst:")       #Spør etter input fra bruker
bokstav = input("Skriv inn en bokstav:")    #Spør etter input fra bruker

def tellForekomst(minTekst, minBokstav):        #LAger en funksjon med to parametere
    if minBokstav in minTekst:                      #Skjekker om bokstav argumentet er i tekst argumentet via parameterene
        svar = minTekst.count(minBokstav)               #Om ja: teler programmet hvor mange ganger den bokstaven finnes
    else:                                           #Vis ikke
        svar = 0                                        #Finnes ikke = 0
    return svar                                     #Returnerer svaret

svaret = tellForekomst(streng, bokstav)             #Kaller på funksjonen i en variabel for å ta med retur verdien videre
print("Det er " + str(svaret) + " forekomster av " + bokstav + " i teksten du skrev ut")            #Skriver ut i terminalen
