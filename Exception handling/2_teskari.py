def teskari_qiymat(lst):
    k=[]
    for i in range(0,len(lst)):
        try:
            k.append(lst[i]**(-1))
        except ZeroDivisionError:
            print(f"ro'yhatda {i}-element no'lga teng royhatdan olib tashlayman")
            
    return k

print(teskari_qiymat([3,6,0,5,0,4]))