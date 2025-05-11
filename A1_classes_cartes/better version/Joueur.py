# A1_classes_cartes/joueuer.py
import json
import os
import random
import jsonpickle
from Personne import Personne
from Carte import Carte_jeux, choisir


class Joueur(Personne):
    """Player class that manages player information and cards"""

    dict_joueur = {}
    _fichier_joueurs = "jeux_carte.json"

    def __init__(self, nom, age):
        super().__init__(nom, age)
        self.liste_carte = []
        self.debut_carte_partie = 1

    def ajouter_joueuer(self):
        """Add player to the dictionary of players"""
        Joueur.dict_joueur[self.nom] = self
        Joueur.sauvegarder_tous_joueurs()
        return self

    @staticmethod
    def piger_carte(nom_joueur):
        """Draw a card from the deck and add it to player's hand"""
        Joueur.charger_joueurs()
        deck = Carte_jeux.get_instance()

        if nom_joueur not in Joueur.dict_joueur:
            return f"Le joueur {nom_joueur} n'existe pas"

        if not deck.tt_list_carte:
            return "Le deck est vide, impossible de piger une carte"

        personne = Joueur.dict_joueur[nom_joueur]
        carte_choisie = random.choice(deck.tt_list_carte)
        deck.enlever_carte(carte_piger=carte_choisie)
        personne.liste_carte.append(carte_choisie)

        # Save changes
        Joueur.sauvegarder_tous_joueurs()
        return f"{nom_joueur} a pigé {carte_choisie}"

    @staticmethod
    def enlever_une_carte(nom_joueur, nom_enemie):
        """Take a random card from another player"""
        Joueur.charger_joueurs()

        if nom_joueur not in Joueur.dict_joueur:
            return f"Le joueur {nom_joueur} n'existe pas"

        if nom_enemie not in Joueur.dict_joueur:
            return f"Le joueur {nom_enemie} n'existe pas"

        joueur1 = Joueur.dict_joueur[nom_joueur]
        joueur2 = Joueur.dict_joueur[nom_enemie]

        if not joueur2.liste_carte:
            return f"{nom_enemie} n'a plus de cartes"

        carte_choisie = random.choice(joueur2.liste_carte)
        joueur2.liste_carte.remove(carte_choisie)
        joueur1.liste_carte.append(carte_choisie)

        # Save changes
        Joueur.sauvegarder_tous_joueurs()
        return f"{nom_joueur} a pris la carte {carte_choisie} de {nom_enemie}"

    @staticmethod
    def ajouter_carte_joueur(nom):
        """Add 5 initial cards to a player (only once)"""
        Joueur.charger_joueurs()

        if nom not in Joueur.dict_joueur:
            return f"Le joueur {nom} n'existe pas"

        joueur = Joueur.dict_joueur[nom]

        if joueur.debut_carte_partie > 1:
            return f"{nom} a déjà reçu ses 5 cartes initiales"

        deck = Carte_jeux.get_instance()

        if len(deck.tt_list_carte) < 5:
            return f"Pas assez de cartes dans le deck ({len(deck.tt_list_carte)})"

        nouvelles_cartes = random.sample(deck.tt_list_carte, 5)
        joueur.liste_carte.extend(nouvelles_cartes)
        deck.enlever_carte(liste_carte=nouvelles_cartes)
        joueur.debut_carte_partie += 1

        # Save changes
        Joueur.sauvegarder_tous_joueurs()
        return f"{nom} a reçu 5 nouvelles cartes"

    @staticmethod
    def voir_info():
        """Display information about all players"""
        Joueur.charger_joueurs()
        resultats = []
        for nom, joueur in Joueur.dict_joueur.items():
            cartes = ", ".join(str(carte) for carte in joueur.liste_carte)
            resultats.append(f"{nom} (âge: {joueur.age}) - Cartes: {cartes}")
        return resultats

    def sauvegarder_joueur(self):
        """Save one player to the players dictionary and file"""
        Joueur.charger_joueurs()
        Joueur.dict_joueur[self.nom] = self
        Joueur.sauvegarder_tous_joueurs()
        return self

    @staticmethod
    def sauvegarder_tous_joueurs():
        """Save all players to the JSON file"""
        with open(Joueur._fichier_joueurs, "w") as file:
            file.write(jsonpickle.encode(Joueur.dict_joueur, indent=4))

    @staticmethod
    def charger_joueurs():
        """Load players from JSON file"""
        try:
            with open(Joueur._fichier_joueurs, "r") as file:
                Joueur.dict_joueur = jsonpickle.decode(file.read())
        except FileNotFoundError:
            Joueur.dict_joueur = {}
        except json.JSONDecodeError:
            print(f"Erreur de lecture du fichier {Joueur._fichier_joueurs}, création d'un nouveau fichier")
            Joueur.dict_joueur = {}
        return Joueur.dict_joueur

    def __str__(self):
        cartes = ", ".join(str(carte) for carte in self.liste_carte)
        return super().__str__() + f"Cartes: {cartes}"