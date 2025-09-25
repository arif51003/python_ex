n=int(input('n='))
k=int(input("k="))
i=0
while n>=k:
    i+=1
    n-=k
print(i,n)