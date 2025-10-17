import  time
from typing import Callable
def decor(func):
    def wrap():
        print("Starting...")
        time.sleep(2)
        func()
        print("Done!")
    wrap()
    
@decor
def fun():
    print("processing")
    
fun()