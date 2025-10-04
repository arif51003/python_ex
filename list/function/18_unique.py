def unique_element(l:list)->list:
    l2=[]
    for i in l:
        if not i in l2:
            l2.append(i)
    return l2
print(unique_element([1,3,3,3,2,4,1,7]))        