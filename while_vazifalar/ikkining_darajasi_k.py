n=int(input("n="))
k=0
s=4
while s<=n:
    k+=1
    s*=4
if n==4**k:
    print(k)
else:
    print("-1")