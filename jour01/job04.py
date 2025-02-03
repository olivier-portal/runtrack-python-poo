class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
        
    def se_presenter(prenom, nom):
        print(f"Je suis {prenom} {nom}")
        
      
personne1 = Personne.se_presenter("John", "Doe")
personne2 = Personne.se_presenter("Jean", "Dupond")