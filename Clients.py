import random

from Compte import Compte

class Client:

    def __init__(self, *args):
        if  len(args) == 1:
            self.ID = args[0]
        elif len(args) == 2:
            self.ID = args[0]
            self.email = args[1]
        elif len(args) == 3:
            self.ID = args[0]
            self.email = args[1]
            self.username = args[2]
        elif len(args) == 4:
            self.ID = args[0]
            self.email = args[1]
            self.username = args[2]
            self.motDePasse = args[3]

    def authentification(self, email, motDePasse):
        self.email = email
        self.motDePasse = motDePasse
        try:
            with open("client.txt", "r") as fichier:
                readfile = fichier.readlines()
                for client in readfile:
                    if client.split(";")[1] == self.email and client.split(";")[3] == motDePasse:
                        test = Client(client.split(";")[0],client.split(";")[1],client.split(";")[2])
                        return test
                fichier.close()
        except IOError:
            return False
    
    def creerClient(self, idBanque):
        print("Création d'un client:")
        self.email = input("Entrer l'email : ")
        self.username = input("Entrer le username : ")
        self.motDePasse = input("Entrer le mot de passe : ")
        self.ID = random.randint(1,10000)
        self.idBanque = idBanque
        compte = Compte()
        compte.creerCompte(self.ID)
        try:
            with open("client.txt", "a") as fichier:
                fichier.write(f"{self.ID};{self.email};{self.username};{self.motDePasse};\n")
                fichier.close()
            print("Client crée")
            return Client(self.ID, self.email, self.username, self.motDePasse)
        except IOError:
            print("Erreur de création du client")
            return False
    
    def consulterClient(self):
        try:
            with open("client.txt", "r") as fichier:
                readfile = fichier.readlines()
                for client in readfile:
                    print("ID:", client.split(";")[0])
                    print("Email:", client.split(";")[1])
                    print("Username:", client.split(";")[2])
                    print("Mot de passe:", client.split(";")[3])
                fichier.close()
            return True
        except IOError:
            return False


# Client().CreerClient(4)