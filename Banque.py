

import random
from Clients import Client


class Banque:

    def __init__(self):
        self.ID = ""
        self.nom = ""

    def CreationClient():
        client = Client()
        client.CreerClient()

    def creerBanque(self, nom):
        self.ID = random.randint(1,10000)
        self.nom = nom
        try:
            with open("banque.txt", "a") as fichier:
                fichier.write(f"{self.ID};{self.nom}\n")
                fichier.close()
            return True
        except IOError:
            return False