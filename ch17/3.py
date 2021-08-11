class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        raise NotImplementedError("Please Implement Sound Method")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        return "Bow Bow"

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        return "Meao Meao"
    

dogy=Dog("A","B")
print(dogy.sound())