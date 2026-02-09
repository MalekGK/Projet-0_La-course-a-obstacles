import threading
from Coureur import Coureur
from Obstacle import Obstacle
from Trampoline import Trampoline
from Messagerie import Messagerie
import random

#Je vais ajouter une classe qui va permettre de sauter de cases qui vont etre generer sur la piste
#Philip


class Teleporteur:

    def appliquer_T(ref, nom: str, messagerie: Messagerie, position: int, piste: Piste):
        min_position = int(piste.longueur / 2)
        max_position = piste.longueur - 1

        nouvelle_position = random.randint(min_position, max_position)

        messagerie.envoyer(
            nom + " s'est téléporté de la case " +
            str(position) + " à la case " +
            str(nouvelle_position)
        )

        return nouvelle_position

        

