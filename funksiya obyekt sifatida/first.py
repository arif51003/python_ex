def isEven(n:int)->bool:
    if not isinstance(n):
        return False
    return n%2==0
juftmi=isEven
print(juftmi(5))