def positiv(l:list)->list:
    
    for i in l:
        if i<0:
            l.remove(i)
    return l
print(positiv([-1,3,5,-2,8,-3]))