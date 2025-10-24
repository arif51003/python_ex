f=open("text.txt","r+")
r=f.readline()
g=open("text1.txt","r+")
f.close()
a=input()
for i in range(len(r)):
    if a in r[i]:
        g.write(r[i])
        
g.close()
