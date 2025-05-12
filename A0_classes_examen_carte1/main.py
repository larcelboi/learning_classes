from classes.Un_joueur import Joueur
from classes.Carte import Carte_jeux,choisir_carte

def menu():
    joueur = None
    deck = Carte_jeux.get_instance()
    print(f"Nombre de carte {deck}")
    while True:
        choix = input("""
        1.Crée un joueur
        2.Sauvegarder le joueur
        3.Voir information
        4.Ajouter carte au joueur
        5.Piger carte hasard
        6.Afficher carte
        7.Mélanger carte
        8.Piger dans l'autre
        0. Quitter l'application
        
        Entrer votre choix: 
        """)
        match choix:
            case "1":
                joueur = cree_joueur()
            case "2":
                if joueur is None:
                    print("Vous devez créer un joueur")
                    continue
                else:
                    sauvegarder_joueur(joueur)
            case "3":
                voir_informations()
            case "4":
                ajouter_joueur_carte()
            case "5":
                piger_c_hasard()
            case "6":
                afficher_carte()
            case "7":
                melanger_carte()
            case "8":
                piger_dans_main_autre()
            case "0":
                print("Au revoir")
                break
            case _:
                print("Votre choix n'est pas valide")
                continue

def cree_joueur():
    nom = input("Nom du joueur: ")
    age = int(input("l'age du joueur: "))
    bio = input("Bio du joueur: ")
    return Joueur(nom, age, bio)

def sauvegarder_joueur(joueur):
    if isinstance(joueur, Joueur):
        joueur.sauvegarder_joueur()
        print(f"{joueur.nom} a été sauvegarder")

def voir_informations():
    Joueur.voir_informations()

def ajouter_joueur_carte():
    nom_joueur = input("Entrer nom joueur: ")
    Joueur.dict_joueur = Joueur.load()
    if nom_joueur in Joueur.dict_joueur:
        Joueur.ajouter_carte_joueur(nom_joueur)
    else:
        print("Votre nom joueur n'est pas valide")

def afficher_carte():
    Joueur.afficher_carte_deck()

def melanger_carte():
    nom_joueur = input("Entrer nom joueur: ")
    Joueur.dict_joueur = Joueur.load()
    if nom_joueur in Joueur.dict_joueur:
        Joueur.melanger_carte_joueur(nom_joueur)
    else:
        print("Votre nom joueur n'est pas valide")

def piger_c_hasard():
    nom_joueur = input("Entrer nom joueur: ")
    Joueur.dict_joueur = Joueur.load()
    if nom_joueur in Joueur.dict_joueur:
        Joueur.piger_carte_hasard(nom_joueur)
    else:
        print("Votre nom joueur n'est pas valide")

def piger_dans_main_autre():
    Joueur.dict_joueur = Joueur.load()

    votre_nom = input("Entrer votre nom: ")
    target_nom = input("Entrer de votre target: ")

    joueur1 = Joueur.dict_joueur[target_nom] # Prendre l'object dans le dict
    joueur2 = Joueur.dict_joueur[target_nom] # Prendre l'object dans le dict

    if votre_nom in Joueur.dict_joueur  and target_nom in Joueur.dict_joueur:
        if isinstance(joueur1, Joueur) and isinstance(joueur2, Joueur): # check the objects in the dictionnary aka the keys
            Joueur.piger_dans_lautre(joueur1, joueur2)

if __name__ == "__main__":
    menu()