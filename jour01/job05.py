class Point:
    def __init__(self, x = 10.5 , y = 5.2):
        self.x = x
        self.y = y
        
    def afficher_les_points(coordonees):
        print(f"Les coordonnées du point est de {coordonees.x} et {coordonees.y}")
        
    def afficher_x(abscisse):
        print(f"l'abscisse du point est {abscisse.x}")
        
    def afficher_y(ordonee):
        print(f"l'ordonnée du point est {ordonee.y}")
        
    def changer_x(abscisse):
        x = input(f"Entrez une nouvelle abscisse de {abscisse.x}: ")
        print(f"la nouvelle abscisse du point est {x}")
        return x
        
    def changer_y(ordonee):
        y = input(f"Entrez une nouvelle abscisse de {ordonee.y}: ")
        print(f"la nouvelle ordonnée du point est {y}")
        return y

point1 = Point()        
point1.afficher_les_points()
point1.afficher_x()
point1.afficher_y()
point1.changer_x()
point1.changer_y()

