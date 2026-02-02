# Messagerie.py
# Malek
'''
Classe gérant les messages d'information de chaque coureur dans la course,
afin de suivre leur progression et les événements importants.
'''

class Messagerie:

    def __init__(self):
        self.messages = []

    def envoyer(self, message):
        self.archiver(message)
        self.afficher(message)

    def archiver(self, message):
        self.messages.append(message)

    def afficher_archive(self):
        for msg in self.messages:
            print(msg)

    def afficher(self, message):
        print(message)


    
