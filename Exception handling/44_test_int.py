from typing import Callable

def validat_args(func):
    
    def wrap(*args):
         
        for arg in args:
             
                if not isinstance(arg,int):
                    raise TypeError(f'{arg} int emas')
        func(*args)
    return wrap

@validat_args
def sum_arg(*args):
    k=0
    for arg in args:
        k+=arg
        
    print(k)

sum_arg(3,5,6,"a") 