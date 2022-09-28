
"""
Dette programmet ber om alder og forteller brukeren hva billettprisen er for brukeren.
"""

def alder():                                    #Prosdyre
    alder = int(input("hvor gammel er du?"))        #Spør om hvor gammel brukeren er
    billettpris = 0                                 #Setter bilett prisen til 0 midlertidlig
    if alder <= 17:                 #Skjekker om alder er under eller lik 17 år
        billettpris = 30                #vis true; settes bilett pris til 30
    elif alder >= 63:               #Skjekker om alder er over eller er lig 63 år
        billettpris = 35                #Vis true; setter bilett pris til 35
    else:                           #Ellers er alder mellom 18 og 62 år
        billettpris = 50                #Setter bilettpris til 50
    print("billettprisen er: " + str(billettpris))              #Skriver ut bilettprisen

alder()             #Kaller på prosedyren
