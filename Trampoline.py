import threading
from Piste import Piste
from Coureur import Coureur
from Obstacle import Obstacle
from Trampoline import Trampoline
from Messagerie import Messagerie

#Je vais ajouter une classe qui va permettre de sauter de cases qui vont etre generer sur la piste
#Philip

class Trampoline:

    def __init__(self, saut):
        self.saut = saut

    def appliquer_trampoline(self,nom:str, messagerie:Messagerie, position:int , piste ):

           nouvelle_position = position + Trampoline.saut

           if nouvelle_position >= piste.longueur:
              
              self.position = piste.longueur 

           else:
              
              self.position = nouvelle_position

           messagerie.envoyer(f"{nom} a prit un trempolin à la case {position} jusqu'a la case{nouvelle_position}")

           return nouvelle_position


        

