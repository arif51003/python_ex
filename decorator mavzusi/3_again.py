from typing import Callable

def decor(func):
    def wrap(s):
        
        res=func(s)
        print(res.upper)
        
    return wrap
@decor
def strin(s):
    print(s)
    
strin("arif")