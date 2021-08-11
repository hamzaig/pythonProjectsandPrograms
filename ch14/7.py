from functools import wraps

def dec(fun):
    "hello fun"
    @wraps(fun)
    def wrapper(*args,**kwargs):
        "Hello wrapper"
        print("hello")
        return fun(*args,**kwargs)
    return wrapper

@dec
def add(a,b):
    "Hello add"
    return a+b
# print(add(5,5))
print(add.__doc__)

