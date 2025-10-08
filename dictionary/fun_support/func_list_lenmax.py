def getmax(lst:list[str])->str:
    s=lst[0]
    for i in lst:
        if len(i)>len(s):
            s=i
    return s
print(getmax(['arfi','asror']))