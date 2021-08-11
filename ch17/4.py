class Mobile:
    def __init__(self,name):
        self.name=name

class Mobile_Store:
    def __init__(self):
        self.mobiles=[]

    def add_mobiles(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError("new mobile should be object of Mobil Class")

j6=Mobile("Samsung J6")
mob="Oppo"
ms=Mobile_Store()
ms.add_mobiles(j6)
print(ms.mobiles[0].name)
