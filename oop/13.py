class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
    def full_name(self):
        return f"{self.brand} {self.model_name}"
    def make_a_call(self,number):
        return f"calling {number} ...."
    
class Smartphone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        #Two Ways
        # Phone.__init__(self,brand,model_name,price)
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera
    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

class FlagshipPhone(Smartphone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
        super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
        self.front_camera=front_camera
    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price} and camera {self.front_camera}"

phone=Phone('Nokia','3310',8000)
smartphone=Smartphone('Samsung','J6',26000,'3GB','32GB',"13MP")
flagshipPhone=FlagshipPhone('Samsung','J7',26000,'3GB','32GB',"13MP","8MP")
print(smartphone.full_name())
print(smartphone.full_name()+ f" and Price is {smartphone._price}")
print(flagshipPhone.full_name())

# print(help(FlagshipPhone))

# print(isinstance(flagshipPhone,Phone))

# print(issubclass(Smartphone,Phone))