s=list(map(int,input().split()))
f=open("text1.txt","a")
for i in s:
    if i%2==0:
        f.write(str(i))
f.close()