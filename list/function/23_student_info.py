def student_info(name:str,age:int,**kwargs):
    dic=dict()
    dic.update(name,age)
    return dic
print(student_info('arif',22))