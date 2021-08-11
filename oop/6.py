class Laptops:
    discount_percent=10
    def __init__(self,brand,brand_model,price):
        self.brand=brand
        self.brand_model=brand_model
        self.price=price
        self.laptop_name=brand+" "+brand_model
    def apply_discount(self):
        off_price=(self.discount_percent/100)*self.price
        return self.price - off_price
# To reset the Discount Variable
# Laptops.discount_percent=0    
l1=Laptops("Hp","Elite Book 840 G3",150000)
l2=Laptops("Dell","Smart Book 340 F3",255000)
# print(l1.apply_discount())
l2.discount_percent=50
print(l1.__dict__)
print(l2.apply_discount())

