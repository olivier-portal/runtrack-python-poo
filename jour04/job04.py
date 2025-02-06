class Forme:
    def __init__(self):
        self.aire_forme = 0
    
    def aire(self):
        return self.aire_forme


class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        super().__init__()
        self.__longueur = longueur
        self.__largeur = largeur
        
    def aire(self):
        super().aire()
        return self.__longueur * self.__largeur
        
forme1 = Forme()
print(forme1.aire())

forme2 = Rectangle(10, 15)
print(forme2.aire())