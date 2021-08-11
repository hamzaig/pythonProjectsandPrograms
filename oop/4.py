class Laptops:
    def __init__(self,brand,brand_model,price):
        self.brand=brand
        self.brand_model=brand_model
        self.price=price
        self.laptop_name=brand+" "+brand_model
    def apply_discount(self,num):
        off_price=(num/100)*self.price
        return self.price - off_price
    
l1=Laptops("Hp","Elite Book 840 G3",100000)
l2=Laptops("Dell","Smart Book 340 F3",255000)
print(l1.apply_discount(10))

