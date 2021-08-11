def dec_fun(func):
    def wrapper():
        print("This is added")
        func()
    return wrapper
@dec_fun
def fun1():
    print("This is function 1")
@dec_fun
def fun2():
    print("This is function 2")
fun1()
fun2()

# var = dec_fun(fun1)
# var()

# fun1 = dec_fun(fun1)
# fun1()