from typing import Callable

def decor1(n:callable):
    
    def decor2(func):
        
        def wrap(*args, **kwargs):
            if n(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                print("skipped")
        return wrap
    
    return decor2

@decor1(lambda x,y:x>y)
def add (a,b):
    return a+b

print(add(2,4))