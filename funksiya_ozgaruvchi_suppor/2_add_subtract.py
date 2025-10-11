def add(x,y):
    return x+y

def subtract(x,y):
    return x-y
l=[add,subtract]
for i in l:
    print(i(5,2))