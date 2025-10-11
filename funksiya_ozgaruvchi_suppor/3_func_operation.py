def add(a,b):
    return a+b
def sub (a,b):
    return a-b
def mul(a,b):
    return a*b

d={
    "add":add,
    "sub":sub,
    "mul":mul
}

while True:
    
    n=input("Amal kirit(add,sub,mul)")
    a=int(input())
    b=int(input())
    print(d[n](a,b))
    print("davom etasizmi ha/yo'q")
    m=input()
    if m=="yo'q":
        break