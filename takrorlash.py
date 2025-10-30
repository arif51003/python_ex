## funksiyani argumentlari bilan birga chiqaruvchi decorator

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Argumentlar:", args, kwargs)
#         return func(*args, **kwargs)
#     return wrapper

# def qosh(a, b):
#     return a + b

# qosh=decorator(qosh)

# print(qosh(3, 5))




## funksiyani n marta ishlatuvchi decorator


# def takrorla(n):
#     def decor(func):
        
#         def wrap(*args, **kwargs):
            
#             for _ in range(n):
#                 func()
#         return wrap
#     return decor

# @takrorla(4)
# def prin_t():
#     print("Salom!!!")

# prin_t()



# from functools import wraps

# def info(func):
#     # @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"{func.__name__} chaqirildi")
#         return func(*args, **kwargs)
#     return wrapper

# @info
# def salom():
#     print("Salom!")

# print(salom.__name__)
# salom()



# def A(func):
#     def wrapper():
#         print("A boshi")
#         func()
#         print("A oxiri")
#     return wrapper

# def B(func):
#     def wrapper():
#         print("B boshi")
#         func()
#         print("B oxiri")
#     return wrapper

# # @A
# # @B
# def test():
#     print("Funktsiya bajarilmoqda")

# test=B(test)
# test=A(test)
# test()



# def decor (func):
    
#     def wrap():
#         res=func()
#         return res*2
#     return wrap

# @decor

# def myfunc():
#     return 

# print(myfunc(5))





# def decor(func):
    
#     def wrap(*args):
#         print(f"{func.__name__} chaqirildi")

#         return (func(*args))
#     return wrap

# @decor
# def add(a,b):
#     return a+b

# print(add(4,6))


# def decor(func):
#     l=[]
#     def wrap(*args):
#         nonlocal l
#         for i in args:
#             if i>0:
#                 l.append(i)
#         func(l)
#         return
#     return wrap 

# @decor
# def myfunc(*args):
#     return 

# print(myfunc(5,-3,9))


import os 
from pathlib import Path

print(os.getcwd())