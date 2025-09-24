# x1=int(input('x1='))
# y1=int(input('y1='))
# x2=int(input('x2='))
# y2=int(input('y2='))

# res=abs(x1-x2)==2 and (y1-y2)==1 or abs(x1-x2)==1 and abs(y1-y2)==2
# print(res)


x1=int(input('x1='))
y1=int(input('y1='))
x2=int(input('x2='))
y2=int(input('y2='))

ox=abs(x1-x2)
oy=abs(y1-y2)
nuqta= (ox == oy) or (x1==x2) or (y1==y2) and (abs(x1-x2)==1) and (abs(y1-y2)==1)
print(nuqta)
