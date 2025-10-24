from typing import Callable

def convert_exeption(func):
    
    def wrap(*args):
        
        try:
            func()
        except KeyError as e:
            raise ValueError(e)
        
    return wrap

@convert_exeption
def myfunc():
    d=dict()
    print(d["l"])
    
myfunc()