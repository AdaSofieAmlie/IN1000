
"""
Dette programmet tar in data fra andre filer.
Med denne datan lager programmet en ordbok.
Så blir ordboken brukt for å sammenøligne verdiene med andre data fra en annen fil for å se om det er ny varmerekord.
Og skriver over den nye
Etter det skriver programmet ut den oppdaterte dataen i en ny fil.
"""

#Oppgave 1
def maxTemp(fil):                           #Lager en funksjon som tar in fil som parameter
    maxTempFil = open(fil)                      #Åpner filen under variabel navnet maxTempFil
    maxTempDict = {}                            #Lager en tom ordbok
    for linje in maxTempFil:                    #Leger for løkke som går like lenge som antall linjeri filen
        biter = linje.split(",")                  #Splitter opp hver linje ved komma tegnet
        maaned = biter[0]                         #Deffinerer første elementet i linja som maaned
        temp = float(biter[1])                    #Deffinerer andre elementet i linjue som temp
        maxTempDict[maaned] = temp                #Legger til begge elementene i ordboken, med maaned som nøkkelverdi og temp som innholdsverdi
    maxTempFil.close()                          #Lukker filen jeg var i
    return maxTempDict                          #returnerer ordboken med alle dataen fra filen

#Oppgave 2 og 3
def sammenlign(ordbok, filnavn):            #Lager en funksjon med to parametre: ordbok og filnavn. Jeg kommer til å reffererer ordboken til ordboken.
    maxTempDict = ordbok                    #setter parametern ordbok under variabel navnet MAxTempDict
    dagligTempFil = open(filnavn)           #Åpner filen som ble gitt som parameter
    for linje in dagligTempFil:             #Lager en løkke som går like mange ganger som antal linjer i filen
        biter = linje.split(",")                #Splitter opp hver linje ved komme tegnet
        maaned = str(biter[0])                  #Deffinerer maaned til første elementet
        dato = int(biter[1])                    #setter andre elementet til variabel navnet dato
        dagTemp = float(biter[2])               #Setter tredje elementet til variabel navnet dagTemp
        for j in maxTempDict:                   #Lager en løkke som går like lenge som elementer i maxTempDict som ble sendt inn via parametere
            if maaned == j:                                 #sammenlinger temperaturen i januar fra filen og temperaturen i januas fra ordboken, og februar med februar osv
                tempMaxMaaned = float(maxTempDict[j])       #Setter max temperaturen til temperaturen fra ordboken
                if tempMaxMaaned < dagTemp:                 #skjekker om temperaturen fra ordboken er mindere enn en av temperaturene fra fil linjen sin data
                    tempMaxMaaned = dagTemp                     #Om mindere, endrer jeg max verdien til den nye
                    print("Ny varmerekord på " + str(dato) +" " + maaned + ": " + str(tempMaxMaaned) + " grader celcius.")          #Skriver ut den nye varmerekorden
                    print("(Den gamle varmerekorden i " + maaned + " var: " + str(maxTempDict[maaned]) + " garder celcius.)")       #Skriver ut den gamle varmerekorden
                    maxTempDict[maaned] = tempMaxMaaned         #Legger til den nye varmerekorden over den gamle i ordboken
    dagligTempFil.close()       #Lukker filen
    return maxTempDict          #Returnerer ordboken

#Oppgave 4
def skrivIFil(oppdatertOrdbok, filnavn):                #Lager en prosedyre med to parametre, ordbok og filnavn
    fil = open(filnavn, "w")                            #åpner filen, og legger til rette at jeg skal skrive (w) i den
    maxTempDict = oppdatertOrdbok                       #Legger ordbokparameteren under variabelnavnet MaxTempDict
    #print(maxTempDict) #Skjekk for meg selv, for å se hva som er i ordboken
    for i in maxTempDict:                                       #lager en løkke som går like mange ganger som elementer i ordboken
        fil.write(str(i) +", " + str(maxTempDict[i]) + "\n")            #Skriver i filen
    fil.close()         #Lukker filen

def hovedprogram():             #Lager et hovedprogram, for å kunn ha lokale 
    maxTempDict = maxTemp("max_temperatures_per_month.csv")             #legger funksjons kallet i en variabel, for letter håndtering
    print(maxTempDict)                                                          #Skriver ut funskjonen
    #sammenlign = sammenlign(maxTempDict, "max_daily_temperature_2018.csv")
    print(sammenlign(maxTempDict, "max_daily_temperature_2018.csv"))            #Printer ut resutlatet av funksjonen sammenlign
    skrivIFil(maxTempDict, "max_temp_month_adasam.csv")         #Kaller på prosedyren

hovedprogram()          #Kaller på hovedprogrammet


#Oppgave 5

def varmeBolgeSkjekk(filnavn):
    fil = open(filnavn)


filNavn = "max_daily_temperature_2018"
varmeBolgeSkjekk(filNavn)
