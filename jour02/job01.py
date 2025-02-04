class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
        
    def set_largeur(self, largeur):
        self.__largeur = largeur
        
rectangle = Rectangle(7, 12)
print(rectangle.get_longueur(), rectangle.get_largeur())
rectangle.set_longueur(10)
rectangle.set_largeur(5)
print(rectangle.get_longueur(), rectangle.get_largeur())
