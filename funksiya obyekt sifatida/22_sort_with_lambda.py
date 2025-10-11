def sort_by_age(lst:list):
    return sorted(lst,key=lambda x: x[1])
a=[('Arif',23),("asror",19)]
print(sort_by_age(a))