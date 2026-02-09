import random
import time

class Obstacle:

    def __init__(self, type_obstacle):
<<<<<<< HEAD
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


=======
       self.type = type_obstacle

       if( self.type == "saut"):
           self.difficulte = 1
           self.chance = 0.30
           self.penalite = 0.8
       if( self.type == "grimper"):
           self.difficulte = 2
           self.chance = 0.50
           self.penalite = 1
       if( self.type == "nager"):
           self.difficulte = 3
           self.chance = 0.80
           self.penalite = 1.5
    
>>>>>>> b30bbb4cd8c1e8787595d1ada9090e376d767335
    def appliquer(self, coureur, messagerie, position):

        if random.random() < self.chance:

            messagerie.envoyer(
<<<<<<< HEAD
                coureur.couleur + " échoue l'obstacle '" +
                self.type + "' à la case " + str(position) +
                " (+" + str(self.penalite) + "s)"
=======
                f"{coureur.couleur} échoue l'obstacle '{self.type}' à la case {position} (+{self.penalite:.1f}s)"
>>>>>>> b30bbb4cd8c1e8787595d1ada9090e376d767335
            )

            time.sleep(self.penalite)
<<<<<<< HEAD
            coureur.temps_total = coureur.temps_total + self.penalite

        else:
            messagerie.envoyer(
                coureur.couleur + " réussit l'obstacle '" +
                self.type + "' à la case " + str(position)
=======
        else:
            messagerie.envoyer(
                f"{coureur.couleur} réussit l'obstacle '{self.type}' à la case {position}"
>>>>>>> b30bbb4cd8c1e8787595d1ada9090e376d767335
            )
