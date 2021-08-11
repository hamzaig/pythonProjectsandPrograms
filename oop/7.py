class Person:
    object_counter=0
    def __init__(self,first_name,last_name,age):
        Person.object_counter+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

p1=Person("Hamza","Ali",23)
p2=Person("Hamza","Ali",24)
print(Person.object_counter)
