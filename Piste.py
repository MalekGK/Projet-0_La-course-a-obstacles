# Piste.py
# Classe représentant la piste de la course
# Philip

import random
from Obstacle import Obstacle
from Trampoline import Trampoline
from Teleporteur import Teleporteur

class Piste:

    def __init__(self, longueur=60, chance_case_obstacle=0.33):
            self.longueur = longueur
            self.chance_case_obstacle = chance_case_obstacle
            self.cases = self._generer_cases()


    def _generer_cases(self):

        nb_cases = self.longueur
        cases = []

        for i in range (nb_cases):
            if (random.random() < self.chance_case_obstacle): #random() est une fonction qui genere un nb random entre 0.0 et 1.0

                r = random.randint(0 , 99)

                if r < 3:
                    cases.append(Teleporteur())
                elif r < 10:
                    cases.append(Trampoline(5))  # 10% jump pad 5=nb de cases sautes
                elif r < 40:
                    cases.append(Obstacle("nager"))
                elif r < 70:
                    cases.append(Obstacle("saut"))
                else:
                    cases.append(Obstacle("grimpe"))
                #choisi quel obstacle prend cette case
            else:
                cases.append(None)
                #ajoute un index vide
        return cases

    def demarrerCourse(self):
        return None




