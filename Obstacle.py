# Obstacle.py
# Classe représentant un obstacle dans la course
# 3 types d'obstacles pour 3 temps d'arret different
#Philip

import random
import time

class Obstacle:

    def __init__(self, type_obstacle):
       self.type == type_obstacle

       if( self.type == "saut"):
           self.difficulte = 1
           self.chance = 0.30
           self.penalite = 0.8
       if( self.type == "grimpe"):
           self.difficulte = 2
           self.chance = 0.50
           self.penalite = 1
       if( self.type == "nager"):
           self.difficulte = 3
           self.chance = 0.80
           self.penalite = 1.5
    
    def appliquer(self, coureur, messagerie, position):
        if random.random() < self.chance: #determine si le joueur a reussi ou echoue son obstacle
            messagerie.envoyer(
                f"{coueur.nom} échoue l'obstacle '{self.type}' à la case {index_case} (+{self.penalite}s)"
            )
            time.sleep(self.penalite)
            coureur.temps_total += self.penalite
        else:
            messagerie.envoyer(
                f"{coureur.nom} réussit l'obstacle '{self.type}' à la case {position}"
            )
    #Philip: methode qui va envoyer un message qui va contenir l'etat du joueur + cmb de temps de penalite + la case ou il est