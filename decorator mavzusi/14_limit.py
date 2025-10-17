from typing import Callable
c=0
def decor(func:Callable):
    
    def wrap():
        global c
        c+=1
        if c<4:
            func()
        else:
            return print("error")
    return wrap
        
@decor
def prnt():
    print("hello")
    
    
prnt()
prnt()
prnt()
prnt()
prnt()
prnt()
prnt()