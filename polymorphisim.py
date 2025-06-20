class Animal:
    def sound(self):
        print("Animal is speaking")


class Cat:
    def sound(self):
        print("Cat says: Meow..!")

class Dog:
    def sound(self):
        print("Dog says: Woof!!")

a = Animal()
a.sound()

b = Cat()
b.sound()

c = Dog()
c.sound()