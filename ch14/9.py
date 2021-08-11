from functools import wraps
import time

def dec(func):
    @wraps(func)
    def wrapper(*args,**kwrags):
        print(f"Executing .... {func.__name__}")
        t1=time.time()
        return_val=func(*args,**kwrags)
        t2=time.time()
        total_time=t2-t1
        print(total_time)
        return return_val
    return wrapper
@dec
def squ(n):
    return [i**2 for i in range(1,n+1)]

(squ(1000))