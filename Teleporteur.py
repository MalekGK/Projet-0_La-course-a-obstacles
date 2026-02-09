<<<<<<< HEAD
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

        

=======
# Teleporteur.py
# Téléporte le coureur à une case aléatoire dans la deuxième moitié de la piste

import random

class Teleporteur:

    @staticmethod
    def appliquer_T(nom, messagerie, position, piste):
        debut = int(piste.longueur / 2)
        fin = int(piste.longueur)

        nouvelle_position = random.randint(debut, fin)

        messagerie.envoyer(
            f"{nom} s'est téléporté de la case {position} à la case {nouvelle_position}"
        )

        return nouvelle_position
>>>>>>> b30bbb4cd8c1e8787595d1ada9090e376d767335
