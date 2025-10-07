def teskari(a:int)->int:
    a=str(a)
    b=a[::-1]
    return int(b)
l=int(input())
print(teskari(l))