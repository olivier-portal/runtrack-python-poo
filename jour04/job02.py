class Personne:
    def __init__(self):
        self.age = 14
        
    def afficher_age(self):
        print(f"L'age de la personne est de : {self.age}")
        
    def bonjour(self):
        print("Hello")
        
    def modifier_age(self, age):
        self.age = age
        

class Eleve(Personne):
    def __init__(self):
        super().__init__()
        
    def allerEnCours(self):
        print("Je vais en cours")
        
    def afficher_age(self):
        print(f"J'ai {self.age} ans")
        

class Professeur(Personne):
    def __init__(self):
        super().__init__()
        self.__matière_enseignee = "Python"

    def enseigner(self):
        print(f"Le cours de {self.__matière_enseignee} va commencer")
        
eleve1 = Eleve()
eleve1.bonjour()
eleve1.allerEnCours()
eleve1.modifier_age(15)
eleve1.afficher_age()

professeur1 = Professeur()
professeur1.bonjour()
professeur1.modifier_age(40)
professeur1.enseigner()
