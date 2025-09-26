
a=int(input("a="))
c=0
while 0<a:
    c=a%10
    a=a //10
    if c % 2==1:
        print("toq son bor")
        break