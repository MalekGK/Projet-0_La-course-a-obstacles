import threading;

# Main.py
# Classe qui sert à exécuter le programme principal

# Creation des joueurs 3threads differents
# Les threads vont partager la classe piste concuremment
# Messagerie ne va pas etre concurrente alors un verrou
# Chaque joueur va avoir une chance de passer la piste avec une augmentation de vitesse ou une penalite
# Classe obstacle determine le resultat
# Fini avec le dernier thread qui fini