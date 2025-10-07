def kopaytma(*args):
    k=1
    for i in args:
        k*=i
    return k
print(kopaytma(2,4,5))