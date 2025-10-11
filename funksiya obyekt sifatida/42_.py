from typing import Callable

def applay(func,n):
    res=n
    for fun in func:
        res=fun(res)
        
    return res

f1=lambda x:x**2
f2=lambda x:x*3
print(applay([f1,f2],5))