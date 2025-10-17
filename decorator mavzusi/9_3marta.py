from typing import Callable

def decor(func):
    
    def wrap():
        
        for i in range(3):
            func()
    return wrap
    
@decor
def say():
    print('hello')
    
say()