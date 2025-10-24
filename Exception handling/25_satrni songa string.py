s=input()
l=s.split()
l2=[]
for i in l:
    try:
        l2.append(int(i))
    except ValueError:
        print(f"{i} sozini o'grish imkonsiz")
        # continue
print(l2)