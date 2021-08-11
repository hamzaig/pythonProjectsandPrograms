class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def calculate_circumeference(self):
        return 2*Circle.pi*self.radius

c=Circle(4)
c1=Circle(5)
print(c1.calculate_circumeference())