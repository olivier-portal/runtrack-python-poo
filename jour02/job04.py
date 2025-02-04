class Student:
    def __init__(self,firstname, lastname, student_number):
        self.__lastname = lastname
        self.__firstname = firstname
        self.__student_number = student_number
        self.__credit_number = 0
        self.__level = self.__student_eval()
        
    def get_add_credits(self):
        return self.__credit_number
    
    def set_add_credits(self, credits):
        if type(credits) is int and credits > 0:
            self.__credit_number += credits
            self.__level = self.__student_eval()
            return self.__credit_number
        else:
            print("Le nombre de crédits doit être positif")
            
    def get_student_firstname(self):
        return self.__firstname
    
    def get_student_lastname(self):
        return self.__lastname
    
    def get_student_number(self):
        return self.__student_number
    
    def __student_eval(self):
        if self.__credit_number >= 0 and self.__credit_number < 60:
            return "Insuffisant"
        elif self.__credit_number >= 60 and self.__credit_number < 70:
            return "Passable"
        elif self.__credit_number >= 70 and self.__credit_number < 80:
            return "Bien"
        elif self.__credit_number >= 80 and self.__credit_number < 90:
            return "Très bien"
        elif self.__credit_number >= 90:
            return "Excellent"
            
    def student_info(self):
        print(f"\nNom = {self.__lastname}\nPrénom = {self.__firstname}\nid = {self.__student_number}\nNiveau = {self.__level}")
        
            
student1 = Student("John", "Doe", 145)

student1.set_add_credits(-10)
student1.set_add_credits(-10)
student1.set_add_credits(-10)

print(f"Le nombre de crédit de {student1.get_student_firstname()} {student1.get_student_lastname()} est de {student1.get_add_credits()} points")

student1.student_info()

student1.set_add_credits(30)
student1.set_add_credits(10)
student1.set_add_credits(10)

student1.student_info()