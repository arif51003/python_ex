import os

print(os.getcwd())

os.chdir("./files")
for i in os.listdir():
    os.rename(i,f"{i.split('.')[0]}.bak")