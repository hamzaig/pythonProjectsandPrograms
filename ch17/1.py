class Animal:
    def __init__(self,name):
        self.name=name
    
    def sound(self):
        return "This is Animal Sound"

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed

d=Dog("Boony","Pug")
print(d.sound())


