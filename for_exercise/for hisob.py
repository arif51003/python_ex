n=int(input('n='))
s=0
k=0
for i in range(1,(n+1)//2):
    s+=i
    k+=(i+1)
print(s+k)