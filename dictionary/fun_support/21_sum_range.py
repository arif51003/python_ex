def sumrange(a,b):
    k=0
    if a>b:
        return 0
    for i in range(a+1,b):
        k+=i
    return k
print(sumrange(1,7))