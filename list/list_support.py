l=map(int,input().split())
n=int(input("n="))
k=list(l)
topildi=False
for i in (len(k)-1,-1,-1):
    if n==k[i]:
        print(i)
        topildi=True
        break
if not(topildi):
    print('-1')