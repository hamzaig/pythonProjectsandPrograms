def dec(fun):
    def wrapper(*args,**kwargs):
        print("Hello")
        return fun(*args,**kwargs)
    return wrapper

@dec
def fun(x):
    print("fun")

# fun(7)

@dec
def add(x,y):
    return x+y

print(add(5,5))