class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__disponible = True
        
    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nombre_pages(self):
        return self.__nombre_pages
    
    def set_titre(self, titre):
        self.__titre = titre
        
    def set_auteur(self, auteur):
        self.__auteur = auteur
        
    def set_nombre_pages(self, nombre_pages):
        if isinstance(nombre_pages, int) and nombre_pages > 0:
            self.__nombre_pages = nombre_pages
        else:
            print("Erreur: Le nombre de pages doit être un nombre entier positif")
            
    def get_vérification(self):
        return self.__disponible
        
    def set_vérification(self, disponible):
        self.__disponible = disponible
        if disponible == True:
            print(f"Le livre {self.__titre} est disponible")
        else:
            print(f"Le livre {self.__titre} n'est pas disponible")
        return self.__disponible
            
    def emprunter(self):
        if self.get_vérification():
            print(f"\nVous venez d'emprunter le livre {self.__titre}")
            self.set_vérification(False)
        else:
            print(f"\nVous ne pouvez-pas emprunter le livre {self.__titre}")
            
    def rendre(self):
        if not self.get_vérification():
            print(f"\nVous venez de rendre le livre {self.__titre}")
            self.set_vérification(True)
        else:
            print(f"\nVous avez toujours le livre {self.__titre} en votre possession")

livre = Livre("Sapiens", "Yuval Noah Harari", 289)
print(f"Le titre du livre est {livre.get_titre()}, son auteur est {livre.get_auteur()} et son nombre de pages est de {livre.get_nombre_pages()}")

livre.set_titre("La plaisanterie")
livre.set_auteur("Milan Kundera")
livre.set_nombre_pages(10.5)
livre.set_nombre_pages(256)

print(f"Le titre du livre est {livre.get_titre()}, son auteur est {livre.get_auteur()} et son nombre de pages est de {livre.get_nombre_pages()}")

livre.set_vérification(True)
livre.emprunter()
livre.rendre()
livre.emprunter()

livre.set_vérification(False)
livre.emprunter()
livre.rendre()
livre.emprunter()