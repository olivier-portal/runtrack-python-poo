class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
    def se_presenter(nom, prenom):
        print(f"Je suis {nom} {prenom}")
        
personne1 = Personne.se_presenter("John", "Doe")
personne2 = Personne.se_presenter("Jean", "Dupond")