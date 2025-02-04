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
            return f"\nVotre {self.__marque} {self.__modèle} de l'année {self.__année} avec un kilométrage de {self.__kilométrage}km dont le niveau d'essance est de {self.__reservoir} litres peut démarrer"
        else:
            self.__en_marche = False
            return f"\nVotre {self.__marque} {self.__modèle} de l'année {self.__année} avec un kilométrage de {self.__kilométrage}km dont le niveau d'essance est de {self.__reservoir} litres ne peut pas démarrer"
            
    def arreter(self):
        self.__en_marche = False
        
    def __verifier_plein(self):
        return self.get_reservoir()
    
ma_voiture = Voiture("Nissan", "Juke", 2022, 122000)

print(ma_voiture.demarrer())

ma_voiture.set_reservoir(4)
ma_voiture.set_marque("Renault")
ma_voiture.set_modèle("Scenic")
ma_voiture.set_année(2003)
ma_voiture.set_kilométrage(459000)
print(ma_voiture.demarrer())