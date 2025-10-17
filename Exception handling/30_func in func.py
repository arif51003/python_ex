from typing import Callable
def f1(func):
    def f2():
        try:
            func()
        except:
            print("funksiyada hatolik bor")
    f2()

def a():
    print(1/0)

f1(a)

