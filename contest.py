# n,m=map(int,input().split())
# s=1
# for i in range(n,m+1):
#   s*=i
# l=[]
# s=str(s)
# for j in reversed(s):
#     if j=="0":
#         l.append(j)
#     else:
#         break
# print(len(l))

n=int(input())
s=input()
l=''
for i in range(len(s)):
    if s[i].isalpha():
        if ord(s[i])>64 or 91>ord(s[i]):
            pass
            
            
k=int(input())
k=k%26
s=input()
l=""
for i in s:
    if i.isalpha():
       if (65<=(ord(i)+k)<=90 and 65<=ord(i)<=90) or( 97<=ord(i)+k<=122 and 97<=ord(i)<=122):
           l+=chr(ord(i)+k)
       else:
           l+=chr(ord(i)-26+k)
    else:
        l+=i 
               
print(l)