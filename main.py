from datetime import datetime
from Clients import Client
from Compte import Compte
from Operation import Operation

operation = Operation()
print("Vous devez vous connecter.")
choix = 10
login = False
while login is False:
    email = input("Entrer votre email: ")
    mdp = input("Entrer votre mot de passe: ")
    user = Client().authentification(email,mdp)
    if user:
        compteActif = Compte()
        compteActif.numeroDeCompte = Compte().rechercherCompte(user.ID)
        login = True
    else:
        print("\nEmail ou mot de passe incorrect!\n")
        
while choix != 0:
    print("\nQue souhaité vous faire :\n")
    print("1- Consulter vos comptes")
    print("2- Effectuer un virement")
    print("3- Télécharger un relever de compte")
    print("4- Créditer votre compte")
    print("5- Débiter votre compte")
    print("6- Consulter les opérations")
    print("0- Quitter")
    choix = input("\nFaites un choix: ")
    if (choix == '1'):
        print("\nLe solde de votre compte courant est: ", operation.consulterCompteCourant(compteActif.numeroDeCompte).solde)
        print("Le solde de votre compte livret est: ", operation.consulterCompteLivret(compteActif.numeroDeCompte).solde)
        operation.enregistrerOperation("consultationCompte", 0, datetime.date(datetime.now()), compteActif.numeroDeCompte)
        choix1 = input("\nAppuyer sur entrer pour quitter ou sur 'P' pour revenir en arrière: ")
        if choix1 != 'P' or choix1 != 'p':
            choix = 0
    if (choix == '2'):
        numeroCompteDestinataire = input("Entrer le numéro de compte dans le quel vous voulez virer de l'argent:")
        montantDuVirement = input("Veuillez entrer le montant du virement: ")
        idClientRecepteur = operation.consulterCompteCourant(numeroCompteDestinataire).idClient
        if idClientRecepteur == False:
            print("Numéro de compte invalide")
        else:
            check = operation.debiterCompteCourant(compteActif.numeroDeCompte, montantDuVirement, user.ID)
            if check == False:
                print("\nSolde insuffisant")
            else:
                operation.crediterCompteCourant(numeroCompteDestinataire, montantDuVirement, idClientRecepteur)
                print("\nVirement effectué avec succès")
                operation.enregistrerOperation("compteDebiter", -montantDuVirement, datetime.date(datetime.now()), compteActif.numeroDeCompte)
                operation.enregistrerOperation("compteCrediter", montantDuVirement, datetime.date(datetime.now()), numeroCompteDestinataire)
        input("\nAppuyez la touche entrer pour continuer...")
    if (choix == '3'):
        print("Cette fonctionalité n'est pas encore opérationnelle")
        input("\nAppuyez la touche entrer pour continuer...")
    if (choix == '4'):
        print("Dans quel compte voulez vous déposer de l'argent:")
        print("1- Compte courant")
        print("2- Compte livret")
        compteDestinataire = input("Faites votre choix: ")
        montantDuDepot = input("Veuillez entrer le montant du dépôt: ")
        if compteDestinataire == '1':
            nouveauSolde = operation.crediterCompteCourant(compteActif.numeroDeCompte, montantDuDepot, user.ID)
            if nouveauSolde == False: 
                print("\nIl y a une erreur! Veuillez recommencer la transaction")
            else:
                print("\nVotre nouveau solde est: ", nouveauSolde)
                operation.enregistrerOperation("compteCrediter", montantDuDepot, datetime.date(datetime.now()), compteActif.numeroDeCompte)
        if compteDestinataire == '2':
            nouveauSolde = operation.crediterCompteLivret(compteActif.numeroDeCompte, montantDuDepot, user.ID)
            if nouveauSolde == False: 
                print("\nIl y a une erreur! Veuillez recommencer la transaction")
            else:
                operation.enregistrerOperation("compteLivretCrediter", montantDuDepot, datetime.date(datetime.now()), compteActif.numeroDeCompte)
                print("\nVotre nouveau solde est: ", nouveauSolde)
        input("\nAppuyez la touche entrer pour continuer...")
    if (choix == '5'):
        print("Dans quel compte voulez vous débiter de l'argent:")
        print("1- Compte courant")
        print("2- Compte livret")
        compteDestinataire = input("Faites votre choix: ")
        montantDuRetrait = input("Veuillez entrer le montant du retrait: ")
        if compteDestinataire == '1':
            nouveauSolde = operation.debiterCompteCourant(compteActif.numeroDeCompte, montantDuRetrait, user.ID)
            if nouveauSolde == False: 
                print("\nSolde insuffisant")
            else:
                operation.enregistrerOperation("compteDebiter", montantDuRetrait, datetime.date(datetime.now()), compteActif.numeroDeCompte)
                print("\nVotre nouveau solde est: ", nouveauSolde)
        if compteDestinataire == '2':
            nouveauSolde = operation.debiterCompteLivret(compteActif.numeroDeCompte, montantDuRetrait)
            if nouveauSolde == False: 
                print("\nSolde insuffisant")
            else:
                operation.enregistrerOperation("compteLivretDebiter", montantDuRetrait, datetime.date(datetime.now()), compteActif.numeroDeCompte)
                print("\nVotre nouveau solde est: ", nouveauSolde)
        input("\nAppuyez la touche entrer pour continuer...")
    if (choix == '6'):
        print("Voici la liste de vos opérations effectuées\n")
        data = operation.consulterOperation(compteActif.numeroDeCompte)
        print(data.items())
        # for item in data:
        #     print("\nLibele: ", item)
        #     print("Mouvement: ", item[2])
        #     print("Date de l'opération:", item[3])
        choix1 = input("\nAppuyer sur entrer pour quitter ou sur 'P' pour revenir en arrière: ")
        if choix1 != 'P' or choix1 != 'p':
            choix = 0
    if (choix == 0):
        exit()