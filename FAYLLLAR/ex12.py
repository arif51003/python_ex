f=open("text.txt","r+")
g=open("text1.txt","a")
a=f.readlines()
f.close()
for l in a:
    l=l[:-1]
    g.write(l[::-1]+'\n')
    
    
    # g.write(a[i][::-1])
    
g.close()