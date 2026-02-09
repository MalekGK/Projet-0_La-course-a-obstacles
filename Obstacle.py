import random
import time

class Obstacle:

    def __init__(self, type_obstacle):
        self.type = type_obstacle

        if self.type == "saut":
            self.chance = 0.30
            self.penalite = 0.8

        elif self.type == "grimpe":
            self.chance = 0.50
            self.penalite = 1.0

        elif self.type == "nager":
            self.chance = 0.80
            self.penalite = 1.5

        else:
            self.chance = 0.0
            self.penalite = 0.0


    def appliquer(self, coureur, messagerie, position):

        if random.random() < self.chance:

            messagerie.envoyer(
                coureur.couleur + " échoue l'obstacle '" +
                self.type + "' à la case " + str(position) +
                " (+" + str(self.penalite) + "s)"
            )

            time.sleep(self.penalite)
            coureur.temps_total = coureur.temps_total + self.penalite

        else:
            messagerie.envoyer(
                coureur.couleur + " réussit l'obstacle '" +
                self.type + "' à la case " + str(position)
            )
