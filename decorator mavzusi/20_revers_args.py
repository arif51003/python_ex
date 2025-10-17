from typing import Callable

def decor(func):
    def wrap(*args):
        for i in range(len(args)-1,-1,-1):
            func(args[i])
    return wrap
@decor
def f(*args):
    print(args)
    
f(1,2,3,'salom')