class student:
    #properties/Attributes
    name ="Dominic"
    gender = "male"
    age = 25

    def study(self):
        print("Student is studying")

    def movement(self):
        print("Student is walking")

student1 = student() #Creating an object
student1.movement()

print(student1.age)

student2 = student()
print(student2.name)
