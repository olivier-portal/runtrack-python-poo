class Animal:
    def __init__(self, age = 0 , prenom = ""):
        self.age = age
        self.prenom = prenom
        
    def vieillir(add_age):
        while add_age.age == add_age.age and add_age.age < 30:
            add_age.age += 1
            print(f"l'âge de l'animal est de {add_age.age} ans")
    
    def nommer(prenom):
        print(f"L'animal se nomme {prenom}")  
        

animal_age = Animal()
print(f"l'âge de l'animal est de {animal_age.age} an")
animal_age.vieillir()

animal_name = Animal
animal_name.nommer("Luna")
