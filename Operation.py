import os
import random
from Clients import Client

from Compte import Compte

class Operation:

    def __init__(self, *args):
        if  len(args) == 1:
            self.ID = args[0]
        elif len(args) == 2:
            self.ID = args[0]
            self.libele = args[1]
        elif len(args) == 3:
            self.ID = args[0]
            self.libele = args[1]
            self.mouvement = args[2]
        elif len(args) == 4:
            self.ID = args[0]
            self.libele = args[1]
            self.mouvement = args[2]
            self.dateOperation = args[3]
        elif len(args) == 4:
            self.ID = args[0]
            self.libele = args[1]
            self.mouvement = args[2]
            self.dateOperation = args[3]
            self.numeroDeCompte = args[4]

    def enregistrerOperation(self, libele, mouvement, dateOperation, numeroDeCompte):
        self.ID = random.randint(1, 10000)
        self.libele = libele
        self.mouvement = mouvement
        self.dateOperation = dateOperation
        self.numeroDeCompte = numeroDeCompte
        try:
            with open("operation.txt", "a") as fichier:
                fichier.write(f"{self.ID};{self.libele};{self.mouvement};{self.dateOperation};{self.numeroDeCompte};\n")
                fichier.close()
                print("Opération validée\n")
            return Operation(self.ID, self.libele, self.mouvement, self.dateOperation, self.numeroDeCompte)
        except IOError:
            print("Erreur lors de la création de l'opération")
            return False

    def ouvrirCompte():
        pass
    
    def debiterCompteCourant(self, numeroDeCompte, montant, idClient):
        try:
            original = open("comptecourant.txt", "r")
            tempFile = open("tempcourant.txt", "w")
            s = ' '
            newMontant = 0
            while (s):
                s = original.readline()
                L = s.split(";")
                if L[0] == numeroDeCompte:
                    if (int(L[1]) - int(montant)) < 0:
                        return False
                    newMontant = int(L[1]) - int(montant)
                    tempFile.write(numeroDeCompte+";"+str(newMontant)+";"+idClient+";\n")
                else:
                    tempFile.write(s)
            original.close()
            tempFile.close()
            os.remove("comptecourant.txt")
            os.rename("tempcourant.txt", "comptecourant.txt")
            return newMontant
        except IOError:
            print["Hello world"]
            return False

    def debiterCompteLivret(self, numeroDeCompte, montant, idClient):
        try:
            original = open("comptelivret.txt", "r")
            tempFile = open("templivret.txt", "w")
            s = ' '
            while (s):
                s = original.readline()
                L = s.split(";")
                if L[0] == numeroDeCompte:
                    if (int(L[1]) - int(montant)) < 0:
                        return False
                    newMontant = int(L[1]) - int(montant)
                    tempFile.write(numeroDeCompte+";"+str(newMontant)+";"+idClient+";\n")
                else:
                    tempFile.write(s)
            original.close()
            tempFile.close()
            os.remove("comptelivret.txt")
            os.rename("templivret.txt", "comptelivret.txt")
            return newMontant
        except IOError:
            return False

    def crediterCompteCourant(self, numeroDeCompte, montant, idClient):
        try:
            original = open("comptecourant.txt", "r")
            tempFile = open("tempcourant.txt", "w")
            s = ' '
            while (s):
                s = original.readline()
                L = s.split(";")
                if L[0] == numeroDeCompte:
                    newMontant = int(L[1]) + int(montant)
                    tempFile.write(numeroDeCompte+";"+str(newMontant)+";"+idClient+";\n")
                else:
                    tempFile.write(s)
            original.close()
            tempFile.close()
            os.remove("comptecourant.txt")
            os.rename("tempcourant.txt", "comptecourant.txt")
            return newMontant
        except IOError:
            return False

    def crediterCompteLivret(self, numeroDeCompte, montant, idClient):
        try:
            original = open("comptelivret.txt", "r")
            tempFile = open("templivret.txt", "w")
            s = ' '
            while (s):
                s = original.readline()
                L = s.split(";")
                if L[0] == numeroDeCompte:
                    newMontant = int(L[1]) + int(montant)
                    tempFile.write(numeroDeCompte+";"+str(newMontant)+";"+idClient+";\n")
                else:
                    tempFile.write(s)
            original.close()
            tempFile.close()
            os.remove("comptelivret.txt")
            os.rename("templivret.txt", "comptelivret.txt")
            return newMontant
        except IOError:
            return False

    def effectuerVirement():
        pass

    def envoyerRelever():
        pass

    def consulterCompteLivret(self, numeroDeCompte):
        try:
            with open("comptelivret.txt", "r") as fichier:
                readfile = fichier.readlines()
                for compte in readfile:
                    if compte.split(";")[0] == numeroDeCompte:
                        return Compte(compte.split(";")[0],compte.split(";")[1],compte.split(";")[2])
                fichier.close()
        except IOError:
            return False
    
    def consulterCompteCourant(self, numeroDeCompte):
        try:
            with open("comptecourant.txt", "r") as fichier:
                readfile = fichier.readlines()
                for compte in readfile:
                    if compte.split(";")[0] == numeroDeCompte:
                        return Compte(compte.split(";")[0],compte.split(";")[1],compte.split(";")[2])
                fichier.close()
        except IOError:
            return False

    def consulterOperation(self, numeroDeCompte):
        try:
            data = {}
            with open("operation.txt", "r") as fichier:
                readfile = fichier.readlines()
                result = Operation()
                i = 0
                for operation in readfile:
                    if operation.split(";")[4] == numeroDeCompte:
                        result.ID = operation.split(";")[0]
                        result.libele = operation.split(";")[1]
                        result.mouvement = operation.split(";")[2]
                        result.dateOperation = operation.split(";")[3]
                        result.numeroDeCompte = operation.split(";")[4]
                        child = {
                            "id" : operation.split(";")[0],
                            "libele" : operation.split(";")[1],
                            "mouvement" : operation.split(";")[2],
                            "dateoperation" : operation.split(";")[3],
                            "numerodecompte" : operation.split(";")[4],
                        }
                        data["child"+str(i)] = child
                    i += 1
                fichier.close()
            return data
        except IOError:
            return False