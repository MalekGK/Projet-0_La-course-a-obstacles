# Coureur.py
# Classe représentant un coureur dans la course
# Malek

class Coureur:
    def __init__(self, id, position, couleur, vitesse = 1, distance_parcourue = 0):
        self.id = id # Id du joueur
        self.position = position # Position dans la course
        self.couleur = couleur # Couleur du coureur(IDENTIFICATION)
        self.vitesse = vitesse  # Vitesse en secondes par cases
        self.distance_parcourue = distance_parcourue # Distance parcourue en cases

    # Méthode qui retourne le nombre de secondes que prend un coureur à changer de case
    def avancer(self, vitesse):
        return None
    
    def modifierVitesse(self):
        return None