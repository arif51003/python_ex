from typing import Callable

def decor(func):
    
    def wrap(s):
        
        if s=='':
            print('bosh string')
            return
        func(s)
        
    return wrap
@decor
def strin(s):
    print(s)
    
strin('')