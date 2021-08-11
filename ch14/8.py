from functools import wraps
def dec(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"you are calling {func.__name__} function")
        print(func.__doc__)
        return func(*args,**kwargs)
    return wrapper






@dec
def add(x,y):
    '''This Function takes two parameters as arguments and add their sum'''
    return x+y

print(add(2,5))