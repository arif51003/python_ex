from typing import Callable

def decor(func):
    
    def wrap(*args):
        t=[]
        for i in args:
            if isinstance(i):
                t.append(i.lower())
            else:
                t.append(i)
            return func(*tuple(t))
            
    return wrap

@decor
def kv(*a):
    print(a)

kv('ariF')