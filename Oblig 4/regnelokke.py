
"""
Dette programmet bruker en while løkke helt til brukeren skriver inn tallet 0,
de andre tallene brukeren velger blir lagt inn i en liste.
Denne listen skriver jeg ut så finner jeg summen av hele listen.
Deretter finner jeg det størtse og minste tallet i listen og skriver de ut.
"""

#Oppgave 1 og 2
tall = int(input("Skriv inn et tall: "))        #Spør bruker om et tall via input
tallForsok = []                                 #Tom liste for forsøkene til bruker
while tall>0:                                   #Så lenge inputen er større en 0 vil denn eløkken holde på
    tallForsok.append(tall)                     #Legger til forsæke i listen
    tall = int(input("Prøv igjen: "))           #Ber bruker om å prøve igjen
#print(tallForsok)  for skjekk

#Oppgave 3
for i in range (0, (len(tallForsok))):          #For i fra 0 til lengden av listen
    print(tallForsok[i])                        #Skriver ut hvert element helt til i har nådd enden av listen

#Oppgave 4
minSum = 0                                      #Sum starter på 0
for i in range (0, (len(tallForsok))):          #Går like mange ganger som lengden av forsøk listen
    minSum += tallForsok[i]                     #Legger til hvert element fra listen til summen
print("Sum: " + str(minSum))                    #Skriv ut i terminalen

#Oppgave 5
tall1 = 0                                       #setter en standar lav som skal skjekes opptil
for i in range (0, (len(tallForsok))):          #Går igjennom like mange ganger som lengden av forsøk listen
    if (tallForsok[i] > tall1):                 #Om forsøk er større enn tall1
        tall1 = tallForsok[i]                   #Gjør om tall 1 til forsøk tallet
print("Det største tallet er: " + str(tall1))   #Printer ut det største tallet

tall2 = tallForsok[0]                                     #setter en standar som skal skjekes opptil
for i in range(1,(len(tallForsok))):                       #Går igjennom like mange ganger som lengden av forsøk listen
    if (tall2 > (tallForsok[i])):                          #If forsøket et mindere en tallet
        tall2 = tallForsok[i]                              #Tallet er lik forsøket
print("Det minste tallet er (bortsett fra 0): " + str(tall2))       #Printer ut
