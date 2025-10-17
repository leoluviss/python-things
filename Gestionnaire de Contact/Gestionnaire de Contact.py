from json import load, dump  # Importation des fonctions pour manipuler les fichiers JSON
from time import sleep  # Importation de la fonction sleep pour faire des pauses

SAVE_FILE = "Gestionnaire de Contact\Liste de contact - Sauvegarde.json"  # Chemin du fichier de sauvegarde des contacts

def fonct_choix():  # Fonction pour afficher le menu et obtenir le choix de l'utilisateur

    choix = 0

    while choix not in (1, 2, 3, 4):
        choix = int(input(""" 
Que voulez-vous faire ?
                      
    1. Ajouter un contact
                      
    2. Supprimer un contact
                      
    3. Afficher un contacts
                      
    4. Quitter

Votre choix : """ ))

        if choix in (1, 2, 3, 4):
            return choix

        else:
            print("\nChoix Invalide")
            sleep(2)


def ajouter_modifier_contact():  # Fonction pour ajouter ou modifier un contact

    nom = input("\nEntrez le nom du contact à ajouter ou à modifier : ")
    numero = input("Entrez le numéro de téléphone du contact : ")
    
    with open(SAVE_FILE, "r", encoding='utf-8') as f:
        data = load(f)

    data[nom] = numero

    with open(SAVE_FILE, "w", encoding='utf-8') as f:
        dump(data, f)
    return f"\nContact {nom} ajouté avec le numéro {numero}."



def supprimer_contact(nom):  # Fonction pour supprimer un contact

    with open(SAVE_FILE, "r", encoding='utf-8') as f:
        data = load(f)
    
    if nom == "*":  # Supprimer tous les contacts
        data.clear()
        with open(SAVE_FILE, "w", encoding='utf-8') as f:
            dump(data, f)
        return "\nTous les contacts ont été supprimés."

    if nom in data:

        del data[nom]

        with open(SAVE_FILE, "w", encoding='utf-8') as f:
            dump(data, f)

        return f"\nLe contact {nom} a été supprimé."

    else:
        return f"\nLe contact {nom} n'existe pas."



def afficher_contacts(nom):  # Fonction pour afficher un contact

    with open(SAVE_FILE, "r", encoding='utf-8') as f:
        data = load(f)

    if nom == "*":  # Afficher tous les contacts
        print("\nAffichage de tout les contacts :")
        for i in data:
            print(f"\n  {i} : {data[i]}")
        return ""

    if nom in data:
        return f"\nLe numéro de {nom} est {data[nom]}."
    else:
        return f"\nLe contact {nom} n'existe pas."


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
