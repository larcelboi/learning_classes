
# A1_classes_cartes/Un_personne.py
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        return f"Nom: {self.nom} age: {self.age}\n"