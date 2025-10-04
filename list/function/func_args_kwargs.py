"""
args- position arguments
kwargs- keywords arguments
"""

def f(*args,**kwargs):
    return args, kwargs
print(f(1,3,5))