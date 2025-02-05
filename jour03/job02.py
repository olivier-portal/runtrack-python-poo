class CompteBancaire:
    def __init__(self):
        self.__numero_compte = 1234
        self.__nom = "Doe"
        self.__prenom = "John"
        self.__solde = 1000
        self.__decouvert = False
        
    def afficher(self):
        print(f"Le numéro de compte de {self.__nom} {self.__prenom} est le: {self.__numero_compte}. Le solde est de {self.__solde}€")
    
    def afficher_solde(self):
        if self.__solde > 0:
            print(f"Solde = {self.__solde}€")
        else:
            self.__solde += self.agios()
            print(f"Solde = {self.__solde}€")
        
    def versement(self, montant):
        self.__solde += montant
        print(f"Le nouveau solde est de: {self.__solde}€")
        
    def retrait(self, retrait):
        if self.__decouvert == True:
            self.__solde -= retrait
            print(f"Le nouveau solde est de: {self.__solde}€")
            
        elif self.__solde - retrait > 0 and self.__solde > 0 and self.__decouvert == False:
            self.__solde -= retrait
            print(f"Le nouveau solde est de: {self.__solde}€")
        
        else:
            print(f"Vous n'avez pas les fonds pour retirer cette somme, il vous reste {self.__solde}€")
            
    def autorisation_decouvert(self, autorisation: bool):
        self.__decouvert = autorisation
        
    def agios(self):
        if self.__solde < 0:
            self.__solde -= abs(self.__solde) * 5/100 + self.__solde
            return self.__solde
        else:
            return self.__solde
        
        
mon_compte = CompteBancaire()

mon_compte.afficher_solde()

mon_compte.versement(150)
mon_compte.retrait(78)

mon_compte.retrait(1100)

mon_compte.autorisation_decouvert(True)

mon_compte.versement(150)
mon_compte.afficher_solde()
mon_compte.retrait(1300)
mon_compte.afficher_solde()
mon_compte.retrait(10)
mon_compte.afficher_solde()