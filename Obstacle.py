# Obstacle.py
# Classe représentant un obstacle dans la course
# 3 types d'obstacles pour 3 temps d'arret different

class Obstacle:
    def __init__(self, id , temps_attente, description):
        self.id = id
        self.temps_attente = temps_attente
        self.description = description


    