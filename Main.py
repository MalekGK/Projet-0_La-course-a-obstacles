import threading
import time
import os
from Piste import Piste
from Coureur import Coureur
from Obstacle import Obstacle
from Trampoline import Trampoline
from Teleporteur import Teleporteur
from Messagerie import Messagerie

# Main.py
# Classe qui sert à exécuter le programme principal

# Création des joueurs → 3 threads différents
# Les threads vont partager la classe piste concurremment
# La messagerie est protégée par un verrou
# Chaque joueur avance avec une vitesse aléatoire ou une pénalité
# La classe obstacle détermine le résultat
# Le programme se termine lorsque tous les threads ont fini


class Main:

    DUREE_MESSAGE = 2.0       # Durée d'affichage d'un message
    RAFRAICHISSEMENT = 10     # Rafraîchissement de l'affichage console

    def __init__(self):
        self.positions = {}
        self.messages = {}
        self.lock = threading.Lock()

    @staticmethod
    def decompte(secondes: int):
        for i in range(secondes):
            print(f"...{secondes - i}")
            time.sleep(1)
        print("\nPartez!")

    # Met à jour la position d’un coureur (protégé par verrou)
    def regler_position(self, couleur: str, pos: int):
        with self.lock:
            self.positions[couleur] = pos

    # Ajoute ou met à jour le message d’un coureur
    def set_message(self, couleur: str, message: str):
        with self.lock:
            self.messages[couleur] = (time.perf_counter(), message)

    # Nettoie les messages expirés
    def nettoyer_messages(self):
        maintenant = time.perf_counter()

        for couleur in self.messages:
            temps, msg = self.messages[couleur]

            if (maintenant - temps) > self.DUREE_MESSAGE:
                self.messages[couleur] = (temps, "")

    # Thread d’affichage console
    # Affiche position + message de chaque coureur
    def fil_affichage(self, arreter_evenement, couleurs, messagerie):
        os.system('cls')
        while not arreter_evenement.is_set():
            with self.lock:
                self.nettoyer_messages()
                lignes = []

                print("\033[33m----------- LA COURSE A OBSTACLES -----------\033[0\n")

                for couleur in couleurs:
                    position = self.positions.get(couleur, 0)
                    msg = self.messages.get(couleur, (0, ""))[1]
                    lignes.append(f"\033[32m{couleur}: position = {position:2d} | {msg}\033[0\n")

                # Ajouter les messages de la messagerie en dessous
                with messagerie.lock:
                    if messagerie.messages:
                        lignes.append("\n\033[1;31m--- Événements ---\033[0\n")
                        for msg in messagerie.messages[-5:]:  # Afficher les 5 derniers messages
                            lignes.append(f"{msg}\n")

                print("".join(lignes), end="") # Trouvé sur internet
                time.sleep(1.5)
                os.system('cls')


    # Thread exécuté par chaque coureur
    def fil_coureur(self, coureur, messagerie, resultats, demarrer_evenement, lock_resultats):

        demarrer_evenement.wait()

        temps_initial = time.perf_counter()

        self.regler_position(coureur.couleur, coureur.position)
        self.set_message(coureur.couleur, "Départ!")

        while coureur.position < coureur.piste.longueur:

            case = coureur.piste.cases[coureur.position]

            if case is None:

                temps = coureur.avancer()

                self.set_message(
                    coureur.couleur,
                    f"avance (+{temps}s)"
                )

                time.sleep(temps)
                coureur.position += 1

            elif isinstance(case, Trampoline):

                saut = getattr(case, "saut", 5)

                ancienne = coureur.position

                coureur.position = min(
                    coureur.position + saut,
                    coureur.piste.longueur
                )

                self.set_message(
                    coureur.couleur,
                    f"Trampoline: {ancienne}->{coureur.position}"
                )

            # Téléporteur
            elif isinstance(case, Teleporteur):

                ancienne = coureur.position

                coureur.position = Teleporteur.appliquer_T(
                    coureur.couleur,
                    messagerie,
                    coureur.position,
                    coureur.piste
                )

                self.set_message(
                    coureur.couleur,
                    f"Teleporteur: {ancienne}->{coureur.position}"
                )

            # Obstacle
            elif isinstance(case, Obstacle):

                self.set_message(coureur.couleur, "Obstacle!")

                try:
                    case.appliquer(
                        coureur,
                        messagerie,
                        coureur.position
                    )

                except Exception as e:

                    self.set_message(
                        coureur.couleur,
                        f"Erreur obstacle: {e}"
                    )

                coureur.position += 1

            else:
                coureur.position += 1

            self.regler_position(
                coureur.couleur,
                coureur.position
            )

        # Fin de course
        temps_total = time.perf_counter() - temps_initial

        self.set_message(
            coureur.couleur,
            f"Terminé en {temps_total:.2f}s"
        )

        with lock_resultats:
            resultats.append(
                (temps_total, coureur.couleur)
            )

    # Programme principal
    def demarrer(self):

        piste = Piste()
        messagerie = Messagerie()

        couleurs = ["Rouge", "Bleu", "Jaune"]

        coureurs = [
            Coureur("Rouge", piste),
            Coureur("Bleu", piste),
            Coureur("Jaune", piste)
        ]

        # Initialisation affichage
        for couleur in couleurs:
            self.positions[couleur] = 0
            self.messages[couleur] = (0, "")

        resultats = []
        fils = []

        demarrer_evenement = threading.Event()
        lock_resultats = threading.Lock()

        # Thread affichage
        arreter_affichage = threading.Event()

        print("********** BIENVENUE À LA COURSE À OBSTACLES **********")

        input("\nÊtes-vous prêt? (Entrée...)")

        Main.decompte(3)

        fil_aff = threading.Thread(target=self.fil_affichage, args=(arreter_affichage, couleurs, messagerie), daemon=True)
        fil_aff.start()

        # Threads coureurs
        for coureur in coureurs:

            fil = threading.Thread(
                target=self.fil_coureur,
                args=(
                    coureur,
                    messagerie,
                    resultats,
                    demarrer_evenement,
                    lock_resultats
                )
            )

            fils.append(fil)
            fil.start()

        demarrer_evenement.set()

        # Attente de fin
        for fil in fils:
            fil.join()

        arreter_affichage.set()
        time.sleep(0.2)

        # Classement final, trouvé avec internet
        resultats.sort(key=lambda x: x[0])

        print("\n\033[33m--- CLASSEMENT ---\033[0m")

        for i, (temps, couleur) in enumerate(resultats, 1):
            print(f"{i}. {couleur} - {temps:.2f}s")

        print("\nArchive des événements:")
        messagerie.afficher_archive()

Main().demarrer()
