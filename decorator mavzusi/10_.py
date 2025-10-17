from typing import Callable

def decor(func):
    
    def wrap():
        if func() is None:
            return "no result"
        
        return func()
    
    return wrap

@decor
def s():
    return

s()