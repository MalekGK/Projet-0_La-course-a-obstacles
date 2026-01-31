# Coureur.py
# Classe représentant un coureur dans la course
# Malek
import random

class Coureur:
    VITESSE_MIN = 1
    VITESSE_MAX = 5
    #Philip: Joueur devra avoir temps total.Je dirai pas de distance parcouru mais en combien de temps car c'est la meme piste

    def __init__(self, id: int, position: int, couleur: str, vitesse = 1, distance_parcourue = 0):
        self.id = id # Id du joueur
        self.position = position # Position dans la course
        self.couleur = couleur # Couleur du coureur(IDENTIFICATION)
        self.vitesse = vitesse  # Vitesse en secondes par cases
        self.distance_parcourue = distance_parcourue # Distance parcourue en cases


    
    # Méthode qui retourne le nombre de secondes que prend un coureur à changer de case
    def avancer(self, vitesse):
        return None
    
    # Modifie la vitesse du coureur(Secondes que le coureur prend pour passer d'une case de la piste à l'autre)
    def modifier_vitesse() -> int:
        return random.randint(Coureur.VITESSE_MIN, Coureur.VITESSE_MAX)
