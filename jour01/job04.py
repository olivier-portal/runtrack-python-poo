class Personne:
    def __init__(self, prenom = "Olivier", nom = "Portal"):
        self.prenom = prenom
        self.nom = nom
        
    def se_presenter(presenter):
        print(f"Je suis {presenter.prenom} {presenter.nom}")
        
Personne().se_presenter()      
Personne("John", "Doe").se_presenter()
Personne("Jean", "Dupond").se_presenter()