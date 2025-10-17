from typing import Callable

def decor(func):
    
    def wrap(*args):
        for i in args:
            if i % 2==0:
                func(i)
    return wrap

@decor
def kv(*args):
    print(args)

kv(2,3,4,5)