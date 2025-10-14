from typing import Callable

def decor(func):
    
    def wrap(a):
        if a<0:
            print("negativ")
            return
        func()
    return wrap

@decor
def r(b):
    print(b)
    
r(-2)