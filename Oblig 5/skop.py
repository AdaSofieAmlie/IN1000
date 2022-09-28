
def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return b

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print(b)
    print(a)

hovedprogram()

"""
Først deffineres minFunksjon, som ikke skal ta inn noen parametere. Deretter definneres
hovedprogram prosedyren som heller ikke tar inn noen parametre. Deretter kalles hovedprogram.
Inne i hovedprogram deffineres variabel a til verdi 42 og variabel b til verdi 0. Deretter
prints ut varabel b, altså verdien 0 i terminalen. Deretter omdeffineres variabel b til a, altså 42.
Så kaller vi på minFunksjon. I minFunksjon er det en løkke som går fra 0 til 1, så løkken går to ganger.
i løkken deffineres variablen c til verdien 2, og printer ut c(2). Deretter legger jeg til 1 på
verdien i variabel c. Så blir variabelen b deffinert med verdien 10. Deretter pråver programmet
å legge til verdien fra variabelen a, men her kommer en error. Det er umulig og få tak i a, siden den
ikke ligger i det globale skopet.

"""
