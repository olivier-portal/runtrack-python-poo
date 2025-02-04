class Commande:
    def __init__(self):
        self.__numéro_commande = 0
        self.__liste_plats_commandés = []
        self.__statut_commande = "en cours"

# define getter and setter
        
    def numero_commande(self):
        self.__numéro_commande += 1
        return self.__numéro_commande
        
    def get_liste_plats_commandés(self):
        return self.__liste_plats_commandés
    
    def set_liste_plats_commandés(self, liste_plats_commandés):
        self.__liste_plats_commandés = liste_plats_commandés
        
    def get_statut_commande(self):
        return self.__statut_commande
    
    def set_statut_commande(self, statut_commande):
        self.__statut_commande = statut_commande
        
# define method to add a dish

    def ajout_plat(self, plat, prix, statut):
        self.__liste_plats_commandés.append({"nom": plat, "prix": prix, "statut": statut})
        
# define method to cancel a dish

    def annuler_commande(self):
        if self.__statut_commande == "en cours":
            self.__statut_commande = "annulée"
            print(f"Votre commande est {self.__statut_commande[2]}")
        else:
            print(f"Vous ne pouvez pas annulé une commande {self.__statut_commande[1]}")
            
# define a method to calculate the total price

    def __calcul_prix(self):
        total = 0
        for plat in self.__liste_plats_commandés:
            if plat["statut"] != "annulée":
                total += plat["prix"]
        return total
            
# define a method to show the priceetotal price to pay

    def afficher_commande(self):
        print(f"La commande {self.get_liste_plats_commandés()} est de {self.__calcul_prix()}€, avec {self.calcul_TVA()}€ de TVA")
 
 # define method to calculate the amount of TVA       
    def calcul_TVA(self):
        return self.__calcul_prix() * 20/100

commande_client = Commande()

commande_client.set_statut_commande("terminée")  
commande_client.ajout_plat("Tajine", 12, commande_client.get_statut_commande())
print(commande_client.get_liste_plats_commandés())

commande_client.set_statut_commande("en cours") 
commande_client.ajout_plat("Couscous Royal", 15, commande_client.get_statut_commande())
print(commande_client.get_liste_plats_commandés())

commande_client.set_statut_commande("annulée") 
commande_client.ajout_plat("Couscous Royal", 15, commande_client.get_statut_commande())
print(commande_client.get_liste_plats_commandés())

print(commande_client.afficher_commande())