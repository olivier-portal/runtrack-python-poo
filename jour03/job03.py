class Tache:
    def __init__(self, titre, description, statut = "à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut
        
    def get_titre(self):
        return self.titre
    
    def get_statut(self):
        return self.statut

    def marquer_comme_finie(self):
        """Change le statut de la tâche à 'terminée'."""
        self.tatut = "terminée"
        
    def __repr__(self):
        return f"Tache(titre='{self.titre}', description='{self.description}', statut='{self.statut}')"

        
class ListeDeTaches:
    def __init__(self):
        self.taches = []
        
    def ajouter_tache(self, tache):
        self.taches.append(tache)
    
    def supprimer_tache(self, titre):
        self.taches = [tache for tache in self.taches if tache.get_titre() != titre]
        
    def marquer_comme_finie(self, titre):
        """Marque une tâche comme terminée en fonction du titre."""
        for tache in self.taches:
            if tache.get_titre() == titre:
                tache.marquer_comme_finie()
                break
        
    def afficher_liste(self):
        """Affiche toutes les tâches."""
        for tache in self.taches:
            print(tache)
            
    def filtrer_liste(self, statut):
        """Filtre les tâches par leur statut."""
        return [tache for tache in self.taches if tache.get_statut() == statut]

# Création des tâches
tache1 = Tache("Acheter des courses", "Aller au magasin pour acheter des légumes et du pain")
tache2 = Tache("Faire les devoirs", "Réviser la leçon de mathématiques et de français")
tache3 = Tache("Nettoyer la maison", "Passer l'aspirateur et laver les sols", "terminée")

# Création d'une liste de tâches         
ma_liste = ListeDeTaches()

ma_liste.ajouter_tache(tache1)
ma_liste.ajouter_tache(tache2)
ma_liste.ajouter_tache(tache3)


# Afficher toutes les tâches
print("Toutes les tâches :")
ma_liste.afficher_liste()

# Supprimer une tâche par son titre
ma_liste.supprimer_tache("Faire les devoirs")
print("\nAprès suppression de 'Faire les devoirs' :")
ma_liste.afficher_liste()

# Marquer une tâche comme terminée
ma_liste.marquer_comme_finie("Acheter des courses")
print("\nAprès avoir marqué 'Acheter des courses' comme terminée :")
ma_liste.afficher_liste()

# Afficher uniquement les tâches à faire
print("\nTâches à faire :")
taches_a_faire = ma_liste.filtrer_liste("à faire")
for tache in taches_a_faire:
    print(tache)
