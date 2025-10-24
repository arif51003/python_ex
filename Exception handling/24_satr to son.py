l=list(map(str,input().split()))
lst=[]
for i in range(0,len(l)):
    try:
        lst.append(int(l[i]))
    except ValueError:
        print(f"{l[i]}ni songa aylantirib bolmadi")
        continue
print(lst)