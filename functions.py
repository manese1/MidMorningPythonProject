#Functions/Methods - Block of code used to perform a task

#Standard Library Functions/In-built Functions
y = max(56, 67, 84, 90, 10, 30, 9876, 9768)
print(y)
x = min(793, 736, 893, 673, 427, 387, 902)
print(x)

#User-Defined Functions
def school():
    print("eMobilis")
school()
def product():
    print(15*5)
product()
#Parameters/Variables
#Argumant/Values
def product(a, b):
    print(a * b)
product(34, 10)
product(28, 20)
def student(name, age, gender):
    print(name, age, gender)
student("Lewis", "19", "Male")
student("Christian", "18", "Male")
student("Clement", "20", "Male")

#User-defined fn for details of 5 employees at eMobilis. The details are; Fullname, Position, Age, Gender

def employees(fullname, position, age, gender):
    print(fullname, position,  age, gender)
employees("Wilberforce Wafula", "Director", "50", "Male")
employees("Christian Mwangi", "Technician", "28", "Male")
employees("Clement Kimani", "Lecturer", "40", "Male")
employees("Glory Akinyi", "Lecturer", "37", "Female")
employees("Mary Wambui", "Receptionist", "25", "Female")
