def lst(l):
    for i in range(0,len(l)):
        try:
            l[i]=int(l[i])
        except ValueError:
            print("satr mavjud")
            return False
    return True
    

print(lst([3,6,8]))