import os
from A1_classes_cartes.Carte import Carte_jeux as choisir, Carte_jeux
from A1_classes_cartes.Personne import Personne
import jsonpickle
import random

class Joueur(Personne):

    dict_joueur = {}
    def __init__(self, nom, age):
        super().__init__(nom, age)
        self.liste_carte = []
        self.debut_carte_partie = 1

    def ajouter_joueuer(self):
        Joueur.dict_joueur[self.nom] = self

    @staticmethod
    def piger_carte(nom_joueur):
        Joueur.dict_joueur = Joueur.load_fichier_joueur()
        personne = Joueur.dict_joueur[nom_joueur]
        deck = Carte_jeux.load()
        carte_choisie = random.choice(deck.tt_list_carte)
        deck.enlever_carte(carte_piger=carte_choisie)
        personne.liste_carte.append(carte_choisie)
        Joueur.dict_joueur[nom_joueur] = personne
        with (open("jeux_carte.json", "w") as file):
            file.write(jsonpickle.encode(Joueur.dict_joueur, indent=4))

    @staticmethod
    def enlever_une_carte(nom_joueur,nom_enemie):
        Joueur.dict_joueur = Joueur.load_fichier_joueur()
        joueur1 = None
        joueur2 = None
        if nom_joueur in Joueur.dict_joueur:
            joueur1 = Joueur.dict_joueur[nom_joueur]

        if nom_enemie in Joueur.dict_joueur:
            joueur2 = Joueur.dict_joueur[nom_enemie]

        if len(joueur2.liste_carte) >= 1:
            carte_choisie = random.choice(joueur2.liste_carte)
            joueur2.liste_carte.remove(carte_choisie)
            joueur1.liste_carte.append(carte_choisie)
        else:
            print(f"{nom_enemie} n'a pu de carte")
            return
        Joueur.dict_joueur[nom_joueur] = joueur1
        Joueur.dict_joueur[nom_enemie] = joueur2

        with (open("jeux_carte.json", "w") as file):
            file.write(jsonpickle.encode(Joueur.dict_joueur, indent=4))
    @staticmethod
    def ajouter_carte_joueur(nom):
        Joueur.dict_joueur = Joueur.load_fichier_joueur()

        if nom in Joueur.dict_joueur:
            joueur = Joueur.dict_joueur[nom]
            if Joueur.dict_joueur[nom].debut_carte_partie > 1:
                print(f"{nom} à déjà eu ses 5 première cartes")
                return

            deck = Carte_jeux.load()
            joueur.liste_carte += random.sample(deck.tt_list_carte, 5)
            deck.liste_carte_supprimer =  joueur.liste_carte
            deck.enlever_carte(liste_carte=deck.liste_carte_supprimer)
            joueur.debut_carte_partie += 1
            Joueur.dict_joueur[nom] = joueur
            print(f"Cartes ajoutées à {nom}")
            with open("jeux_carte.json", "w") as file:
                file.write(jsonpickle.encode(Joueur.dict_joueur, indent=4))
        else:
            print(f"Joueur {nom} N'existe PAS")

    @staticmethod
    def voir_info():
        Joueur.dict_joueur = Joueur.load_fichier_joueur()
        for i,information in Joueur.dict_joueur.items():
            print(f"{i}: {information}")

    def sauvegarder_joueur(self):
        if os.path.isfile("jeux_carte.json"):
            try:
                Joueur.dict_joueur = Joueur.load_fichier_joueur()
            except Exception:
                return None

        Joueur.dict_joueur[self.nom] = self

        with open("jeux_carte.json", "w") as file:
            file.write(jsonpickle.encode(Joueur.dict_joueur, indent=4))

    @staticmethod
    def load_fichier_joueur():
        try:
            with open("jeux_carte.json", "r") as file:
                return jsonpickle.decode(file.read())
        except Exception:
            return None

    def __str__(self):
        return super().__str__() + f"liste_carte: {self.liste_carte}"

if __name__== '__main__':

    voir_fichier = Joueur.load_fichier_joueur()

