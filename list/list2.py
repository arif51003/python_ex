n=int(input("n="))
l=[]
l2=[]
k=0
while n>=1:
    k=n%10
    l.append(k)
    n=n//10
for i in range(len(l)):
    l[i]=l[i]*pow(10,i)
    if l[i]!=0:
        l2.append(l[i])

print(l2[::-1])


# n=int(input("n="))
# l=[]
# k=0
# p=0
# while n>=1:
#     k=n%10
#     if k!=0:
#      l.append(k*10**p)
#     else:
#        p+=1 
#     n=n//10
# for i in range(len(l)):   
#      l[i]=l[i]*pow(10,i)


# print(l[::-1])


s=input()

dic=dict()
for i in s:
    if i in dic:
        dic[i]+=1
    else :
        dic[i]=1
print(dic)
