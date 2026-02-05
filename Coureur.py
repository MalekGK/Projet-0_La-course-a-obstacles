# Coureur.py
# Classe représentant un coureur dans la course
# Malek
# TERMINÉ

import uuid
import random
import time
from Piste import Piste

class Coureur:
    POSITION_DEFAULT = 0
    VITESSE_MIN = 1
    VITESSE_MAX = 3
    #Philip: Joueur devra avoir temps total.Je dirai pas de distance parcouru mais en combien de temps car c'est la meme piste

    def __init__(self, couleur: str):
        self.id = str(uuid.uuid4()) # Id du joueur
        self.couleur = couleur # Couleur du coureur(IDENTIFICATION)
        self.position = Coureur.POSITION_DEFAULT # Position dans la course
        self.vitesse = Coureur.VITESSE_MIN # Vitesse en secondes par case
        self.temps_total = 0 # Temps du coureur du début jusqu'à la fin de la course
        # Le temps sera instancier au moment du départ de la course, par time_perf_counter()


    
    # Méthode qui retourne le nombre de secondes que prend un coureur à changer de case
    def avancer(self, vitesse) -> int:
        vitesse = Coureur.modifier_vitesse()

        return vitesse
    
    # Modifie la vitesse du coureur(Secondes que le coureur prend pour passer d'une case de la piste à l'autre)
    def modifier_vitesse() -> int:
        return random.randint(Coureur.VITESSE_MIN, Coureur.VITESSE_MAX)
