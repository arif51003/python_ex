from typing import Callable

def filter_sort(lst:list)->list:
    return sorted(lst,key=lambda x:len(x))


a=['muhammadali','arif','asror']
print(filter_sort(a))
