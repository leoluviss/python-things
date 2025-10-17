from random import *

z="oui"

while z=="oui":
    p=1
    f=2
    n=0

    a=str(input("Pile ou face ? "))

    if a=="pile":
        n=int(uniform(1,3))
        if n==p:
            print("Gagné")
        else:
            print("Perdu")
    elif a=="face":
        n=int(uniform(1,3))
        if n==f:
            print("Gagné")
        else:
            print("Perdu")
    else:
        print("Erreur")

    z=str(input("Continuer ? oui ou non ? "))