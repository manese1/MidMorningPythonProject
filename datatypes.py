age = 18 #Integer
length = 45.6 #Float
greeting = "Hello there" #String
hasFeathers = True #Boolean

#Data Structures - Multiple values stored in one variable.
fruits = ["Pineapple", "Banana", "Mango"] #List - Ordered and changeable
courses = ["MIT", "Data Science", "Cybersecurity"] #Arrary - Similar data types
cars = ("Mercedes", "Ford", "Nissan", "Subaru") #Tuple - Ordered and Unchangeable
countries = {"India", "Zambia", "Canada"} #Set - Unordered and Unchangeable
student = {
    "firstname": "Esther",
    "course": "MIT",
    "age": 19,
    "nationality": "Pakistani",
    "gender": "Female"
} #Dictionary - Key Value pair

print(age)
print("The length is",length)
print(fruits)
print(countries)
print(student)
print(student["nationality"])

#Typecasting - Conversion of one data type to another
print(float(age))
print(int(length))