

"""
Dette er et program som henter en klasse fra en annen fil og tar den i bruk.
Programmet lager et objekt i kalssen og bruker metodene.
Programmet har og en if test for å se om objektet har en spesiel verdi eller en annen.
"""

from dato import Dato       #Henter Dato klassen fra dato.py

#Oppgave 3
def hovedprogram():                 #lager et hovedprogram
    dato1 = Dato(15,8,2020)         #lager et objekt i kalsse dato
    print(dato1.lesAar())           #Skriver ut aaret til dato1 ved hjelp av metoden lesAar
    if dato1.lesDag() == 15:        #om dato1 sin dag er 15
        print("Loenningsdag")           #Skriver ut i terminalen
    elif dato1.lesDag() == 1:       #Else om dato1 sin dag er 1
        print("Ny maaned, nye muligheter")      #Printer ut i terminalen
    dato1.skrivUt()                 # lager dato som en streng og skriver den ut

hovedprogram()      #Kaller på hovedprogram
