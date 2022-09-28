"""
Dette er et program som omhandler ordbøk, hvordan man skriver dem og legger til nøkkelverdier og innholdsverdier
"""

#Oppgave 1
ordbok = {                  #Lager en ordbok med forskjellige "Nøkkelverdier": innholdsverdier
    "Melk": 14.90,
    "Brød": 24.90,
    "Yoghurt": 12.90,
    "Pizza": 39.90
    }
print(ordbok)

#Oppgave 2
mat1 = (input("Skriv inn en matvare:"))             #Spør brukeren om en matvare
ordbok[mat1] = float(input("Skriv inn prisen"))         #Legger til matvaren og prisen
mat2 = (input("Skriv inn en matvare til:"))             #Spør brukeren om en til matvare
ordbok[mat2] = float(input("Skriv inn prisen"))         #Legger til matvare nr 2 og prisen

print(ordbok)
