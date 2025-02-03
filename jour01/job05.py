class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def afficher_les_points(x, y):
        print(f"Les coordonnées du point est de {x} et {y}")
        
    def afficher_x(x):
        print(f"l'abscisse du point est {x}")
        
    def afficher_y(y):
        print(f"l'ordonnée du point est {y}")
        
    def changer_x(x):
        x = input(f"Entrez une nouvelle abscisse de {x}: ")
        print(f"la nouvelle abscisse du point est {x}")
        
    def changer_y(y):
        y = input(f"Entrez une nouvelle abscisse de {y}: ")
        print(f"la nouvelle ordonnée du point est {y}")
        
coordonees = Point.afficher_les_points(10.3, 5.2)
abscisse = Point.afficher_x(10.3)
ordonnée = Point.afficher_y(5.2)
nouvelle_abscisse = Point.changer_x(10.3)
nouvelle_ordonée = Point.changer_y(5.2)

