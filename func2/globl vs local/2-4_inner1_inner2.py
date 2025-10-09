def outer():
    x='outer'
    def inner1():
        nonlocal x
        x="inner1"
        print(x)
    inner1()
    def inner2():
        nonlocal x
        x="inner2"
        print(x)
    inner2()
    
outer()