"""
Dette er et program som ber et enket ja/nei spørsmål,
som svarer tilbake med tane på hva brukeren svarer
"""

svar = input("Kunne de tenke seg en brus?")        #Spør om brukern har lyst på brus

if svar == "ja":                    #Vis svaret er ja, får brukeren en brus
    print("Her har du en brus!")
elif svar == "nei":                 #Vis svaret er nei, får brukeren ikke en brus
    print("Den er grei")
else:                               #Vis svaret er noe annet, programmet forstår ikke det.
    print("Det forsto jeg ikke helt")
