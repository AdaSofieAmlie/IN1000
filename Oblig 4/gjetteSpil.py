
"""
Skriv et program som lar brukkeren gjette et tall maskinen velger mello 1 og 20.
Bruk en for-løkke til å lage en liste med alle mulige valg, og bruk velg ut en verdi til maskinens valg.
Spør om brukrens gjette forsøk og skjør en while løkke helt til den gjettet riktig.
Skriv ut at det ble riktig og hvor mange forsøk brukeren brukte.
"""
import random

tallMulig = []              #Tom liste
for i in range(1,26):           #Skriver inn alle veridene fra 1-25 i en liste
    tallMulig.append(i)
    i += 1

#Uten random:
#tallValgtPc = 15              For eksempel

tilfeldigTall = random.randint(0,24)                 #Finner ett rndom tall som index
tallValgtPc = tallMulig[tilfeldigTall]              #lager en variable med mackinens tall
print(tallValgtPc)                                      #Juks, for å lett sjekke

print("Maskinen har vagt et tall mellom 1 og 20")           #instruksjon til bruker
gjettet = int(input("Gjett hvilket tall maskinen har valgt: "))         #Henter input

forsok = []                                     #Tom liste
while gjettet != tallValgtPc:                   #Går så lenge brukeren gjetter feil
    forsok.append(gjettet)                      #Legger til forsøk i tom liste
    gjettet = int(input("Prøv igjenn: "))       #Ny input

print("Du klarte det!")                         #Når while løkken er feridg betyr det at brukeren har gjettet riktig
print("Du brukte " + str(len(forsok) + 1) + " forsøk.")         #Skriver ut antall forsøk
