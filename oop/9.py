class Person:
    count_instances=0
    def __init__(self,first_name,last_name,age):
        Person.count_instances+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    @classmethod
    def from_string(cls,string):
        first_name,last_name,age=string.split(",")
        return cls(first_name,last_name,age)
    @classmethod
    def count_instance(cls):
        return f"You have created {cls.count_instances} instances of {cls.__name__}"
    def full_name(self):
        return self.first_name+" "+self.last_name
    def is_above_18(self):
        return self.age>18
    
p1=Person('Hamza','Ali',18)
p2=Person('Hamza','Ali',14)

p3=Person.from_string("Hamza,Ali,20")
print(p3.full_name())
