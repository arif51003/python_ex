from typing import Callable

def decor(func):
    
    def wrap(*args, **kwargs):
        ret=func(*args, **kwargs)
        print(ret.upper())
        
    return wrap

@decor
def say(s):
    return "Hi "+s

say('eshmat')