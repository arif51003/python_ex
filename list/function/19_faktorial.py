def faktorial(x:int):
    k=1
    for i in range(1,x+1):
        k*=i
    return k
print(faktorial(5))