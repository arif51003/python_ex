f=open("text.txt","r+")
a=f.read()
print(a.count("\n")+1)
f.close()