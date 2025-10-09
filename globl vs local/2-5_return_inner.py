def outer():
    x='out'
    def ret_inner():
        x='in'
        print(x)
    ret_inner()
outer()
    