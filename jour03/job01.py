class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants
        
    def get_nom(self):
        return self.__nom
    
    def get_nombre_habitants(self):
        return self.__nombre_habitants
    
    def set_nombre_habitants(self):
        self.__nombre_habitants += 1
        
class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        
    def get_nom(self):
        return self.__nom
    
    def get_age(self):
        return self.__age
    
    def get_ville(self):
        return self.__ville
        
    def ajouterPopulation(self):
        self.__ville.set_nombre_habitants()

# création d'instances Ville        
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Récupération des arguments des instances Ville
print(f"Population de la ville de {paris.get_nom()} est de: {paris.get_nombre_habitants()} habitants")
print(f"Population de la ville de {marseille.get_nom()} est de: {marseille.get_nombre_habitants()} habitants")

# Créations d'instances Personne       
personne1 = Personne("John", 45, paris)
personne2 = Personne("Myrtille", 4, paris)
personne3 = Personne("Chloé", 18, marseille)

# Mise à jour des instances Personne
personne1.ajouterPopulation()
personne2.ajouterPopulation()
personne3.ajouterPopulation()

# Récupération des arguments modifiés des instances Ville
print(f"Mise à jour de la population de la ville de {paris.get_nom()} est de: {paris.get_nombre_habitants()} habitants")
print(f"Mise à jour de la population de la ville de {marseille.get_nom()} est de: {marseille.get_nombre_habitants()} habitants")