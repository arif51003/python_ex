from typing import Callable

def decor(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        func()
        
    return wrapper
@decor
def f():
    print('hello')
    
f()