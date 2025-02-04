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

    def ajout_plat(self, numero_commande, plat, prix, statut):
        self.__liste_plats_commandés.append({"numéro de commande": numero_commande, "nom": plat, "prix": prix, "statut": statut})

commande_client = Commande()

commande_client.set_statut_commande("terminée")  
commande_client.ajout_plat(commande_client.numero_commande(), "Tajine", 12, commande_client.get_statut_commande())
print(commande_client.get_liste_plats_commandés())

commande_client.ajout_plat(commande_client.numero_commande(), "Couscous Royal", 15, commande_client.get_statut_commande())
print(commande_client.get_liste_plats_commandés())