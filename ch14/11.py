from functools import wraps

def data_type(dtype):
    def deco(func):
        def wrapper(*args,**kwargs):
            if all([type(i) == dtype for i in args]):
                return func(*args,**kwargs)
            else:
                print("invalid")
        return wrapper
    return deco

@data_type(str)
def String(*args):
    s=""
    for i in args:
        s+=i
    return s

print(String('hamza','ali',11))


                