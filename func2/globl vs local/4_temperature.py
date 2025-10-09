temp=[]
def add_temp(t:float,shkala:str):
    global temp
    temp.append([t,shkala])
add_temp(23,'C')
add_temp(34,"F")
print(temp)