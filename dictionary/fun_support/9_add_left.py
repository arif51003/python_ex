def add_left(n,k):
    a=len(str(n))
    n=n+k*10**a
    return n
b=int(input())
l=int(input())

print(add_left(b,l))