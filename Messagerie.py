

# Messagerie.py
# Malek
'''
Classe gérant les messages d'information de chaque coureur dans la course,
afin de suivre leur progression et les événements importants.
'''

import threading

class Messagerie:
    def __init__(self):
        self._lock = threading.Lock()
        self.messages = []

    def envoyer(self, message):
        with self._lock:
            self.messages.append(message)
            print(message)

    def afficher_archive(self):
        with self._lock:
            for msg in self.messages:
                print(msg)


    
