# Piste.py
# Classe représentant la piste de la course
# Philip

import random
import Obstacle
import JumpPad

class Piste:
    #Philip: Piste sera un singleton car on veut pas en creer plusieurs

    _instance = None # pour verifier si un obj a ete instancier

    def __init__(cls, longueur=60, chance_case_obstacle=0.33):
        if (cls._instance is None):
            instance = super().__new__(cls) #SI l'objet n'a pas ete instancer ca le creer 
            instance.longueur = longueur
            instance.chance_case_obstacle = chance_case_obstacle
            instance.cases = instance._generer_cases()
            cls._instance = instance
        return cls._instance


    def _generer_cases(self):

        nb_cases = self.longueur
        cases = []

        for i in range (nb_cases):
            if (random.random() < self.chance_case_obstacle): #random() est une fonction qui genere un nb random entre 0.0 et 1.0

                r = random.randint(0 , 99)

                if r < 10:
                    cases.append(JumpPad(5))  # 10% jump pad 5=nb de cases sautes
                elif r < 40:
                    cases.append(Obstacle("nager"))
                elif r < 70:
                    cases.append(Obstacle("saut"))
                else:
                    cases.append(Obstacle("grimper"))
                #choisi quel obstacle prend cette case
            else:
                cases.append(None)
                #ajoute un index vide
        return cases

    def demarrerCourse():
        return None




