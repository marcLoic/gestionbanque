class Compte:
    def __init__(self, numero, depot, type, libelle, idClient):
        self.numero = numero
        self.solde = depot
        self.type = type
        self.libelle = libelle
        self.idClient = idClient
        self.operations = []

    def debiter(self, montant):
        if (montant <= self.solde):
            self.solde = self.solde - montant
            self.operations.append("Débit " + str(montant))
            return ("Compte débité de " + str(montant))
        else:
            return ("Solde insuffisant.")

    def crediter(self, montant):
        self.solde = self.solde + montant
        self.operations.append("Crédit " + str(montant))
        return ("Compte credité de " + str(montant))

    def effectuerVirement(self, montant, compte):
        if (montant <= self.monant):
            self.debiter(montant)
            compte.crediter(montant)
            return ("Opération effectuée.")
        else:
            return ("Solde insuffisant pour effectuer le virement.")

    def solde(self):
        print("Solde : "+self.solde())

    def envoyerReleve(self):
        for operation in self.operations:
            print(operation)

class Client:
    def __init__(self, nom, adresse, idClient):
        self.nom = nom
        self.adresse = adresse
        self.idClient = idClient

class Banque:

    def __init__(self, ID, nom):
        self.ID = ID
        self.nom = nom

class CompteCourant(Compte):
    
    def __init__(self, numeroCompte, solde):
        super().__init__(numeroCompte, solde)

class CompteLivret(Compte):

    def __init__(self, numeroCompte, solde, interet):
        super().__init__(numeroCompte, solde)
        self.interet = interet

    def CalculerInteret():
        pass

class Operation:

    def __init__(self, ID, nom, type, dateOperation) :
        self.ID = ID
        self.nom = nom
        self.type = type
        self.dateOperation = dateOperation

    def OuvrirCompte():
        pass

    def DebiterCompte():
        pass

    def CrediterCompte():
        pass

    def EffectuerVirement():
        pass

    def EnvoyerRelever():
        pass

    def ConsulterCompte():
        pass

clients = []
comptes = []
choix = 9
cpt = 0
clt = 0
while choix != 0:
    print("Que souhaitez-vous faire :")
    print("1- Ouvrir un compte")
    print("2- Débiter un compte")
    print("3- Créditer un compte")
    print("4- Effectuer un virement")
    print("5- Créditer les intérêts")
    print("6- Envoyer un relevé")
    print("7- Liste des comptes")
    print("8- Liste des clients")
    print("0- Quitter")
    choix = input()
    if (choix == "1"):
        clt = clt + 1
        print("Informations Client")
        print("Entrez votre nom : ")
        nom = input()
        print("Entrez votre adresse : ")
        adresse = input()
        print("Choisissez un type de compte :")
        print("1- Courant")
        print("2- Livret")
        cpt = input()
        if(cpt == "1"):
            print("Entrez un libellé : ")
            libelle = input()
            print("Combien souhaitez-vous déposer : ")
            depot = int(input())
            tempClt = Client(nom, adresse, clt)
            clients.append(tempClt)
            tempCpt = Compte(clt, depot, "Courant", libelle, clt)
            comptes.append(tempCpt)
            print("Compte créé")
        if (cpt == "2"):
            print("Entrez un libellé : ")
            libelle = input()
            print("Combien souhaitez-vous déposer : ")
            depot = int(input())
            tempClt = Client(nom, adresse, clt)
            clients.append(tempClt)
            tempCpt = Compte(clt, depot, "Livret", libelle, clt)
            comptes.append(tempCpt)
            print("Compte créé")
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if (choix == "2"):
        print("Quel compte souhaitez-vous débiter ? Saisissez le numero de compte")
        for compte in comptes:
            print("Numero de compte: " + str(compte.numero) + " | Solde: " + str(compte.solde) + " | Type de compte: " + str(compte.type) + " | Identifiant Client: " + str(compte.idClient))
        debit = int(input())
        print("De combien souhaitez-vous débiter le compte ?")
        montant = int(input())
        comptes[debit-1].debiter(montant)
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if (choix == "3"):
        print("Quel compte souhaitez-vous créditer ? Saisissez le numero de compte")
        for compte in comptes:
            print("Numero de compte: " + str(compte.numero) + " | Solde: " + str(compte.solde) + " | Type de compte: " + str(compte.type) + " | Identifiant Client: " + str(compte.idClient))
        credit = int(input())
        print("De combien souhaitez-vous créditer le compte ?")
        montant = int(input())
        comptes[credit-1].crediter(montant)
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if (choix == "4"):
        print("Quel compte souhaitez-vous débiter ? Saisissez le numero de compte")
        for compte in comptes:
            print("Numero de compte: " + str(compte.numero) + " | Solde: " + str(compte.solde) + " | Type de compte: " + str(compte.type) + " | Identifiant Client: " + str(compte.idClient))
        debit = int(input())
        print("De combien souhaitez-vous débiter le compte ?")
        montant = int(input())
        print("Quel compte souhaitez-vous créditer ? Saisissez le numero de compte")
        for compte in comptes:
            print("Numero de compte: " + str(compte.numero) + " | Solde: " + str(compte.solde) + " | Type de compte: " + str(compte.type) + " | Identifiant Client: " + str(compte.idClient))
        credit = int(input())
        comptes[debit - 1].effectuerVirement(montant, comptes[credit-1])
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if (choix == "7"):
        for compte in comptes:
            print("Numero de compte: "+str(compte.numero)+" | Solde: "+str(compte.solde)+" | Type de compte: "+str(compte.type)+" | Identifiant Client: "+str(compte.idClient))
    # -----------------------------------------------------------------------------------------------------------
    if (choix == "8"):
        for client in clients:
            print (str(client.idClient)+" "+str(client.nom)+" "+str(client.adresse))
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if (choix == "0"):
        exit()