from A0_classes_examen_carte1.phase_enum.phase_chiffre import Carte_chiffre
from A0_classes_examen_carte1.phase_enum.phase_carte import Carte
import jsonpickle

class Carte_jeux:
    _instance_carte = None
    def __init__(self):
        self.tt_liste_carte = []
        self.lst_carte_supprimer = []

    @classmethod
    def get_instance(cls):
        if cls._instance_carte is None:
            cls._instance_carte = cls.load()
        return cls._instance_carte

    def creation_carte(self):
        for carte in list(Carte):
            for chiffre_carte in list(Carte_chiffre):
                combiner_carte = f"{carte.value} {chiffre_carte.value}"
                self.tt_liste_carte.append(combiner_carte)
        return  self.tt_liste_carte

    @staticmethod
    def supprimer_carte(une_carte=None,list_supprimer_carte=None):
        deck = Carte_jeux.get_instance()
        if une_carte is not None:
            for carte in une_carte:
                if carte in deck.tt_liste_carte:
                    deck.tt_liste_carte.remove(carte)
        elif list_supprimer_carte is not None:
            for carte1 in list_supprimer_carte:
                if carte1 in deck.tt_liste_carte:
                    deck.tt_liste_carte.remove(carte1)
        deck.sauvegarder_carte()

    def sauvegarder_carte(self):
        with open("Carte.json","w",encoding="utf-8") as f:
            f.write(jsonpickle.encode(self, indent=4))
        return self

    @staticmethod
    def load():
        try:
            with open("Carte.json","r",encoding="utf-8") as f:
                return jsonpickle.decode(f.read())
        except FileNotFoundError:
            new_carte = Carte_jeux()
            new_carte.creation_carte()
            new_carte.sauvegarder_carte()
            return new_carte

    def __str__(self):
        return f"Nombre de cartes {len(self.tt_liste_carte)}"

def choisir_carte():
    return Carte_jeux.get_instance()