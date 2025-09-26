n=int(input("n="))
s=0
k=0
while True:
    k+=1
    s+=k
    if s>=n:
        print(k)
        break