x=float(1)
ms=float(input("Temps d'une période en ms ? "))

def hz():
  x=ms/1000
  return 1/x

print("Fréquence :",hz(),"Hz")
