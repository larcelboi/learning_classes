# A1_classes_cartes/Phase_carte.py
import os
import json
import jsonpickle
from enum_carte.Phase_carte import Carte
from enum_carte.Phae_chiffre_carte import chiffre_carte


class Carte_jeux:
    _instance = None  # Singleton pattern

    def __init__(self):
        self.tt_list_carte = []
        self.liste_carte_supprimer = []
        self.creation_carte = False

    @classmethod
    def get_instance(cls):
        """Get or create the deck instance using singleton pattern"""
        if cls._instance is None:
            cls._instance = cls.load()
        return cls._instance

    def creation_deck(self):
        """Create a full deck of cards"""
        self.tt_list_carte = []
        for carte in list(Carte):
            for chiffre in list(chiffre_carte):
                self.tt_list_carte.append(f"{carte.value} {chiffre.value}")
        self.creation_carte = True
        return self

    def sauvegarder_carte(self, filename="Carte.json"):
        """Save the deck to a JSON file"""
        with open(filename, "w", encoding="utf-8") as file:
            file.write(jsonpickle.encode(self, indent=4))
        return self

    def enlever_carte(self, liste_carte=None, carte_piger=None):
        """Remove one or multiple cards from the deck"""
        if liste_carte is not None:
            for carte in liste_carte:
                if isinstance(carte, list):  # Handle nested lists
                    for c in carte:
                        if c in self.tt_list_carte:
                            self.tt_list_carte.remove(c)
                elif carte in self.tt_list_carte:
                    self.tt_list_carte.remove(carte)
        elif carte_piger is not None:
            if carte_piger in self.tt_list_carte:
                self.tt_list_carte.remove(carte_piger)

        # Save changes to file
        self.sauvegarder_carte()
        return self

    @staticmethod
    def load(filename="Carte.json"):
        """Load deck from JSON file or create a new one if file doesn't exist"""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                deck = jsonpickle.decode(file.read())
                Carte_jeux._instance = deck
                return deck
        except Exception:
            # Create new deck if file doesn't exist
            new_deck = Carte_jeux()
            if not new_deck.creation_carte:
                new_deck.creation_deck()
                new_deck.sauvegarder_carte()
            return new_deck

    def __str__(self):
        return f"Deck actuel: {len(self.tt_list_carte)} cartes"


def choisir():
    """Get the current deck instance or create a new one"""
    return Carte_jeux.get_instance()