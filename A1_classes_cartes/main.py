from A1_classes_cartes.joueuer import Joueur
from A1_classes_cartes.Personne import Personne
from A1_classes_cartes.Carte import choisir

def menu():
    le_joueur = None
    deck = choisir()
    print(deck)
    while True:
        choix = input("""
            Menu:
        1. Création de joueur
        2. Sauvegarder joueur
        3. Voir joueur et information
        4. Ajouter carte au joueur
        5. Enlever carte au joueur
        6. Piger une carte
        0. Quitter l'application
        Entrer votre choix:
        """)
        match choix:
            case "1":
                le_joueur = creation_joueur()
            case "2":
                if le_joueur is not None:
                    sauvegarder_joueur(le_joueur)
                else:
                    print(f"Aucun joueur n'a été crée")
            case "3":
                voir_joueur_et_information()
            case "4":
                ajouter_carte()
            case "5":
                enlever_une_carte()
            case "6":
                Piger_un_carte()
            case "0":
                print(f"Au revoir")
                break


def creation_joueur():
    nom = input("Entrer nom du joueur: ")
    age = int(input("Entrer age du joueur: "))
    return Joueur(nom, age)

def sauvegarder_joueur(joueur):

    Joueur.sauvegarder_joueur(joueur)
    print(f"{joueur} a été ajouté")

def voir_joueur_et_information():
    Joueur.voir_info()
def ajouter_carte():
    nom_joueur = input("Entrer nom du joueur: ")
    Joueur.ajouter_carte_joueur(nom_joueur)

def enlever_une_carte():
    nom_joueur = input("Entrer votre nom : ")
    nom_autre_joueur = input("Entrer le nom de votre enemie: ")
    Joueur.enlever_une_carte(nom_joueur, nom_autre_joueur)

def Piger_un_carte():
    nom_joueur = input("Entrer votre nom joueur: ")
    Joueur.piger_carte(nom_joueur)
if __name__ == "__main__":
    menu()