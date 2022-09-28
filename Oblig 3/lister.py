
"""
Dette er et program som jobber med lister, beregninger av lister, legge til elementer i lister.
"""

#Oppgave 1
tallListe = [1,2,3]         #Lager en liste med tall
tallListe.append(4)         #Legger på 4 på slutten av listen

print(tallListe[0])         #Skriver ut første elementet i lista
print(tallListe[2])         #Skriver ut tredje elementet i lista

#Oppgave 2
navnListe = []                      #Lager tom liste
navn0 = input("Skriv inn navn:")        #Spør om navn
navnListe.append(navn0)                 #Legger navnet til i listen
navn1 = input("Skriv inn navn:")
navnListe.append(navn1)
navn2 = input("Skriv inn navn:")
navnListe.append(navn2)
navn3 = input("Skriv inn navn:")
navnListe.append(navn3)
#print(navnListe2)      #Skriver ut listen for å skjekke

"""Eller
navnListe2 = [                           #Liste
    input("Skriv inn et navn:"),        #Spør om navn i hvert element som legges inn automatisk
    input("Skriv inn et navn:"),
    input("Skriv inn et navn:"),
    input("Skriv inn et navn:")
    ]
print(navnListe)
"""

#Oppgave3
mittNavn = "Ada Sofie"          #Skriver en variabel med mitt navn

if mittNavn in navnListe:           #Skjekker om variable verdien er i listen
    print("Du husket meg!")             #Skriver ut i terminalen
else:                               #Om verdien ikke er i listen
    print("Glemte du meg?")             #Skriver ut i terminalen

#Oppgave 4
summen = tallListe[0] + tallListe[1] + tallListe[2] + tallListe[3]          #Regner ut summen, føler det kan gjøres lettere med en for løkke
#print(summen)
produkt = tallListe[0] * tallListe[1] * tallListe[2] * tallListe[3]         #Regner ut produktet, ^^
#print(produkt)

beregninger = []                    #Lager en tom liste
beregninger.append(summen)          #Legger til summen elementet
beregninger.append(produkt)         #Legger til produkt elementet

sammen = []         #Lager en tom liste
sammen = tallListe + beregninger        #Legger to lister sammen til en
print(sammen)       #skriver ut i terminalen

sammen.pop(5)       #Tar vekk verdien på index nr 5
sammen.pop(4)       #Tar vekk verdien på index nr 4
