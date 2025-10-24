def ind_elem(lst,i):
    try:
        print(lst[i])
    except IndexError:
        print(None)
ind_elem([1,3,5],4)