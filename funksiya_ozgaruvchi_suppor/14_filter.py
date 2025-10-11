from typing import Callable

def func(a:list):
    for i in a:
        if i%2!=0:
            a.remove(i)
    return a
def filter_even(even:Callable, numbers:list):
    return even(numbers)

print(filter_even(func,[2,3,4,5,6]))