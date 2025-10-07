def kvadrat_tenglama(a,b,c):
    d=b**2-4*a*c
    if d >0:
        return 2
    if d<0:
        return 0
    if d==0:
        return 1
    
print(kvadrat_tenglama(2,-5,3))