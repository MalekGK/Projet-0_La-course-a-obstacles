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
