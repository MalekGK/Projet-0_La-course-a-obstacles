import Messagerie

import random

import Piste

class Teleporteur:

   def appliquer_T(ref, nom:str, messagerie:Messagerie, position:int , piste:Piste ):

        rand = random.randint(piste.longueur/2 , piste.longueur)

        nouvelle_position = rand

        messagerie.envoyer(f"{nom} s'est teleporte de la case {position} a la case{nouvelle_position}")

        return nouvelle_position