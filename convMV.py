from time import *

x = float(input("Donner la valeur du numérateur ? "))
y = float(input("Donner la valeur du dénominateur ? "))
a = str(input("Donner l'unité du numérateur ? "))
b = str(input("Donner l'unité du dénominateur ? "))

print(x, a, "/", y, b)
print("Mv =", x / y, a, "/", b)

c = int(input("Transformer le numérateur (1) ou le dénominateur (2) ? "))
d = str(input("Transformer l'unité en ? "))


if a == "kg":
    f = 7
elif a == "hg":
    f = 6
elif a == "dag":
    f = 5
elif a == "g":
    f = 4
elif a == "dg":
    f = 3
elif a == "cg":
    f = 2
elif a == "mg":
    f = 1
else:
    print("Erreur")

if d == "kg":
    e = 7
    a = d
elif d == "hg":
    e = 6
    a = d
elif d == "dag":
    e = 5
    a = d
elif d == "g":
    e = 4
    a = d
elif d == "dg":
    e = 3
    a = d
elif d == "cg":
    e = 2
    a = d
elif d == "mg":
    e = 1
    a = d
else:
    print("Erreur")


if c == 1:
    g = f - e
    if g == -6:
        x = x / 1000000
    elif g == -5:
        x = x / 100000
    elif g == -4:
        x = x / 10000
    elif g == -3:
        x = x / 1000
    elif g == -2:
        x = x / 100
    elif g == -1:
        x = x / 10
    elif g == 1:
        x = x * 10
    elif g == 2:
        x = x * 100
    elif g == 3:
        x = x * 1000
    elif g == 4:
        x = x * 10000
    elif g == 5:
        x = x * 100000
    elif g == 6:
        x = x * 1000000
else:
    print("Erreur")

print("Mv =", x / y, a, "/", b)
sleep(5)
