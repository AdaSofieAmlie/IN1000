"""
Dette programmet ber om og tar vare på to datoer. Disse to datoene blir sammenlignet.
Om brukeren har skrevet dem i rikkitg rekkefølge, kronologisk, vil programet si at det er riktig.
Om ikke vil det stå feil rekkefølge.
"""
print("*Skriv in to datoer hver for seg og skjekk om det er i riktig rekkefølge. Skriv som mm.dd")

a = int(input("skriv in en måned?"))        #Spør om en dato
b = int(input("Skriv in en dag?"))

c = int(input("skriv in en annen måned?"))         #spør om en dato til
d = int(input("Skriv in en annen dag?"))

if a < c and b < d:                            #Vis måneden i dato nr 1 og dagen i dato nr 1 er mindere (aka tidligere)
    print("Riktig rekkefølge!")                     #Skriv ut "riktig rekkefølge"
elif a == c and b == d:                         #Hvis dato1 er samme som dato2
    print("Samme dato!")                           #Skriv ut "samme dato"
elif a == c:
    if b < d:
        print("Riktig rekkefølge!")
    else:
        print("Feil rekkefølge!")
else:                                           #Alle andre mulgiheter
    print("Feil rekkefølge!")                       #Skriv ut "Feil rekkefølge"
