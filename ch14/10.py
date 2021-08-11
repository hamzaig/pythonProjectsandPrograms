from functools import wraps
def only_input(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if all([type(arg)==int for arg in args]):
            return func(*args,**kwargs)
        else:
            print("invalid")

        # data_type=[]
        # for arg in args:
        #     data_type.append(type(arg)==int)
        # if all(data_type):
        #     return func(*args,**kwargs)
        # else:
        #     print("Invalid Datatype") 
    return wrapper
@only_input
def add_all(*args):
    total = 0
    for i in args:
        total+=i
    return total
print(add_all(1,2,3,4))