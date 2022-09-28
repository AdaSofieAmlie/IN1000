
"""
Dette programmet er beregningsprogram for skreddere med en
funksjon som leser inn en fil (som du lager selv og leverer sammen med de andre
filene) der hver linje beskriver et navn på et mål og selve målet i tommer.
Programmet legger disse målene i en ordbok med navn på målet som nøkkelverdi
og returner ordboken. Så har programmet en prosedyre som tar imot en liste av mål og
benytter seg av tommerTilCm
"""

def beregn(filnavn, ordbok):        #funskjon med to parametre
    fil = open(filnavn)                 #Åpner filen
    oBok = ordbok                       #deffinere ordbok variabel
    for linje in fil:                   #For løkke like lang som antall linjer i fil
        biter = linje.split()               #Spliter linjen
        navn = biter[0]                     #Førte elementer er navn
        maal = float(biter[1])              #Andre elementet er mål
        oBok[navn] = maal                   #Legger til i ordbok
    fil.close()                         #Lukker fil
    return oBok                     #Returnerer ordbok

def tommerTilCm(liste):         #funksjon med en parameter
    cmListe = []                    #Tom cm liste
    for i in range(len(liste)):         #For løkke like lang som lengden av lsute parameteret
        assert liste[i] > 0             #Skjekker at liste elementet er større en 0
        forskjell = 2.54                #Forskjellen variable
        cm = liste[i] * forskjell       #Regner om til sm
        cmListe.append(cm)              #legger til cm i listen
    return cmListe              #returnerer cm listen

def hovedprogram():         #prosedyre hovedprogram
    ordBokTom = {}              #Tom ordbok
    beregnObok = beregn("skredderFil.csv", ordBokTom)   #Kaller på beregn funksjon med argumenter
    print(beregnObok)                       #Printer kallet på funksjonen
    listeTommer = [1,2,3]                   #Liste med tommer
    tomme = tommerTilCm(listeTommer)        #KAller på tammer til cm funksjon
    print(tomme)                            #printer kallet på funksjonen over

hovedprogram()          #Kaller på hovedprogrammet
