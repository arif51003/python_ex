from typing import Callable

def decor(func):
    def wrap(*args, **kwargs):
        for i in args:
            print(type(i))
        return func(*args, **kwargs)
    return wrap
    
@decor   
def s(a):
    return a

s(5,3,'s',t=3)