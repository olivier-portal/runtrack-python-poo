class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "à faire"
        
    def __repr__(self):
        return f"Tache(titre='{self.titre}', description='{self.description}', statut='{self.statut}')"

        
class ListeDeTaches:
    def __init__(self):
        self.taches = []
        
    def ajouter_tache(self, titre, description):
        nouvelle_tache = Tache(titre, description)
        self.taches.append(nouvelle_tache)
        return nouvelle_tache
    
    def supprimer_tache(self, titre):
        self.taches.titre = titre
        self.taches.remove(titre)
        return titre
          
ma_liste = ListeDeTaches()
print(ma_liste.ajouter_tache("réveil", "réveiller les enfants"))
print(ma_liste.supprimer_tache("réveil"))
