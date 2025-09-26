a=int(input('a='))
b=int(input('b='))

kop=a*b
ekub=0

while True:
    if a==0 or b==0:
        ekub=a+b
        print(a+b)
        break
    if a>b:
        a=a%b
    else:
        b=b%a
    ekub=a+b
print(kop // ekub)