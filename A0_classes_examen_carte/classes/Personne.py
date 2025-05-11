
class Personne:
    def __init__(self, nom,age,bio):
        self.nom = nom
        self.age = age
        self.bio = bio


    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self, nouv_nom):
        if isinstance(nouv_nom, str):
            self._nom = nouv_nom

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, nouv_age):
        if isinstance(nouv_age, int):
            self._age = nouv_age

    @property
    def bio(self):
        return self._bio

    @bio.setter
    def bio(self, nouv_bio):
        if isinstance(nouv_bio, str):
            self._bio = nouv_bio
