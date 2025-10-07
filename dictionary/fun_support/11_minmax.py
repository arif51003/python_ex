def minmax(x,y):
    if x>y:
        x,y=y,x
    return x,y
a=int(input())
b=int(input())
c=int(input())
d=int(input())
f=minmax(a,b)
g=minmax(c,d)
p=minmax(f[1],g[1])
print(p[1])
