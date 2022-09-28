"""
Dette programmet spør om navn på bruker og gjør beregninger med variabler.
"""

print("Hei Student!")       #Skriver ut Hei Student! i terminalen

navn1 = input("Hva er ditt navn?")      #Spør om navnet i terminalen, svaret er variablen a
print("Hei " + navn1)               #Skriver ut variablen navnet

x = 20
y = 12          #To heltalsverdi variabler
print(x)
print(y)        #Skriver ut verdiene fra variablene i terminalen

diff = x - y       #Regner ut differansen mellom de to variablene
print( "Differansen: " + str(diff))       #Skriver ut i terminalen

navn2 = input("Hva er din bestevenns navn?")     #Spør om navnet i terminalen, svret er variabelen b
sammen = navn1 + navn2       #Legger sammen navnene i en variabel
print(sammen)        #Skriver ut hele navnet

sammen2 = navn1 + " og " + navn2             #Legger en og mellom navnene
print(sammen2)                       #Skriver d ut i terminalen
