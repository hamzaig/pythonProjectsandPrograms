def adds(a,b):
    if ((type(a) is int) and (type(b) is int)):
        return a+b
    raise TypeError("Please Enter Integer")

print(adds(2+2,"2"))