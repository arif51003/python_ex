f,g=open("text.txt","a+"),open("files/file1.txt","a+")
file3=open("files/f1.txt","a+")
a=f.read()
b=g.read()

file3.write(a+b)

f.close()
g.close()
file3.close()
