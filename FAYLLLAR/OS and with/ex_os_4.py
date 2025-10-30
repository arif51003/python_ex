from pathlib import Path
import os
import shutil
# file="practice_file"
# if not os.path.exists(file):
#     os.mkdir(file)
# os.chdir(file)
# open("myfile.txt","w").close()
    
# print(os.path.exists("myfile.txt"))

# os.chdir("..")
# try:
#     os.rename("practice_dir","test_dir")
# except FileNotFoundError:
#     print("bunday directory mavjud emas")


# print(os.getcwd())
# # os.remove("text.txt")
# os.chdir(".")
# print(os.getcwd())
# try:
#     os.rmdir("test_dir")
#     print("directory o'chirildi")
# except FileNotFoundError:
#     print("Mavjud emas")



# print(os.name)

# print(os.getcwd())
# try:

#     os.path.join("/home/arif-03/Python_projects/python_ex/text1.txt")
#     print("Path qo'shildi")
# except FileNotFoundError:
#     print("mavjud emas")
# 32
# print(Path.home())
# 31
print(Path.cwd())
# 33

print(Path("example.txt").exists())

# 34

Path.mkdir("temp_data")
os.chdir("temp_data")
Path