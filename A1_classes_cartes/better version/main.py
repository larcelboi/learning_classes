from Joueur import Joueur
from Carte import Carte_jeux
# main.py
def menu():
    # Load players and deck at start
    Joueur.charger_joueurs()
    deck = Carte_jeux.get_instance()

    le_joueur = None
    print(f"Bienvenue au jeu de cartes! {deck}")

    while True:
        choix = input("""
            Menu:
        1. Création de joueur
        2. Sauvegarder joueur
        3. Voir joueurs et information
        4. Ajouter cartes à un joueur
        5. Prendre une carte d'un autre joueur
        6. Piger une carte du deck
        0. Quitter l'application
        Entrer votre choix: """)

        print("\n" + "-" * 40)

        match choix:
            case "1":
                le_joueur = creation_joueur()
                print(f"Joueur {le_joueur.nom} créé")
            case "2":
                if le_joueur is not None:
                    sauvegarder_joueur(le_joueur)
                else:
                    print("Aucun joueur n'a été créé")
            case "3":
                afficher_info_joueurs()
            case "4":
                result = ajouter_carte()
                print(result)
            case "5":
                result = enlever_une_carte()
                print(result)
            case "6":
                result = piger_une_carte()
                print(result)
            case "0":
                print("Au revoir!")
                break
            case _:
                print("Choix invalide")

        print("-" * 40 + "\n")

def creation_joueur():
    """Create a new player"""
    nom = input("Entrer nom du joueur: ")

    # Check if player already exists
    Joueur.charger_joueurs()
    if nom in Joueur.dict_joueur:
        print(f"Le joueur {nom} existe déjà!")
        return Joueur.dict_joueur[nom]

    try:
        age = int(input("Entrer âge du joueur: "))
        joueur = Joueur(nom, age)
        joueur.ajouter_joueuer()
        return joueur
    except ValueError:
        print("L'âge doit être un nombre")
        return None

def sauvegarder_joueur(joueur):
    """Save player to file"""
    joueur.sauvegarder_joueur()
    print(f"{joueur.nom} a été sauvegardé")

def afficher_info_joueurs():
    """Display information about all players"""
    infos = Joueur.voir_info()
    if not infos:
        print("Aucun joueur enregistré")
        return

    print("Liste des joueurs:")
    for info in infos:
        print(f"- {info}")

def ajouter_carte():
    """Add 5 initial cards to a player"""
    nom_joueur = input("Entrer nom du joueur: ")
    return Joueur.ajouter_carte_joueur(nom_joueur)

def enlever_une_carte():
    """Take a card from another player"""
    nom_joueur = input("Entrer votre nom: ")
    nom_autre_joueur = input("Entrer le nom de votre adversaire: ")
    return Joueur.enlever_une_carte(nom_joueur, nom_autre_joueur)

def piger_une_carte():
    """Draw a card from the deck"""
    nom_joueur = input("Entrer votre nom: ")
    return Joueur.piger_carte(nom_joueur)

if __name__ == "__main__":
    menu()