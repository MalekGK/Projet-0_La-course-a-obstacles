import threading
import Piste
import Coureur
import Obstacle
import Trempoline

#Je vais ajouter une classe qui va permettre de sauter de cases qui vont etre generer sur la piste
#Philip

class Trempoline:

    def __init__(self, saut):
        self.saut = saut

    def appliquer_JP(ref,nom, messagerie , position , piste ):

           nouvelle_position = position + Trempoline.saut

           if nouvelle_position >= piste.longueur:
              
              self.position = piste.longueur 

           else:
              
              self.position = nouvelle_position

           messagerie.envoyer(f"{nom} a prit un trempolin à la case {position} jusqu'a la case{nouvelle_position}")

           return nouvelle_position


        

