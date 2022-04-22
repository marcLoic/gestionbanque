import random

class Compte: 

    def __init__(self, *args):
        if  len(args) == 1:
            self.numeroDeCompte = args[0]
        elif len(args) == 2:
            self.numeroDeCompte = args[0]
            self.solde = args[1]
        elif len(args) == 3:
            self.numeroDeCompte = args[0]
            self.solde = args[1]
            self.idClient = args[2]

    def creerCompte(self, ID):
        self.idClient = ID
        self.numeroDeCompte = random.randint(1,10000)
        self.solde = 0
        try:
            print("\nCréation du compte\n")
            with open("comptecourant.txt", "a") as fichier:
                fichier.write(f"{self.numeroDeCompte};{self.solde};{self.idClient};\n")
                fichier.close()
                print("Compte courant crée\n")
            with open("comptelivret.txt", "a") as fichier:
                fichier.write(f"{self.numeroDeCompte};{self.solde};{self.idClient};\n")
                fichier.close()
                print("Compte livret crée\n")
            return True
        except IOError:
            print("Erreur de création du compte")
            return False
    def rechercherCompte(self, idClient):
        try:
            with open("comptecourant.txt", "r") as fichier:
                readfile = fichier.readlines()
                for compte in readfile:
                    if compte.split(";")[2] == idClient:
                        return compte.split(";")[0]
                fichier.close()
        except IOError:
            print("Compte n'existe pas !!!")
            return 0