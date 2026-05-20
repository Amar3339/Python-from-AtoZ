# write a decorators to measure time of a function takes to execute
import time
def timer(func):
    def wrapper(*args , **kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        print(f"{func.__name__},ran in {end-start} time ")
        return result
    return wrapper
@timer
def slepp(n):
    time.sleep(n)


slepp(2)
    