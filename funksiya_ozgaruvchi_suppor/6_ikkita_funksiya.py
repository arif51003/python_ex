from typing import Callable
def n_daraja_k(n,k):
    return pow(n,k)

def opr(a,b,func:Callable):
    return func(a,b)

print(opr(3,5,lambda a,b:pow(a,b)))