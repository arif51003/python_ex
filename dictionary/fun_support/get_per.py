from mukammal import mukammal
def getnum(lst:list)->list:
    l=[]
    for i in lst:
        if mukammal(i):
            l.append(i)
    return l