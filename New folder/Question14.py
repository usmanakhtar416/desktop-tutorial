class Vertebrate:
    def __init__(self, name):
        self.name = name
    
    def lay_eggs(self):
        return None  

class Mammal(Vertebrate):
    def __init__(self, name, is_warm_blooded=True):
        super().__init__(name)
        self.is_warm_blooded = is_warm_blooded
    
    @classmethod
    def is_mammal(cls):
        return True  

class Platypus(Mammal):
    def __init__(self, name):
        super().__init__(name)
    
    @staticmethod
    def quack():
        return "Platypus can quack!"

class Bird(Vertebrate):
    def lay_eggs(self):
        return True  
    
    def fly(self):
        return f"{self.name} is flying."

class Dinosaur(Vertebrate):
    def lay_eggs(self):
        return True  
    
    @staticmethod
    def roar():
        return "Rawrrr!"


vertebrate = Vertebrate("Generic Vertebrate")
platypus = Platypus("Perry")
bird = Bird("Sparrow")
dinosaur = Dinosaur("T-Rex")

print(platypus.quack())
print(dinosaur.roar())
print(bird.fly())
print(vertebrate.lay_eggs())