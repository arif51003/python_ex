
from typing import Callable
p=[lambda x:x**2,lambda x:x*5]

def apply(fun,a)->list:
    return fun(a)
l=[]
for i in range(len(p)):
    l.append(apply(p[i],8))
print(l)