
"""
Dette programmet henter en klasse fra en annen fil.
Programet spør om navn og alder og lager et objekt av brukerens svar.
Deretter spør programmet om hobbier helt til brukeren sier "ferdig".
Programmet skriver ut statistikken på slutten
"""

from Person import Person       #Henter person fra person.py

def hovedprogram():                 #definerer hovedprogram
    navn = input("Hva heter du? ")          #Spør om navn
    alder = int(input("Hvor gammel er du? "))   #Spør om alder
    bruker = Person(navn, alder)        #Lager et objekt
    hobby = input("Skriv in dine hobbyer(skriv ferdig når ferdig): ").lower()       #Spør om hobby
    while hobby != "ferdig":            #Så lenge bruker ikke sier ferdig
        bruker.leggTilHobby(hobby)      #Legger til hobby til objektet
        hobby = input("Skriv in dine hobbyer(skriv ferdig når ferdig): ").lower()   #Spør igjen
    bruker.skrivUt()        #Skriver ut statistikken
    
hovedprogram()      #Kaller på hovedprogrammet
