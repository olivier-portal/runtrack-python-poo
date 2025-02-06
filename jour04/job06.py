class Vehicule:
    def __init__(self, marque, modèle, année, prix):
        self.marque = marque
        self.modèle = modèle
        self.année = année
        self.prix = prix
        
    def informations_vehicule(self):
        print(f"Marque: {self.marque}\nModèle: {self.modèle}\nAnnée: {self.année}\nPrix: {self.prix}")
        
    def demarrer(self):
        print("Attention, je roule")
        

class Voiture(Vehicule):
    def __init__(self, marque, modèle, année, prix):
        super().__init__(marque, modèle, année, prix)
        self.portes = 4
        
    def informations_vehicule(self):
        print(f"Marque: {self.marque}\nModèle: {self.modèle}\nAnnée: {self.année}\nPrix: {self.prix}\nPortes: {self.portes}")
        
    def demarrer(self):
        print("C'est parti pour faire gronder le V8 !")

class Moto(Vehicule):
    def __init__(self, marque, modèle, année, prix):
        super().__init__(marque, modèle, année, prix)
        self.roues = 2
        
    def informations_vehicule(self):
        print(f"\nMarque: {self.marque}\nModèle: {self.modèle}\nAnnée: {self.année}\nPrix: {self.prix}\nNombre de roues: {self.roues}")
        
    def demarrer(self):
        print("Attention, j'arsouille !!!")

        
ma_voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
ma_voiture.informations_vehicule()
ma_voiture.demarrer()

ma_moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
ma_moto.informations_vehicule()
ma_moto.demarrer()