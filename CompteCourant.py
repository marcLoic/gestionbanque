from Compte import Compte

class CompteCourant(Compte):
    
    def __init__(self, numeroCompte, solde, idClient):
        super().__init__(numeroCompte, solde, idClient)