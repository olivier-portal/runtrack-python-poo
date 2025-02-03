class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        
    def addition(nombre1, nombre2):
        result = nombre1 + nombre2
        print(f"Le résultat de l'addition du nombre1 et du nombre2 est de {result}")
        
Operation.addition(12, 3)

