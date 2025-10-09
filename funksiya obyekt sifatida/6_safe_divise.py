from typing import Callable

def safe_devise(a,b):
    return a/b

def error():
    print("Error")


def run_if_safe(
    func:Callable,
    handler:Callable,
    a,b
):
    if (b!=0):
        func(a,b)
    else:
        handler()
        
print(run_if_safe(safe_devise,error,3,2))