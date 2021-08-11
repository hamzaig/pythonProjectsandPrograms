class Laptops:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        self.brand_name=brand+' '+model

Laptop1=Laptops("Hp","Elite Book 840 G1",55000)
print(Laptop1.brand_name)