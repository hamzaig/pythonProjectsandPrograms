class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        if price>0:
            self._price=price
        else:
            self._price=max(price,0)
        # self.prop=f"{self.brand} {self.model} and Price {self._price}"
    @property
    def description(self):
        return f"{self.brand} {self.model} and Price {self._price}"
    @property
    def price(self):
        return self._price
    @price.setter
    def prices(self,new_price):
        self._price=max(new_price,0)


phone1=Phone('Samsung','J6',26000)
phone1.prices=10000
print(phone1._price)
# print(phone1.description)

        