class NameTooShort(ValueError):
    pass
def validate(name):
    if len(name)<8:
        raise NameTooShort("Name is Too Short")

username=input("Please Enter Your Username")
validate(username)
print(username)
