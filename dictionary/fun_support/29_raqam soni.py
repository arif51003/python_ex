def count(a):
    k=0
    while a>0:
        k+=1
        a=a//10
    return k
print(count(213))