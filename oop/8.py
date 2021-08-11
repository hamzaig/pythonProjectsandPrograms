class Person:
    instances_counter=0
    def __init__(self,first_name,last_name,age):
        Person.instances_counter+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    @classmethod
    def count_instances(cls):
        return f'You have created {cls.instances_counter} instances of {cls.__name__} that class'
    def fullname(self):
        return self.first_name+" "+self.last_name
    def is_above_18(self):
        return self.age>18
    
p1=Person("Hamza","Ali",19)
p2=Person("Hamza","Ali",29)

print(Person.count_instances())