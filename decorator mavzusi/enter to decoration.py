from typing import Callable

def decor(func:Callable):
    k=0
    def inner(*args, **kwargs):
        nonlocal k
        print('Starting...')
        func(*args, **kwargs)
        k+=1
        print('Done')
    return inner
@decor
def l(a):
    print(a*2)

l(5)
l(6)