"""
1. Er dette lovlig kode? Begrunn svaret.
    Nei, dette er ikke en lovelig kode. Fordi python vil ikke skrive ut en integer og en string i samme print
2. Hvilke problemer vil vi kunne møte på når vi kjører denne koden?
    At tallet er int sammen med str. De må være samme type.
"""

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print(b + "Hei!")
