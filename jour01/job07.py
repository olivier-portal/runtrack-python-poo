class Personnage:
    def __init__(self, x = 0 , y = 0):
        self.x = x
        self.y = y
        
    def gauche(left):
        left.x -= 1
        gauche = int(left.x)
        print(f"La position en x est de {gauche}")
        
    def droite(right):
        right.x += 1
        droite = int(right.x)
        print(f"La position en x est de {droite}")
        
    def haut(top):
        top.y += 1
        haut = int(top.y)
        print(f"La position en x est de {haut}")
        
    def bas(bottom):
        bottom.y -= 1
        bas = int(bottom.y)
        print(f"La position en x est de {bas}")
        
    def position(self):
        localisation = (self.x, self.y)
        print(f"Le personnage se situe aux coordonnées: {localisation}")
        
        
            
pos_personnage = Personnage()
pos_personnage.gauche()
pos_personnage.droite()
pos_personnage.haut()
pos_personnage.haut()
pos_personnage.haut()
pos_personnage.bas()
pos_personnage.droite()
pos_personnage.position()

  
        
