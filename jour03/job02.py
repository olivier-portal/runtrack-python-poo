class CompteBancaire:
    def __init__(self, numero_compte):
        self.__numero_compte = numero_compte
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
        
    def virement(self, destinataire, montant):
        if self.__solde >= montant:
            self.__solde -= montant
            destinataire.__solde += montant
            print(f"Vous venez de faire un virement de {montant}€ au compte {destinataire.__numero_compte}")

        else:
            print(f"Vous ne pouvez pas faire de virement sur le compte {self.__numero_compte}, le montant de {montant}€ est supérieur à votre solde de {self.__solde}€")
        
        
mon_compte = CompteBancaire(1234)

mon_compte.afficher_solde()

mon_compte.versement(150)
mon_compte.retrait(78)

mon_compte.retrait(1100)

mon_compte.autorisation_decouvert(True)

mon_compte.versement(150)
mon_compte.afficher_solde()
mon_compte.retrait(1300)
mon_compte.afficher_solde()
mon_compte.versement(1500)
mon_compte.afficher_solde()

mon_compte2 = CompteBancaire(12345)
mon_compte2.autorisation_decouvert(True)
mon_compte2.retrait(2100)
mon_compte2.afficher_solde()

mon_compte.virement(mon_compte2, 1155)
mon_compte.afficher_solde()
mon_compte2.afficher_solde()
