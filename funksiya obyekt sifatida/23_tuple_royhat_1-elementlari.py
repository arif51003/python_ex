def first_elem_tup(lst:list)->list:
    return list(map(lambda x:x[0],lst))
a=[('Arif',23),("Asror",19)]
print(first_elem_tup(a))