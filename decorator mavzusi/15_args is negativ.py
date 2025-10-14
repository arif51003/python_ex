from typing import Callable

def decor(func):
    
    def wrap(*args, **kwargs):
        for n in args:
            if n<0:
                print("error")
                return
        func(*args)
    return wrap
