from typing import Callable


def decor(func):

    
    def wrap(n):
        try:
            func()
            
        except:
            pass