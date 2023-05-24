import time

def fathers(func):
    def gg(*args, **kargs):
        print('sdsds')
        f=func(*args,**kargs)
        return f
    return gg
@fathers
def add(a,b):
    return  a+b
# def time_calc(func):
#     def wrapper(*args, **kargs):
#         start_time = time.time()
#         f = func(*args,**kargs)
#         exec_time = time.time() - start_time
#         return f
#     return wrapper
add(3,2)