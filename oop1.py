class Dog:
    def __init__(self,name,breed,age,color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color


    def sound(self):
        print(self.name, "is barking")

dog1 = Dog("Victory", "Germany shephard",2,"white")
print(dog1.name)
dog1.sound()

dog2 = Dog("Braxton", "siberian Husky",3,"Black")
print(dog2.breed, dog2.age, dog2.color)
dog2.sound()

dog3 = Dog("Abigael", "Chihuahua",5,"Brown")
print(dog3.color)
