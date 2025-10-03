# import random
# n=int(input("n="))
# l=[random.randint(1,100) for i in range(n)]
# print(l)
# k=l[0]
# p=l[0]
# for j in l:
#     if k>j:
#         k=j
#     if p<j:
#         p=j 

# print(k,p)    


# n=int(input("n="))
# num=list(map(int, input().split()))

# mx=max(num)
# mn=min(num)

# for i in range(len(num)):
#     if num[i]==mx:
#         j=i
    
#     if num[i]==mn:
#         j=i
# print(j)


# num=list(map(int, input().split()))
# b=int(input("b="))
# c=int(input("c="))
# mx=0
# for i in num:
#     if b<i and i<c and i>mx:
#         mx=i
# print(mx)



# n=int(input("n="))
# num=list(map(int, input().split()))
# mn=0
# mn2=0
# for i in range(len(num)):
#     if num[i]<mn:
#         mn=num[i]
# print(mn)

# for j in range(len(num)):
#         if num[j]<mn2 and num[i]!=num[j] or i!=j:
#             mn2=num[j]

# print(mn2)


# n=int(input("n="))
# num=list(map(int, input().split()))
# num.sort()
# print(num[0],num[1])


# m1=int(input("m="))
# m2=int(input("m="))
# m3=int(input("m="))



# s=input()

# frec=dict()
# k=0
# for i in s:
#     if i in frec:
#         frec[i]+=1
#     else:
#         frec[i]=1
# num="0"
# ch=0
# for key , val in frec.items():
#     if val>ch:
#         num=key
#         ch=val

# print(num)
target=int(input("n="))
l1=list(map(int , input().split()))
for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i]+l1[j]==target and i!=j :
            print(l1[i],l1[j])
            