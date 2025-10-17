a=5
b=2
try :
    print((lambda x,y:x/y)(a,b))
except ZeroDivisionError as e:
    print(e)