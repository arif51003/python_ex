def doira2(r1,r2):
    s1=3.14*r1**2
    s2=3.14*r2**2
    if r1>r2:
        return s1-s2
    else:
        return s2-s1
print(doira2(2,3))