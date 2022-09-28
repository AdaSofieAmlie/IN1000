

"""
Dette programmet henter en klasse fra et annet dokument og bruker den.
Programmet lager tre objekter innenfor klassen, med tre argumenter hvær.
Så bruker programmet metoder fra klassen til å skrive ut objektene
Deretter bruker den en annen metode for å legge til km i kilometeravstanden og
printer den ut.
"""
#oppgave 5
from motorsykkel import Motorsykkel                     #importerer klassen fra filen

def hovedprogram():                                     #Lager et hovedprogram
    #Oppgave 6
    ms1 = Motorsykkel("BMW", "BT86374", "30000")        #oppretter et ovjekt av klassen motorsykkel
    ms2 = Motorsykkel("Honda", "PC87201", "45630")      #oppretter et ovjekt av klassen motorsykkel
    ms3 = Motorsykkel("Volvo", "DP36021", "29800")      #oppretter et ovjekt av klassen motorsykkel

    ms1.skrivUt()       #Kaller på metoden skrivUt fra klassen
    ms2.skrivUt()       #Kaller på metoden skrivUt fra klassen
    ms3.skrivUt()       #Kaller på metoden skrivUt fra klassen

    #Oppgave 7
    ms3.kjor(10)                                #Kaller på kjor metoden, som legger til 10 (argumentet) i killometeravstanden
    assert ms3.hentKilometerstand() == 29810    #Skjekker at svaret blir et jeg tror det vill
    print(ms3.hentKilometerstand())             #Skriver ut den nye kilometeravstanden
#Oppgave 8 haha
hovedprogram()      #kaller på hovedprogrammet
