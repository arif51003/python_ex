def sortabc(a,b,c):
    if a<b and b>c:
        b,c=c,b
    if b<a and b>c:
        a,c=c,a
    if c>a and c>b and a>b:
        a,b=b,a
    return a,b,c
a=int(input())
b=int(input())
c=int(input())
print(sortabc(a,b,c))
