import random

class Carte:
    """Représente une carte avec une valeur et une couleur."""
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    """Gère le paquet de cartes (création, mélange et pioche)."""
    def __init__(self):
        self.paquet = []
        self.initialiser_paquet()
        self.melanger()

    def initialiser_paquet(self):
        """Crée un paquet de 52 cartes."""
        couleurs = ["Cœur", "Carreau", "Trèfle", "Pique"]
        valeurs = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
            "Valet": 10, "Dame": 10, "Roi": 10, "As": 11  # L'As peut valoir 1 ou 11
        }

        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))

    def melanger(self):
        """Mélange les cartes du paquet."""
        random.shuffle(self.paquet)

    def piocher(self):
        """Pioche une carte du paquet."""
        return self.paquet.pop() if self.paquet else None

class Joueur:
    """Représente un joueur avec une main de cartes."""
    def __init__(self, nom):
        self.nom = nom
        self.main = []  # Liste des cartes
        self.score = 0  # Score total du joueur

    def ajouter_carte(self, carte):
        """Ajoute une carte à la main du joueur."""
        self.main.append(carte)

    def calculer_score(self):
        """Calcule le score total en tenant compte des As (1 ou 11)."""
        score = 0
        nombre_as = 0

        for carte in self.main:
            if carte.valeur == "As":
                nombre_as += 1
                score += 11  # On suppose d'abord que l'As vaut 11
            elif carte.valeur in ["Valet", "Dame", "Roi"]:
                score += 10  # Les figures valent 10 points
            else:
                score += int(carte.valeur)

        # Ajuster les As si le score dépasse 21
        while score > 21 and nombre_as > 0:
            score -= 10  # Transformer un As de 11 à 1
            nombre_as -= 1

        return score

    def décider_action(self):
        """Demande au joueur s'il veut piocher ou passer."""
        while True:
            choix = input(f"{self.nom}, voulez-vous prendre une carte ? (oui/non) : ").strip().lower()
            if choix in ["oui", "o"]:
                return "prendre"
            elif choix in ["non", "n"]:
                return "passer"
            else:
                print("Réponse invalide, veuillez entrer 'oui' ou 'non'.")

class Croupier(Joueur):
    """Le croupier suit des règles spécifiques."""
    def __init__(self):
        super().__init__("Croupier")

    def jouer(self, jeu):
        """Le croupier tire des cartes jusqu'à obtenir au moins 17 points."""
        while self.calculer_score() < 17:
            carte = jeu.piocher()
            self.ajouter_carte(carte)
            print(f"Le croupier pioche : {carte}")

class Blackjack:
    """Gère le déroulement d'une partie de Blackjack."""
    def __init__(self):
        self.jeu = Jeu()
        self.joueur = Joueur(input("Entrez votre nom : "))
        self.croupier = Croupier()

    def distribuer_cartes(self):
        """Distribue deux cartes à chaque joueur."""
        for _ in range(2):
            self.joueur.ajouter_carte(self.jeu.piocher())
            self.croupier.ajouter_carte(self.jeu.piocher())

    def afficher_mains(self, cacher_croupier=True):
        """Affiche les mains des joueurs, avec la possibilité de cacher une carte du croupier."""
        print(f"\n{self.joueur.nom} a les cartes : " + ", ".join(str(c) for c in self.joueur.main))
        print(f"Score actuel : {self.joueur.calculer_score()}")
        
        if cacher_croupier:
            print(f"\nCroupier montre : {self.croupier.main[0]} et une carte cachée.")
        else:
            print(f"\nCroupier a les cartes : " + ", ".join(str(c) for c in self.croupier.main))
            print(f"Score du croupier : {self.croupier.calculer_score()}")

    def tour_joueur(self):
        """Gère le tour du joueur."""
        while self.joueur.calculer_score() < 21:
            action = self.joueur.décider_action()
            if action == "prendre":
                carte = self.jeu.piocher()
                self.joueur.ajouter_carte(carte)
                print(f"Vous piochez : {carte}")
                self.afficher_mains()
            else:
                break

    def déterminer_gagnant(self):
        """Détermine le gagnant de la partie."""
        score_joueur = self.joueur.calculer_score()
        score_croupier = self.croupier.calculer_score()

        print("\n--- Résultat final ---")
        self.afficher_mains(cacher_croupier=False)

        if score_joueur > 21:
            print(f"{self.joueur.nom} a dépassé 21 ! Vous perdez. 😢")
        elif score_croupier > 21 or score_joueur > score_croupier:
            print(f"Félicitations {self.joueur.nom}, vous gagnez ! 🎉")
        elif score_joueur < score_croupier:
            print("Le croupier gagne. 😞")
        else:
            print("Égalité ! 🤝")

    def démarrer_partie(self):
        """Démarre une partie de Blackjack."""
        self.distribuer_cartes()
        self.afficher_mains()

        # Tour du joueur
        self.tour_joueur()

        # Si le joueur n'a pas dépassé 21, le croupier joue
        if self.joueur.calculer_score() <= 21:
            print("\n--- Tour du croupier ---")
            self.croupier.jouer(self.jeu)

        # Déterminer le gagnant
        self.déterminer_gagnant()

# Exécuter le jeu
if __name__ == "__main__":
    game = Blackjack()
    game.démarrer_partie()
