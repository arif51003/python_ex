def max_three(a:int,b:int,c :int):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c
res=max_three(3,4,6)
print(res)
    