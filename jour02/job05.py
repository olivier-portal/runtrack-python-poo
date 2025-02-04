class Voiture:
    def __init__(self, marque, modèle, année, kilométrage):
        self.__marque = marque
        self.__modèle = modèle
        self.__année = année
        self.__kilométrage = kilométrage
        self.__en_marche = False
        self.__reservoir = 50
        
    def get_marque(self):
        return self.__marque
    
    def set_marque(self, marque):
        self.__marque = marque
    
    def get_modèle(self):
        return self.__modèle
    
    def set_modèle(self, modèle):
        self.__modèle = modèle
    
    def get_année(self):
        return self.__année
    
    def set_année(self, année):
        self.__année = année
    
    def get_kilométrage(self):
        return self.__kilométrage
    
    def set_kilométrage(self, kilométrage):
        self.__kilométrage = kilométrage
        
    def get_en_marche(self):
        return self.__en_marche
    
    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche
        
    def get_reservoir(self):
        return self.__reservoir
    
    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir
        return self.__reservoir
        
    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            return f"Votre {self.__marque} {self.__modèle} peut démarrer"
        else:
            self.__en_marche = False
            return f"Votre {self.__marque} {self.__modèle} ne peut pas démarrer"
            
    def arreter(self):
        self.__en_marche = False
        
    def __verifier_plein(self):
        return self.get_reservoir()
    
ma_voiture = Voiture("Nissan", "Juke", 2022, 122000)

print(ma_voiture.get_reservoir())
print(ma_voiture.demarrer())

print(ma_voiture.set_reservoir(4))
print(ma_voiture.demarrer())