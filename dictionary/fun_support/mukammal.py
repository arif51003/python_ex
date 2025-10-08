def mukammal(n:int)->bool:
    k=0
    for i in range(1,n):
        if n%i==0:
            k+=i
    return k==n
print(mukammal(28))