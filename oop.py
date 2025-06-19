# Object Oriented Programming
# invovles the use of classes and objects it also has methods and properties


# Classes are blue prints of how objects are created and they behave

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def read(self):
        print(f"{self.name} is codding python")
        print(f"{self.age} is the age of the {self.name}")

student1= Student("Kimani", 19)
student1.read()


print((student1.name))
print((student1.age))

student2 = Student("Vincent", 20)
student2.read()
print((student2.name))
print((student2.age))

def greeting2():
    return "Good Morning"

print(greeting2())

print("\n")
print("___Working on given assignment___")
print("\n")

# Create a class Person with 3-4 attributes and 2 methods(behaviours)
class Person:
    def __init__(self, name, proffession, height, age,):
        self.proffession = proffession
        self.height = height
        self.age = age
        self.name = name
        
    def work(self):
        print(f"{self.name} works as a {self.proffession} in microsoft")
    def morning_routine(self):
        print("Kimani must go for mud for brakefast every morning with his buddies")
    def birthday(self):
        print(f"{self.name}is turning 20 this in  5 months from {self.age}")
        
        
person1= Person("Vincent Kimani", "Software Engineer", 63, 19)
print("This are my behaviours accorfding to what python calls them :")
person1.work()
person1.morning_routine()
person1.birthday()
print("My name is :")
print((person1.name))
print("My proffession is :")
print((person1.proffession))
print("My height is:")
print((person1.height))
print("My age is :")
print((person1.age))

print("\n")

def modifier(func):
    def inner(a, b):
        a = a + 5
        return func(a,b)
    
    return inner

def validator(func):
    def inner(a, b):
        # check if the args are of type int
        if isinstance(a, int) and isinstance(b ,int):
            return func(a, b)
        else:
            return "Args must be of type int"
    return inner
    

@modifier
@validator
def calculate(a, b):
    return a + b
@validator
def multiply(x, y):
    return x * y

print(calculate(3,3))
# print(calculate("Wed", "Thur"))
print(multiply(2, 2))
print(multiply("x", 4))