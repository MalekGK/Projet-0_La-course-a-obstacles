import threading
import time
from Piste import Piste
from Coureur import Coureur
from Obstacle import Obstacle
from Trampoline import Trampoline
from Messagerie import Messagerie

# Main.py
# Classe qui sert à exécuter le programme principal

# Creation des joueurs 3threads differents
# Les threads vont partager la classe piste concuremment
# Messagerie ne va pas etre concurrente alors un verrou
# Chaque joueur va avoir une chance de passer la piste avec une augmentation de vitesse ou une penalite
# Classe obstacle determine le resultat
# Fini avec le dernier thread qui fini

class Main:
    def __init__(self, argument = None):
        self.argument = argument

    def decompte(secondes: int):
        for i in range(secondes):
            print(f"...{secondes - i}")
            time.sleep(1)
        print("\nPartez!")

    def demarrer(self):
        piste = Piste()
        messagerie = Messagerie()

        coureurs = [
            Coureur("Rouge"),
            Coureur("Bleu"),
            Coureur("Jaune")
        ]
        resultats = []
        fils = []

        demarrer_evenement = threading.Event()
        barrer = threading.Lock()

        for coureur in coureurs:
            fil = threading.Thread(
                target=self.fil_coureur,
                args=(coureur, messagerie, resultats, demarrer_evenement, barrer)
            )

            fils.Append(fil)
            fil.start

        print("********** BIENVENUE À LA COURSE À OBSTACLES **********")
        commencer = input("\nÊtes-vous prêt?(Appuyer sur entrer pour continuer...)")
        Main.decompte(3)
        demarrer_evenement.set()

        for fil in fils:
            fil.join()
        


















# self.position = 0

# while self.position < self.piste.longueur:
#     case = self.piste.cases[self.position]

#     self.messagerie.envoyer(f"{self.nom} est à la case {self.position}")

#     if case is None:
#         self.position += 1

#     elif isinstance(case, Trempoline): # verifie si la case est de type de jump pad
#         self.messagerie.envoyer(f"{self.nom} trouve un JumpPad (+5 cases)")

#         nouvelle_position = self.position + 5

#         if nouvelle_position >= self.piste.longueur:
#             self.position = self.piste.longueur
#         else:
#             self.position = nouvelle_position


#     elif isinstance(case, Obstacle):
#         case.appliquer(self, self.messagerie, self.position)  #Passe une position et l'objet messagerie
        # self.position += 1


# Coureur bleu = Coureur