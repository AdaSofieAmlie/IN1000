
""" Oppgave tekst:
Du skal lage et program som viser en word search med 7-12 ord av en kategori, for eksempel dyr eller frukt og grønt.
Du skal så la brukeren prøve å finne 5 ord. Bruk en liste med alle ordene i word searchen for å skjekke om brukeren
har skrevet inn et gyldig ord. Om brukeren finner et riktig ord skal du gi brukeren et poeng. (TIPS! Du kan bruke en liste
og legge til ett nytt element hver gang og finne elngden av den som poengteller.)
"""

#Beskriver for brukeren hva som sal gjøres
print("Word search: Finn 5 dyre ord! Du får et poeng for hver riktige dyr du finner.")
print("--------------------")           #Skriver inn en word search
print("A D K H U N D Y H W")
print("R G A Y G W K L E H")
print("O T T G L T F U G L")
print("T U T J E O W D R V")
print("T Ø H E S T S H I K")
print("E U Q X L H E A S A")
print("F I S K A T U J K N")
print("U G D U L V O S D I")
print("E S E L Y E T K Y N")
print("E H B K Y L L I N G")
print("--------------------")

#Liste med alle ordene som er gjemt i word searchen
dyrListe = [ "HUND", "KATT", "UGLE", "FUGL", "ROTTE", "HEST", "GRIS", "KANIN", "FISK", "ULV", "ESEL", "KYLLIG" ]
poeng = []      #Lager en tom poeng liste

def skjekkDyr():                                #Lager en prosedyre som spør brukeren om å skrive inn et dyr
    dyr = input("Skriv inn et dyr: ").upper()       #Spør om brukerens svar
    if dyr in dyrListe:                             #Skjekker om brukerens svar er i listen
        print("Der var du flink! Du fant: " + dyr)      #Skriver ut bra
        poeng.append(1)                             #Legger til et element i listen
    else:                                           #Om dyre ikke er i listen
        print("Beklager, " + dyr + " er ikke et at dyrene.")    #Skriver ut at det ikke er i word searchen

#kaller på prosedyren så mange ganger som brukeren skal få prøve å svare
skjekkDyr()
skjekkDyr()
skjekkDyr()
skjekkDyr()
skjekkDyr()

print("Du fikk: " + str(len(poeng)) + " poeng")         #Skriver ut poeng summen i terminalen
