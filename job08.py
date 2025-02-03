import math

class Cercle:
    def __init__(self, rayon = 10):
        self.rayon = rayon
        
    def changerRayon(self):
        while self.rayon:
            try:
                self.rayon = input("Entrez le rayon du cercle: ")
                self.rayon = int(self.rayon)
                print(f"Le rayon du cercle est de {self.rayon}")
                return self.rayon
            
            except ValueError:
                print("Votre nombre doit-être un nombre entier")
                
    def diametre(self):
        calc_diametre = self.rayon * 2
        return calc_diametre
        
    def circonference(self):
        calc_circonference = int(math.pi*self.rayon)
        return calc_circonference
        
        
    def aire(self):
        calc_aire = int(2*math.pi*self.rayon**2)
        return calc_aire
        
        
    def afficherInfos(self):
        print(f"\nLe rayon du cercle est de : {self.rayon}")
        print(f"Le diamètre du cercle est de : {self.diametre()}")
        print(f"La circonférence du cercle est de : {self.circonference()}")
        print(f"L'aire du cercle est de : {self.aire()}")
        
circle = Cercle(1)
print(circle.rayon)
cercle4 = Cercle(4)
cercle7 = Cercle(7)
circle.changerRayon()
print(circle.rayon)
cercle4.afficherInfos()
cercle7.afficherInfos()