"""Dette er et program som konverterer grader fra en enhet til en annen"""

print("Oppgi en verdi i farenheit og programmet vil konvertere det til celcius")        #instruksjon til bruker

#Oppgave 1
tempF = 75          #Variabel som bærer en fahrenheit verdi

#Oppgave 5
tempF = int(input("Oppgi grader i fahrenheit: "))
#Oppgave 2
print("Temperaturen i fahrenheit: " + str(tempF))        #Skriver det ut i terminalen

#Oppgave 3
tempC = ((tempF - 32) * 5/9)                    #Omregner til celcius
#oppgave 4
print("Temperaturen i celcius: " + str(tempC))                 #Skriver det ut i terminalen
