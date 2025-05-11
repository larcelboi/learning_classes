import os

from enum_carte.Phase_carte import Carte
from enum_carte.Phae_chiffre_carte import chiffre_carte
import jsonpickle

class Carte_jeux:
    def __init__(self):
        self.tt_list_carte = []
        self.liste_carte_supprimer = []
        self.creation_carte = False

    def creation_deck(self):
        for carte in list(Carte):
            for chiffre in list(chiffre_carte):
                self.tt_list_carte.append(f"{carte.value} {chiffre.value}")
        self.creation_carte = True

    def sauvegarder_carte(self,filename="Carte.json"):
        with open(filename,"w",encoding="utf-8") as file:
            file.write(jsonpickle.encode(self,indent=4))

    @staticmethod
    def enlever_carte(liste_carte=None,carte_piger=None):
        deck = Carte_jeux.load()
        if liste_carte is not None:
            for carte in liste_carte:
                if carte in  deck.tt_list_carte:
                    deck.tt_list_carte.remove(carte)
                    print(f"{carte} a été enlevée")
            print(len(deck.tt_list_carte))
        elif carte_piger is not None:
            if carte_piger in deck.tt_list_carte:
                deck.tt_list_carte.remove(carte_piger)
                print(f"{carte_piger} a été enlevée")
            print(len(deck.tt_list_carte))
        deck.sauvegarder_carte()

    @staticmethod
    def load(filename="Carte.json"):
        try:
            with open(filename,"r",encoding="utf-8") as file:
                return jsonpickle.decode(file.read())
        except Exception:
            return Carte_jeux()


    def __str__(self):
        return f"Deck fini: {len(self.tt_list_carte)}"


def choisir():
    filename = "Carte.json"
    if os.path.isfile(filename):
        return Carte_jeux.load()
    else:
        creation_carte = Carte_jeux()
        creation_carte.creation_deck()
        creation_carte.sauvegarder_carte()
        return Carte_jeux.load()