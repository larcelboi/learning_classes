import jsonpickle


class Personne:
    def __init__(self, nom,age):
        self.nom = nom
        self.age = age


    def __str__(self):
        return f"Nom: {self.nom} age: {self.age}\n"

if __name__ == "__main__":
    tt_list_carte=  [
        "Carreau 1",
        "Carreau 2",
        "Carreau 3",
        "Carreau 4",
        "Carreau 5",
        "Carreau 6",
        "Carreau 7",
        "Carreau 8",
        "Carreau 9",
        "Carreau 10",
        "Carreau Jack",
        "Carreau Queen",
        "Carreau King",
        "Trefle 1",
        "Trefle 2",
        "Trefle 3",
        "Trefle 4",
        "Trefle 5",
        "Trefle 6",
        "Trefle 7",
        "Trefle 8",
        "Trefle 9",
        "Trefle 10",
        "Trefle Jack",
        "Trefle Queen",
        "Trefle King",
        "Pique 1",
        "Pique 2",
        "Pique 3",
        "Pique 4",
        "Pique 5",
        "Pique 6",
        "Pique 7",
        "Pique 8",
        "Pique 9",
        "Pique 10",
        "Pique Jack",
        "Pique Queen",
        "Pique King",
        "Coeur 1",
        "Coeur 2",
        "Coeur 3",
        "Coeur 4",
        "Coeur 5",
        "Coeur 6",
        "Coeur 7",
        "Coeur 8",
        "Coeur 9",
        "Coeur 10",
        "Coeur Jack",
        "Coeur Queen",
        "Coeur King"]
    print(len(tt_list_carte))