# Use name plus = for declaration of variable

name = "Max Santos"
age = 23
course = "Master in Software Engineering"
university = "Universidade Federal do Estado de São Paulo - USP"
h = 1.88
is_student = True   

print("My name is " + name + " and I'm " + str(age) + " years old.")
print("I'm studying " + course + " at " + university)
print("")
# Variables types 
print("Variables types:")

"""
    int = Whole numbers
    float = Real numbers 
    str = Textual data
    bool = Logical values
"""
print(type(age))
print(type(h))
print(type(name))
print(type(is_student))
print("")


print("Interation with user:")
#  Receved datas and salved in a variable
Name = input("Enter your name: ")
age =  input("Enter your age: ")
print("Hello " + Name + " your age is " + age)

language = input("Enter your language: ")
# Use ',' for concat string plus variables or variable with variable
print("You are styding " ,language)