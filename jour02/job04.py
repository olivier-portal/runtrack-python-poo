class Student:
    def __init__(self,firstname, lastname, student_number):
        self.__lastname = lastname
        self.__firstname = firstname
        self.__student_number = student_number
        self.__credit_number = 0
        
    def get_add_credits(self):
        return self.__credit_number
    
    def set_add_credits(self, credits):
        if type(credits) is int and credits > 0:
            self.__credit_number += credits
        else:
            print("The number of credits must be positive")
            
    def get_student_firstname(self):
        return self.__firstname
    
    def get_student_lastname(self):
        return self.__lastname
    
    def get_student_number(self):
        return self.__student_number
            
student1 = Student("John", "Doe", 145)

student1.set_add_credits(10)
student1.set_add_credits(10)
student1.set_add_credits(10)

print(f"Le nombre de crédit de {student1.get_student_firstname()} {student1.get_student_lastname()} est de {student1.get_add_credits()} points")