from typing import Callable

def sqr(a):
    return a**2

def apply(
    func:Callable,
    b:int
)->int:
    return func(b)

print(apply(lambda b:b**2,9))