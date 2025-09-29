n=int(input('n='))
a=float(input("a="))
b=float(input("b="))
d=abs(a-b)
s=min(a,b)
r=d/n
for i in range(n-1):
    s+=r
    print(s,end=", ")

