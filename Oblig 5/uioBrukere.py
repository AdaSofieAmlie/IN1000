
"""
Dette programmet tar in navn til elever og lager brukernavn til dem
Så lager den en "mail" til hver av brukernavnene, med bruker valgt suffixStr
Så skriver den ut alle mailene som blir laget ut fra en ordbok.
Deretter spør programmet om komandoer, helt til brukeren sier s, som gjør forksjellige ting.
"""
#Oppgaev 2
def lagBrukernavn(navn):       #lager en funskjon som tar in en parameter
    navnSmå = navn.lower()      #Gjør om parametern til bare små bokstaver
    navnListe = navnSmå.split()     #Splitter navnet ved mellomromm, så du får to deler, et fornavn og et etternavn
    fornavn = navnListe[0]     #Setter fornavn til første elementet
    etternavn = navnListe[1]    #Setter etternvn til andre elementet
    etternavnListe = list(etternavn)    #Lager en liste av etternavnet
    brukernavn = fornavn + etternavnListe[0]        #Lager brukernavn av fornanvn og første bokstav av etternavn
    return brukernavn       #Returnerer brukernavnet

#Oppgave 3
def lagEpost(brukernavn, suffix):       #funksjon med to prosedyrer; brukernavn og suffix
    bruker = str(brukernavn)                #setter brukernavn til string av parameteren brukernavn
    suffixStr = str(suffix)                 #Setter brukernavn til string av parameteren suffix
    epost = bruker + "@" + suffixStr        #LAger epost av variablene
    return epost                #Returnerer eposten

#Oppgave 4
def printEpost(ordbok):             #Prosedyre som tar in en ordbok parameter
    for i in ordbok:                    #for løkke like lang som ordboken
        print(lagEpost(i, ordbok[i]))       #Skrivr ut nøkkelverdi og innholdsverdi

def hovedprogram():             #Hovedprogram prosedyre
    #Oppgave 1
    ordbokTom = {}      #Lager en tom liste

    bNavn = lagBrukernavn("Kari Nordmann")      #Lager brukernavn til KAri Nordmann
    print(bNavn)                #Printer det ut
    epost = (lagEpost(bNavn, "student.matnat.uio.no"))          #LAger epost til kari
    print(epost)        #Printer det ut
    #Oppgave 4 continued
    testOrdbok = {"olan" : "ifi.uio.no" , "karian": "student.matnat.uio.no"}        #Lager en testordbok
    for i in testOrdbok:                        #For løkke like lang som testordboken
        ePoster = lagEpost(i,testOrdbok[i])         #LAger epost til hver enkelt element i ordboken
        print(ePoster)              #Skriver ut hver enkelt epost

    #Oppgave 5
    brukerInput = input("Skriv in  en kommando (i,p,s): ")      #Spør om input
    while brukerInput != "s":                   #While løke som går så lenge inoutten ikke er s
        if (brukerInput == "i"):                        #Om input er i
            navn = input("Skriv in hele navnet ditt: ")     #Spør om navn
            suffix = input("Skriv in suffix: ")             #Spør om suffix
            brukernavn = lagBrukernavn(navn)                #LAger brukernavn
            ordbokTom[brukernavn] = suffix                  #Legger til i tom ordbok fra oppgave 1
        elif (brukerInput == "p"):                      #Om input er p
            printEpost(ordbokTom)                           #kaller på epost funksjonen med ordboken som argument
        brukerInput = input("Skriv in en kommando (i,p,s): ")   #Spør om ny kommando

hovedprogram()      #Kaller på hovedprogramm

"""
***
Her prøde jeg å løse oppgave 7, men jeg klarte det ikke :(
***

#Oppgave 7
def lagBrukernavn(navn, ordbok):
    navnSmå = navn.lower()
    navnListe = navnSmå.split()
    fornavn = navnListe[0].lower()
    etternavn = navnListe[1].lower()
    etternavnListe = list(etternavn)

    oBok = ordbok
    brukernavn = fornavn + etternavnListe[0]
    print(brukernavn)
    for i in oBok:
        for j in range(1,len(etternavnListe)):
            if (oBok[i] == brukernavn):
                brukernavn += etternavnListe[j]
    oBok[navn] = brukernavn
    return ordbok

def oppgave7():
    brukernavnOrdbok = {"Emma Alnes": "emmaa", "Emma Andresen": "emmaan"}
    lagnavn = lagBrukernavn("Emma Andersen", brukernavnOrdbok)
    print(lagnavn)

oppgave7()
"""
