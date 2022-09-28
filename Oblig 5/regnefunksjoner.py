
"""
Dette programmet adderer, substraherer, og dividerer to tall ved hjelp av funksjoner.
I tillegg kan brukeren skrive inn egene tall som beregnes med.
Programmet regner og om en enhet fra tommer til cm.
"""
#Oppgave 1
def addisjon(tall1, tall2):         #Lager en funksjon med parametre
    sum = tall1 + tall2             #Legger parameterene sammen
    return sum                      #returnerer svaret

#Oppgave 2
def subtraksjon(tall1, tall2):      #Lager en funksjon med parametre
    sum = tall1 - tall2             #Substraherer parameterne
    return sum                      #Returnerer svaret

def divisjon(tall1,tall2):          #Lager en funksjon med parametre
    sum = tall1/tall2               #Deler parametre på hverandre
    return sum                      #Returnerer svaret

#Oppgave 3
def tommerTilCm(antallTommer):          #LAger en funksjon med antallTommer som parameter
    assert antallTommer > 0             #Skjekker at parameteren ikke er mindere enn 0
    forskjell = 2.54                    #Deffinerer forskjellen
    cm = antallTommer * forskjell       #Regner om til cm
    return cm                           #Returnerer cm

#Oppgave 4
def skrivBeregninger():                                                         #LAger en funskjon som ikke tar inn parametere
    tall1 = float(input("Skriv inn et tall: "))                                 #Spør om to tall fra bruker
    tall2 = float(input("Skriv inn et annet tall: "))
    print("Utregninger:")                                                       #Skriver ut
    print("Resultatet av summering: " + str(addisjon(tall1, tall2)))            #Skriver ut, regner ut via addisjon funskjoen av brukerens tall
    print("Reslutatet av substraksjon er: " + str(subtraksjon(tall1, tall2)))   #Skriver ut, regner ut via subbstraksjon funskjoen av brukerens tall
    print("Resultatet av divisjon er : " + str(divisjon(tall1, tall2)))         #Skriver ut, regner ut via divisjon funskjoen av brukerens tall
    tomme = float(input("Skriv inn ett tall i tommer: "))                       #Ber om en enhet i tommer
    print("Det er " + str(tommerTilCm(tomme)) + " cm.")                         ##Skriver ut, regner om via tommerTilCm funskjoen av brukerens tall

def hovedprogram():
    #Skjekker assert med addisjon, for å sikkre meg på at funksjonen gjør det jeg tror den skal
    assert addisjon(4,4) == 8
    assert addisjon(-2,-2) == -4
    assert addisjon(-6,10) == 4
    #Skjekker assert med substraksjon, for å sikkre meg på at funksjonen gjør det jeg tror den skal
    assert subtraksjon(5,2) == 3
    assert subtraksjon(-10,-2) == -8
    assert subtraksjon(10,-7) == 17
    #Skjekker assert med divisjon, for å sikkre meg på at funksjonen gjør det jeg tror den skal
    assert divisjon(10,5) == 2
    assert divisjon(-30,-3) == 10
    assert divisjon(4,-2) == -2
    #Kaller på skrivBeregninger funksjonen
    skrivBeregninger()

hovedprogram()              #Kaller på hovedprogrammet
