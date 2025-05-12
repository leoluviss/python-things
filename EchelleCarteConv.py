longueurReelle=float(input("Longueur réelle en km ? "))
longueurCarte=float(input("Longueur réelle en cm ? "))
echelleInv=longueurReelle*100000/longueurCarte
print("L'échelle est au 1-",echelleInv,"ème")
