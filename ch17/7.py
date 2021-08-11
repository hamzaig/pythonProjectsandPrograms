def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        # print("You cannot divide a number by zero")
        print(err)
    except TypeError as err:
        print("number must be int or float")
    except:
        print("unexpected error")

print(divide(2,""))
