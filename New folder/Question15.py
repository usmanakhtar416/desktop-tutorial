class Animal:
    def breathe(self):
        return "Breathing..."

class Pet:
    def cuddle(self):
        return "Cuddling..."

class Dog(Animal, Pet): 
    def bark(self):
        return "Woof!"

dog = Dog()
print(dog.breathe()) 
print(dog.cuddle()) 
print(dog.bark())     



print("-------------------------------------")


class Animal:
    def move(self):
        return "Moving..."

class Mammal(Animal):
    def warm_blooded(self):
        return "I am warm-blooded."

class Dog(Mammal):  
    def bark(self):
        return "Woof!"

dog = Dog()
print(dog.move())        
print(dog.warm_blooded())
print(dog.bark())      


print("-------------------------------------")



class Animal:
    def eat(self):
        return "Eating..."

class Dog(Animal):
    def bark(self):
        return "Woof!"

class Cat(Animal):
    def meow(self):
        return "Meow!"

dog = Dog()
cat = Cat()

print(dog.eat()) 
print(dog.bark())
print(cat.eat())  
print(cat.meow()) 