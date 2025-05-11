from A0_classes_examen_carte.phase_enum.phase_carte import Carte_deck
from A0_classes_examen_carte.phase_enum.phase_chiffre import Chiffre_carte
import jsonpickle

class Carte_jeux:
    _instance_carte = None
    def __init__(self):
        self.tt_lite_carte = []
        self.lst_carte_supprimer = []

    @classmethod
    def get_instance(cls):
        if cls._instance_carte is None:
            cls._instance_carte = cls.load()
        return cls._instance_carte

    def creation_carte(self):
        for carte in list(Carte_deck):
            for chiffre_carte in list(Chiffre_carte):
                print(f"{carte.value} {chiffre_carte.value}")
                self.tt_lite_carte.append(chiffre_carte)
        return self

    def sauvegarder_carte(self):
        with open("Carte.json","w",encoding="utf-8") as f:
            f.write(jsonpickle.encode(self.tt_lite_carte,indent=4))
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

def choisir_carte():
    return Carte_jeux.get_instance()