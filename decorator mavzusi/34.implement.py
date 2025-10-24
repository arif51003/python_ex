from typing import Callable

def call_logger(func):
    l=[]
    
    def wrap(*args):
        nonlocal l
        try:
            res=func(*args)
            l.append(
                {
                    "args":args,
                    "res": res
                }
            )
            return res
        except Exception as e:
            l.append(
                {
                    "args": args,
                    "res": e
                }
            )
    def get_history():
        return l
    
    wrap.history=get_history
    
    return wrap
    
@call_logger
def add(a,b):
    return a/b


print(add(3,5))
print(add(4,0))

print(add.history())