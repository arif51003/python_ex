# import os
# print(os.getcwd())
try:
    
    a=open("text.txt","r")
    print(a.read())
except OSError:
    print("faylda hatolik")

a.close()