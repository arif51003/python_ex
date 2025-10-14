from typing import Callable

def decor(func):
    
    def wrap(*args, **kwargs):
        l=[]
        for i in args[0]:
            if not i in l:
                l.append(i)
        func(l)
    return wrap
@decor
def lst(ls:list):
    print(max(ls))
    
lst([2,2,5,5,3])