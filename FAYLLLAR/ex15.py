f=open("text1.txt","r+")
s=(f.read()).split()
f.close()
d=dict()
for i in s:
    if  i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)