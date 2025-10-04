def sum_all(*args):
    k=0
    for i in args:
        k+=i
    return k
print(sum_all(3,5,2))