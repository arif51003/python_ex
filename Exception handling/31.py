from typing import Callable

def safe_call(func):
    
    def wrap():
        try:
            func()
        except ZeroDivisionError:
            print("division 0 by not allow")
        except Exception as e:
            raise Exception(e)
    return wrap
    
    
@safe_call
def myfunc():
    import random
    l=[ValueError,ZeroDivisionError,IndexError,TypeError]
    i=random.randint(0,3)
    raise l[i]

myfunc()