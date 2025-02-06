class Animal:
    def __init__(self, name):
        self.name = name
    
    def se_déplacer(self):
        print("L'animal se déplace")
        
class Chien(Animal):
    def __init__(self, race, name):
        self.race = race
        super().__init__(name)
    
    def se_déplacer(self):
        super().se_déplacer()
        print("Le chien court")
        
    def bruit(self):
        print("Le chien aboie")
        
class Oiseau(Animal):
    def __init__(self, couleur_plume, name):
        self.couleur_plume = couleur_plume
        super().__init__(name)
    
    def se_déplacer(self):
        super().se_déplacer()
        print("L'oiseau vole")


chient = Chien("Berger Australien", "Alpha")
chient.se_déplacer()

oiseau = Oiseau("Jaune", "Titi")
oiseau.se_déplacer()