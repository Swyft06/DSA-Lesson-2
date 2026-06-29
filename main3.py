class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print("I make a sound")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")
    
class Cat(Animal):
    def speak(self):
        print("Meow! Meow!")

dog = Dog("Buddy")
dog.speak()

cat = Cat("Whiskers")
cat.speak()