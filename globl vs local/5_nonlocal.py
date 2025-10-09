
def outer():
    x='outer'
    print(x)
    def inner():
        nonlocal x
        x="inner"
        print(x)
    inner()
    print(x)
    
outer()
