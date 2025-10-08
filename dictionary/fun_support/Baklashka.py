def baklashka(n):
    k=0
    s=0
    while n>0:
        k+=n
        yn=(n+s)//3
        s=(n+s)%3
        n=yn
    return k
print(baklashka(10))
        