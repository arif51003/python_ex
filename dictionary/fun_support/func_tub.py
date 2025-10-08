def is_prime(n:int)->bool:
    for i in range(2,int(n**0.5)+1):
        if  n%i==0:
            return False
    return True

def get_tub_son(lst:list)->list:
    l=[]
    for i in lst:
        if is_prime(i):
            l.append(i)
    return l
print(get_tub_son([3,7,10,69,41]))