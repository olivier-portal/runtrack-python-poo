import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
        
    def __str__(self):
        return f"{self.valeur} de {self.couleur}"
    

class Jeu:
    def __init__(self):
        self.paquet = []
        self.initialiser_paquet()
        self.melanger()
        
    def initialiser_paquet(self):
        couleurs = ["Coeur", "Carreau", "Pique", "Trèfle"]
        valeurs = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
            "Valet": 10, "Dame": 10, "Roi": 10, "As": 11
        }
        
        for couleur in couleurs:
            for valeur, points in valeurs.items():
                self.paquet.append(Carte(valeur, couleur))
                
    def melanger(self):
        random.shuffle(self.paquet)
        
    def piocher(self):
        """Pioche une carte du paquet"""
        return self.paquet.pop() if self.paquet else None
    
    def afficher_paquet(self):
        """Affiche toutes les cartes du paquet"""
        for carte in self.paquet:
            print(carte)
            
            
class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []
        self.score = 0
        
    def ajouter_carte(self, carte):
        self.main.append(carte)
            
            
    def calculer_score(self):
        """Calcule la valeur totale de la main en prenant en compte l'As (1 ou 11)"""
        score = 0
        nombre_as = 0  # Nombre d'As dans la main

        for carte in self.main:
            if carte.valeur == "As":
                nombre_as += 1
                score += 11  # L'As est compté comme 11 par défaut
            elif carte.valeur in ["Valet", "Dame", "Roi"]:
                score += 10  # Les figures valent 10 points
            else:
                score += int(carte.valeur)  # Valeurs numériques normales

        # Ajustement des As si le score dépasse 21
        while score > 21 and nombre_as > 0:
            score -= 10  # Transforme un As de 11 à 1
            nombre_as -= 1

        return score
    
    def décider_action(self):
        """Demande au joueur s'il veut piocher ou passer"""
        while True:
            choix = input(f"{self.nom}, voulez-vous prendre une carte ? (o/n) : ").strip().lower()
            if choix in ["o"]:
                return "prendre"
            elif choix in ["n"]:
                return "passer"
            else:
                print("Réponse invalide, veuillez entrer 'oui' ou 'non'.")
                
                
class Croupier(Joueur):
    def __init__(self, nom):
        super().__init__(nom)
        
    def jouer(self):
        if self.score <= 17:
            self.ajouter_carte()
    
    
jeu = Jeu()
# jeu.afficher_paquet()
print(jeu.piocher())

joueur = Joueur("Jinx")
joueur.ajouter_carte(Carte("As", "Cœur"))
joueur.ajouter_carte(Carte("9", "Pique"))

print(f"{joueur.nom} a un score de : {joueur.calculer_score()}")

action = joueur.décider_action()
print(f"{joueur.nom} a choisi de {action}.")