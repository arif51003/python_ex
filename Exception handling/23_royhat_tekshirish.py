def lst(l):
    for i in range(0,len(l)):
        try:
            if not isinstance(i,int):
                raise TypeError()
            l[i]=int(l[i])
        except ValueError:
            print("royhatda satr mavjud")
            
    

print(lst([3,6,8,'a']))