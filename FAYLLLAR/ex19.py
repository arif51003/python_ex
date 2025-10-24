import sys
f=open("text.txt")
a=f.read()
print(sys.getsizeof(f))

print(len((a).encode("utf-8")))