# Coureur.py
# Classe représentant un coureur dans la course

class Coureur:
    def __init__(self, id, vitesse, position, couleur, distance_parcourue = 0):
        self.id = id
        self.vitesse = vitesse  # Vitesse en cases par seconde
        self.position = position # Position dans la course
        self.position = couleur # Couleur du coureur(IDENTIFICATION)
        self.distance_parcourue = distance_parcourue  # Distance parcourue en cases

    def avancer(self, vitesse, distance_parcourue):
        return None