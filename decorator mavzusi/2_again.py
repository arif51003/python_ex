from typing import Callable

def decor(func:Callable):
    k=0
    def wrap():
        nonlocal k
        func()
        k+=1
        print(k)
    print(k)
    wrap()   
    
@decor
def fun():
    print("Hi!")
    
    
fun()
fun()