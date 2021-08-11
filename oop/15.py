class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    
    def phone_name(self):
        return f"{self.brand} {self.model}"
    
    #str, repr

    def __str__(self):
        return f"{self.brand} {self.model} "
    
    def __repr__(self):
        return f"Phone(\'{self.brand}\',\'{self.model}\',{self.price})"
    
    def __len__(self):
        return len(self.phone_name())

    def __add__(self,other):
        return self.price+other.price

# l=[2,4,6,8]
# print(len(l))
# t=(1,2,3,4)
# print(len(t))
# s="1234"
# print(len(s))



p=Phone("Samsung","6",26000)
p1=Phone("Samsung","7",23000)
# print(p)
# print(str(p))
# print(repr(p))
# print(p.__repr__())

# print(len(p))

print(p1+p)