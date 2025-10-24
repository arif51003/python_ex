with open("text1.txt","r+") as m, open("myfile1.txt","w+") as l:
    a=m.read()
    l.write(a)
    