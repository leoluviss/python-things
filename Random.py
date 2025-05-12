from random import *

z = str(input("Entier ou Décimal ? "))
a = float(input("Nombre Minimum ? "))
b = float(input("Nombre Maximum ? "))

if z == "Entier":
    y = int(uniform(a, b))
    print(y)
elif z == "Décimal":
    x = float(uniform(a, b))
    print(x)
else:
    print(0)
