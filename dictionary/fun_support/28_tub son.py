def tub_son(n:float):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
print(tub_son(9))