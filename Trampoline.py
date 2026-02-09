from Messagerie import Messagerie

class Trampoline:

    def __init__(self, saut):
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
