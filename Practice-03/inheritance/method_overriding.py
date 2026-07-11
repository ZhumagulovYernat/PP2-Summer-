class Animal:
    def sound(self):
        print("Some sound")


class Cat(Animal):
    def sound(self):
        print("Meow")


class Dog(Animal):
    def sound(self):
        print("Woof")


animal = Animal()
cat = Cat()
dog = Dog()

animal.sound()
cat.sound()
dog.sound()