# Messagerie.py
# Malek
'''
Classe gérant les messages d'information de chaque coureur dans la course,
afin de suivre leur progression et les événements importants.
'''

import threading

class Messagerie:
    def __init__(self):
        self.lock = threading.Lock()
        self.messages = []

    def envoyer(self, message):
        with self.lock:
            self.messages.append(message)

    def afficher_archive(self):
        with self.lock:
            for msg in self.messages:
                print(msg)


    
