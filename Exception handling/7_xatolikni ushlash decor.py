import time
from typing import Callable
def decor(func):
    def wrap(*args, **kwargs):
        try:
            print("processing...")
            time.sleep(2)
            func(*args,**kwargs)
            print("done!")
        except:
            print("Error!")
    return wrap

@decor
def f():
    print (1/0)
    
f()