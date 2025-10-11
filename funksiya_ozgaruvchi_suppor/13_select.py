from typing import Callable
def sq_qu_du(name:Callable):
    if name=="squer":
        return lambda s:s**2
    if name=="cube":
        return lambda s:s**3
    if name=="duble":
        return lambda s:s*2
    
aml=input()
a=int(input())
func=sq_qu_du(aml)
print(func(a))