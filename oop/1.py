class Person:
    def __init__(self,first_name,last_name,age):
        #instance variables
        print("This is calling constructer")
        self.first_name=first_name
        self.last_name=last_name
        self.age=age


p1=Person('Hamza','Ali',18)
p2=Person('Khalid','Ali',18)

print(p1.first_name)
print(p2.first_name)
