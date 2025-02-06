class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def perimètre(self):
        return (self.__longueur + self.__largeur)*2
    
    def surface(self):
        return self.__longueur * self.__largeur

# assesseurs   
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
# mutateurs   
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
        
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    def volume(self):
        return super().surface() * self.__hauteur
 
 
        
rectangle1 = Rectangle(10, 15)
print(rectangle1.perimètre())
print(rectangle1.surface())

parallelepipede1 = Parallelepipede(10, 12, 10)
print(parallelepipede1.volume())