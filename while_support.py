# char=input('char=')
# n=int(input("jump="))
# a=chr(ord(char)+n)
# if (65-ord(char))<n or ((97-ord(char))<n) :
#     a=chr(ord(char)-(26-n))
# print(a)

a=int(input('a='))
y=0
s=0
while a>0:
    y=a%10
    s+=y
    a=a//10
print(s)