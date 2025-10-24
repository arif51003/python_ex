f=open("text1.txt","r+")
s=(f.read()).split()
k=s[0]
for i in range(0,len(s)):
    if len(s[i])>len(k):
        k=s[i]  
print(k)
f.close()
