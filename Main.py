
import threading
import time

from Piste import Piste
from Coureur import Coureur
from Obstacle import Obstacle
from Trampoline import Trampoline
from Teleporteur import Teleporteur
from Messagerie import Messagerie


class Main:
    def __init__(self, argument=None):
        self.argument = argument


    def decompte(secondes: int):
        for i in range(secondes):
            print("..." + str(secondes - i))
            time.sleep(1)
        print("\nPartez!")


    def fil_coureur(self, coureur, piste, messagerie, resultats, demarrer_evenement, barrer):
        demarrer_evenement.wait()

        coureur.position = 0
        coureur.temps_total = 0

        messagerie.envoyer(coureur.couleur + " démarre la course")

        while coureur.position < piste.longueur - 1:
            v = coureur.avancer()
            time.sleep(v)

            messagerie.envoyer(
                coureur.couleur + " est à la case " + str(coureur.position) +
                " (temps total: " + format(coureur.temps_total, ".2f") + "s)"
            )

            case = piste.cases[coureur.position]

            if case is None:
                pass

            else:
                if isinstance(case, Obstacle):
                    case.appliquer(coureur, messagerie, coureur.position)

                elif isinstance(case, Teleporteur):
                    nouvelle_position = Teleporteur.appliquer_T(
                        None, coureur.couleur, messagerie, coureur.position, piste
                    )

                    if nouvelle_position >= piste.longueur:
                        coureur.position = piste.longueur - 1
                    else:
                        coureur.position = nouvelle_position

                elif isinstance(case, Trampoline):
                    nouvelle_position = case.appliquer_trampoline(
                        coureur.couleur, messagerie, coureur.position, piste
                    )

                    if nouvelle_position >= piste.longueur:
                        coureur.position = piste.longueur - 1
                    else:
                        coureur.position = nouvelle_position

        messagerie.envoyer(
            coureur.couleur + " termine en " + format(coureur.temps_total, ".2f") + "s"
        )

        barrer.acquire()
        resultats.append(coureur)
        barrer.release()


    def demarrer(self):
        piste = Piste()
        messagerie = Messagerie()

        coureur1 = Coureur("Rouge")
        coureur2 = Coureur("Bleu")
        coureur3 = Coureur("Jaune")

        coureurs = [coureur1, coureur2, coureur3]

        resultats = []
        fils = []

        demarrer_evenement = threading.Event()
        barrer = threading.Lock()

        for coureur in coureurs:
            fil = threading.Thread(
                target=self.fil_coureur,
                args=(coureur, piste, messagerie, resultats, demarrer_evenement, barrer)
            )

            fils.append(fil)
            fil.start()

        print("********** BIENVENUE À LA COURSE À OBSTACLES **********")
        input("\nÊtes-vous prêt? (Appuyer sur entrer pour continuer...)")

        Main.decompte(3)
        demarrer_evenement.set()

        for fil in fils:
            fil.join()

        print("")
        print("=== CLASSEMENT FINAL ===")

        if len(resultats) == 3:
            c1 = resultats[0]
            c2 = resultats[1]
            c3 = resultats[2]

            if c1.temps_total <= c2.temps_total and c1.temps_total <= c3.temps_total:
                premier = c1
                if c2.temps_total <= c3.temps_total:
                    deuxieme = c2
                    troisieme = c3
                else:
                    deuxieme = c3
                    troisieme = c2

            elif c2.temps_total <= c1.temps_total and c2.temps_total <= c3.temps_total:
                premier = c2
                if c1.temps_total <= c3.temps_total:
                    deuxieme = c1
                    troisieme = c3
                else:
                    deuxieme = c3
                    troisieme = c1

            else:
                premier = c3
                if c1.temps_total <= c2.temps_total:
                    deuxieme = c1
                    troisieme = c2
                else:
                    deuxieme = c2
                    troisieme = c1

            print("1. " + premier.couleur + " - " + format(premier.temps_total, ".2f") + "s")
            print("2. " + deuxieme.couleur + " - " + format(deuxieme.temps_total, ".2f") + "s")
            print("3. " + troisieme.couleur + " - " + format(troisieme.temps_total, ".2f") + "s")


main = Main()
main.demarrer()

# Main.py
# Classe qui sert à exécuter le programme principal

# Creation des joueurs 3threads differents
# Les threads vont partager la classe piste concuremment
# Messagerie ne va pas etre concurrente alors un verrou
# Chaque joueur va avoir une chance de passer la piste avec une augmentation de vitesse ou une penalite
# Classe obstacle determine le resultat
# Fini avec le dernier thread qui fini


# class Main:
#     def __init__(self, argument = None):
#         self.argument = argument

#     def decompte(secondes: int):
#         for i in range(secondes):
#             print(f"...{secondes - i}")
#             time.sleep(1)
#         print("\nPartez!")

#     def demarrer(self):
#         piste = Piste()
#         messagerie = Messagerie()

#         coureurs = [
#             Coureur("Rouge"),
#             Coureur("Bleu"),
#             Coureur("Jaune")
#         ]
#         resultats = []
#         fils = []

#         demarrer_evenement = threading.Event()
#         barrer = threading.Lock()

#         for coureur in coureurs:
#             fil = threading.Thread(
#                 target=self.fil_coureur,
#                 args=(coureur, messagerie, resultats, demarrer_evenement, barrer)
#             )

#             fils.Append(fil)
#             fil.start

#         print("********** BIENVENUE À LA COURSE À OBSTACLES **********")
#         commencer = input("\nÊtes-vous prêt?(Appuyer sur entrer pour continuer...)")
#         Main.decompte(3)
#         demarrer_evenement.set()

#         for fil in fils:
#             fil.join()
    
    
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