from json import load, dump
from time import sleep

# Fichier de sauvegarde
SAVE_FILE = "Sauvegarde_contact.json"

def fonct_choix():
    choix = 0
    while choix not in (1, 2, 3, 4):
        choix = int(input(""" 
Que voulez-vous faire ?
                      
    1. Ajouter un contact
                      
    2. Supprimer un contact
                      
    3. Afficher les contacts
                      
    4. Quitter

Votre choix : """ ))
        if choix in (1, 2, 3, 4):
            return choix
        else:
            print("\nChoix Invalide")
            sleep(2)


def ajouter_modifier_contact():
    nom = input("\nEntrez le nom du contact à ajouter ou à modifier : ")
    numero = input("Entrez le numéro de téléphone du contact : ")
    
    with open(SAVE_FILE, "r") as f:
        data = load(f)

    data[nom] = numero

    with open(SAVE_FILE, "w") as f:
        dump(data, f)
    return f"Contact {nom} ajouté avec le numéro {numero}."



def supprimer_contact(nom):

    with open(SAVE_FILE, "r") as f:
        data = load(f)

    if nom in data:
        del data[nom]

        with open(SAVE_FILE, "w") as f:
            dump(data, f)

        return f"Le contact {nom} a été supprimé."
    else:
        return f"Le contact {nom} n'existe pas."



def afficher_contacts(nom):
    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        data = load(f)

    if nom in data:
        return f"Le numéro de {nom} est {data[nom]}."
    else:
        return f"Le contact {nom} n'existe pas."


choix = 1

while choix in (1, 2, 3):

    choix = fonct_choix()

    if choix == 1: 
        print(ajouter_modifier_contact())
        sleep(2)   

    elif choix == 2:
        nom = input("\nEntrez le nom du contact à supprimer : ")
        print(supprimer_contact(nom))
        sleep(2)

    elif choix == 3:
        nom = input("\nEntrez le nom du contact à afficher : ")
        print(afficher_contacts(nom))
        sleep(2)

print("\nÀ bientôt dans le gestionnaire de contacts !", "\n")
