import random

from Personne import Personne
import jsonpickle
from Carte import Carte_jeux,choisir_carte

class Joueur(Personne):
    dict_joueur = {}

    def __init__(self, nom,age,bio):
        super().__init__(nom,age,bio)
        self.meilleur_main = None
        self.liste_carte = []


    def ajouter_joueur(self):
        Joueur.dict_joueur[self.nom] = self
        return self

    @staticmethod
    def ajouter_carte_joueur(nom):
        Joueur.dict_joueur = Joueur.load()
        deck =  Carte_jeux.get_instance()

        if nom in Joueur.dict_joueur:
            joueur = Joueur.dict_joueur[nom]

            carte_choisie = random.sample(deck.tt_list_carte, 5)
            deck.lst_carte_supprimer = carte_choisie


    def piger_carte_hasard(self):
        pass

    def melanger_carte_joueur(self):
        pass



    def sauvegarder_joueur(self):
        with open("Joueur.py.json", "w",encoding="utf-u8") as file:
            file.write(jsonpickle.encode(self, indent=4))

    @staticmethod
    def load():
        try:
            with open("Joueur.py.json", "r", encoding="utf-u8") as file:
                return jsonpickle.decode(file.read())
        except FileNotFoundError:
            print(f"LOAD impossible fichier introuvable")
            Joueur.dict_joueur = {}
            return Joueur.dict_joueur



