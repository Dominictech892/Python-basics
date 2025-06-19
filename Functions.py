#1. Built-functions/Standard library functions

x = max(67, 89, 90, 23, 67, 45)
print("The maximum number is", x)

Y = min(67, 89, 90, 23, 67, 45)
print("The minimum number is", Y)

z =pow(2,3)
print("The power of z is", z)

#User Defined Functions
def greeting():
    print("Hello world")

greeting()    #Calling a function


def school():
    print("My coding school is Emobilis")
school()

#parameter and argument
def add(num1, num2):
    print(num1 + num2)

add(5 ,10)
add(20, 10)


def student(fullname, course, gender):
    print(fullname, course, gender)

student("Dominic John", "MIT", "Male")
student("Mary Mbotela", "MIT", "Female")
student("James Mbotela", "MIT", "Male")
student("Mutati John", "MIT", "Male")

#A python program that displays details of five employees
# using parameter and arguments (full name, email, age, position, salary, marriage status)


def employee(fullname, email, age, position, salary, marriagestatus):
    print(fullname, email, age, position, salary, marriagestatus)

employee("Dominic John", "johndominic92@gmail.com", 23, "Manager", float(80000),"Single")
employee("Ashley Mueni", "Mueni@gmail.com", 24, "Receptionist", float(40000),"married")
employee("Jackson kipkirui", "Jackson@gmail.com", 25, "Storekeeper", float(30000),"Single")
employee("Daniel Ochenge", "Ochenge@gmail.com", 26, "Grounds man", float(20000),"Married")
employee("Joshua Okumu", "Okumujoshua@gmail.com", 27, "Gate Man", float(15000),"Single")
