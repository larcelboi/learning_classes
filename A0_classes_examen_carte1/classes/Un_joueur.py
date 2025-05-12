import os

from .Un_personne import Personne
from .Carte import Carte_jeux,choisir_carte
import random
import jsonpickle



class Joueur(Personne):
    dict_joueur = {}

    def __init__(self, nom,age,bio):
        super().__init__(nom,age,bio)
        self.meilleur_main = None
        self.liste_carte = []
        self.ajouter_carte_fait = False

    def piger_dans_lautre(self,target_nom):
        pass

    @staticmethod
    def voir_informations():
        Joueur.dict_joueur = Joueur.load()
        for nom,informations in Joueur.dict_joueur.items():
            print(f"{nom} : {informations}")
            print()

    @staticmethod
    def ajouter_carte_joueur(nom):
        Joueur.dict_joueur = Joueur.load()
        deck =  Carte_jeux.get_instance()

        if nom in Joueur.dict_joueur:
            joueur = Joueur.dict_joueur[nom]

            if len(deck.tt_liste_carte) >= 5:
                carte_choisie = random.sample(deck.tt_liste_carte, 5)
                deck.lst_carte_supprimer = carte_choisie
                deck.supprimer_carte(list_supprimer_carte=deck.lst_carte_supprimer)
                joueur.liste_carte.extend(carte_choisie) # ajoute les éléements dans la liste
                joueur.ajouter_carte_fait = True
                Joueur.dict_joueur[nom] = joueur
                joueur.sauvegarder_joueur()
                print(f"Cartes ajoutés :\n{",".join(carte_choisie)} ")
            else:
                print(f"il ne reste pus assez de carte")
        else:
            print("Joueur n'existe pas")

    @staticmethod
    def afficher_carte_deck():
        deck = Carte_jeux.get_instance()
        for carte in deck.tt_liste_carte:
            print(carte)

    @staticmethod
    def piger_carte_hasard(nom_joueur):
        Joueur.dict_joueur = Joueur.load()
        joueur = Joueur.dict_joueur[nom_joueur]

        deck = Carte_jeux.get_instance()
        if len(deck.tt_liste_carte) >= 1:
            carte_choise = random.sample(deck.tt_liste_carte, 1)
            print(f"la carte {",".join(carte_choise)} a été choisie!")
            deck.supprimer_carte(une_carte=carte_choise)
            joueur.liste_carte.extend(carte_choise)
            Joueur.dict_joueur[nom_joueur] = joueur
            joueur.sauvegarder_joueur()
        else:
            print(f"il ne reste pus assez de carte")

    @staticmethod
    def melanger_carte_joueur(nom):
        Joueur.dict_joueur = Joueur.load()

        joueur = Joueur.dict_joueur[nom]
        carte_non_melanger = joueur.liste_carte
        print(f"Carte de {nom} sont mélangées:")
        print(f"before: {",".join(carte_non_melanger)}")
        random.shuffle(joueur.liste_carte)
        Joueur.dict_joueur[nom] = joueur
        print(f"after: {",".join(joueur.liste_carte)}")
        joueur.sauvegarder_joueur()



    def sauvegarder_joueur(self):
        if os.path.isfile("Un_joueur.py.json"):
            try:
                with open("Un_joueur.py.json", "r", encoding="utf-8") as file:
                    Joueur.dict_joueur = jsonpickle.decode(file.read())
            except FileNotFoundError:
                return  None
        Joueur.dict_joueur[self.nom] = self
        with open("Un_joueur.py.json", "w",encoding="utf-8") as file:
            file.write(jsonpickle.encode(Joueur.dict_joueur, indent=4))

    @staticmethod
    def load():
        try:
            with open("Un_joueur.py.json", "r", encoding="utf-8") as file:
                return jsonpickle.decode(file.read())
        except FileNotFoundError:
            print(f"LOAD impossible fichier introuvable")
            Joueur.dict_joueur = {}
            return Joueur.dict_joueur

    def __str__(self):
        return  super().__str__() + f"\nartes: {self.liste_carte}"


