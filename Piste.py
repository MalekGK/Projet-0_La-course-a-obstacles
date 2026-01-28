# Piste.py
# Classe représentant la piste de la course
# Malek

class Piste:
    __coureurs = []

    def __init__(self, coureurs, allees):
        self.__coureurs = coureurs
        self.allees = allees

    def resultat(self, resultat):
        self.resultat = resultat