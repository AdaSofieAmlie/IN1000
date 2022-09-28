
"""
Dette programmet lar brukeren lage en reiseplan ved hjelp av en nøstet liste.
"""
#Oppgave 1 og 2
steder = []                                     #Tomme lister klare for input
klesplagg = []
avreisedatoer = []

for i in range(0,5):                                #Går igjennom 5 ganger
    sted = input("Skriv inn et reisemaal: ")        #Spør om reisemål
    steder.append(sted)                             #Legger til i liste
    klaer = input("Skriv inn et klesplagg: ")       #Spør om klesplagg
    klesplagg.append(klaer)                         #Legger til i liste
    dato = int(input("Skriv in avreise datoen: "))  #Spør om dato
    avreisedatoer.append(dato)                      #Legger til i liste

#Oppgave 3
reiseplan = []                      #Tom liste
reiseplan.append(steder)                #Legger til fylt inn loste av steder i reieplan
reiseplan.append(klesplagg)             #Legger til fylt inn loste av klær i reieplan
reiseplan.append(avreisedatoer)         #Legger til fylt inn loste av datoer i reieplan

#Oppgave 4
print(len(reiseplan))
for i in range(0,len(reiseplan)):                #Går igjennom 3 ganger
    print(reiseplan[i])             #Skriver ut de forskjellige listene

#Oppgave 5
i1 = int(input("Skriv in indeks til en av listene(0-2): "))         #Spør om input 1
i2 = int(input("Skriv in indeks til et element i listen(0-4): "))       #Spør om input 2

if (0<=i1<=(len(reiseplan)-1)) and (0<=i2<=(len(reiseplan[i1])-1)):           #Skjekker om indeksene er innefor rekevidder
    print(reiseplan[i1][i2])                #Skriver ut det brukeren vil ha fram
else:                                   #Om ikke
    print("Ugyldig input!")                 #Skriver ut ugyldig input
