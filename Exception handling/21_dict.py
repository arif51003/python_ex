def f(d:dict,key:str,value):
    try:
        if not isinstance(d,dict):
          raise TypeError("dict emas")

        d[key]=value
        return d        
        
    except TypeError:
        
        print("argument hato")

print(f([3,4,5],"arif",2))

