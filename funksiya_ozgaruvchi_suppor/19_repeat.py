from typing import Callable

def repeat(fun,n):
    def inner():
        
        for _ in range(n):
                fun()
        return "Sucsess"
    return inner()

print(repeat(lambda :print("Hello!"),5))