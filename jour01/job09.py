class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
        
    def calculer_prix_TTC(self):
        return self.prixHT * (1 + self.TVA)
    
    def afficher(self):
        return self.nom, self.prixHT, self.TVA, self.calculer_prix_TTC()
    
    def changer_nom(self, nouveau_nom):
        self.nom = nouveau_nom
        return self.nom
        
    def changer_prix(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT 
        return self.prixHT
    
    def afficher_nom(self):
        return self.changer_nom(self.nom)
    
    def afficher_prixHT(self):
        return self.changer_prix(self.prixHT)
    
    def afficher_prixTTC(self):
        return self.calculer_prix_TTC()


données = Produit("ordinateur", 1350, 20/100) 
print(f"Le produit: {données.afficher()[0]}\na un prix HT de : {données.afficher()[1]}€\nLa TVA est de: {données.afficher()[2]}\nLe prix TTC est de: {données.afficher()[3]}€")

données.changer_nom("Téléphone")
données.changer_prix(653)
print(f"\nLe nouveau produit est: {données.afficher_nom()}")
print(f"\nSon prix est de: {données.afficher_prixHT()}€ HT, soit {données.afficher_prixTTC()}€ TTC")

données.changer_nom("Tablette")
données.changer_prix(897)
print(f"\nLe nouveau produit est: {données.afficher_nom()}")
print(f"\nSon prix est de: {données.afficher_prixHT()}€ HT, soit {données.afficher_prixTTC()}€ TTC")