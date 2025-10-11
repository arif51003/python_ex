from typing import Callable
p=lambda x:x%4==0
def count_true(fun,l):
    count=0
    for i in range(len(l)):
        
        if fun(l[i]) is True:
            count+=1
    return count
f=[4,2,3,8,2,12,31,16]
print(count_true(p,f))