def digitN(n,k):
    n=int(str(n)[::-1])
    s=0
    e=0
    while True:
        e=n%10
        n=n//10
        s+=1
        if s==k:
            return e
    
        
print(digitN(98768,3))