<<<<<<< HEAD
from Messagerie import Messagerie
=======
# import threading
# from Piste import Piste
# from Coureur import Coureur
# from Obstacle import Obstacle
# from Trampoline import Trampoline
# from Messagerie import Messagerie
>>>>>>> b30bbb4cd8c1e8787595d1ada9090e376d767335

class Trampoline:

    def __init__(self, saut):
<<<<<<< HEAD
        self.saut = saut

    def appliquer_trampoline(self, nom: str, messagerie: Messagerie, position: int, piste):
        nouvelle_position = position + self.saut

        if nouvelle_position >= piste.longueur:
            nouvelle_position = piste.longueur - 1

        messagerie.envoyer(
            nom + " a pris un trampoline à la case " +
            str(position) + " jusqu'à la case " +
            str(nouvelle_position)
        )

        return nouvelle_position
=======
        self.saut = saut
>>>>>>> b30bbb4cd8c1e8787595d1ada9090e376d767335
