def digit_count(n:int)->int:
    s=0
    k=0
    l=0
    while n>0:
            s=n%10
            k+=s
            l+=1
            n=n//10
    return k,l, print(f"Raqamlar yig'indisi:{k}\nRaqamlar soni:{l}")
                 
p=int(input())
digit_count(p)