
"""
Dette er et program som definerer en klasse og en del metoder objekten i klassen har nytte av
"""

class Person():                         #Lager en klasse
    def __init__(self, navn, alder):        #konduktør med to argumenter
        self._navn = navn                       #definerer self:_navn til navn
        self._alder = alder                     #Definerer self._alder til alder
        self._liste = []                        #Lager en tom liste til det objektet
    def leggTilHobby(self, hobby):          #Metode for å legge til hobby i liste
        self._liste.append(hobby)               #legger til hobby i liste
    def skrivUtHobby(self):                 #Skriv ut hobby metode
        svar = "Hobbier: "                      #Svar variabel
        for i in range(len(self._liste)):       #For løkke som går like mange ganger som lengden til listen
            svar += self._liste[i] + ", "           #Legger til liste elementet i svar variablenen
        print(svar)                             #PRintr ut svaret
    def skrivUt(self):                      #Skriver ut metode
        print("Navn: " + self._navn)            #Skriver ut navnet
        print("Alder: " + str(self._alder))     #Skriver ut alder
        self.skrivUtHobby()                     #Kaller på metoden over, somskriver ut hobbyene
#Slutten av klassen
