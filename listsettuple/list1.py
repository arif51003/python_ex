# # 1
# l=map(str,input("Mevalar:").split())
# k=list(l)
# print(k)


# # 2
# l=[i for  i in range(1,11)]
# print(l)


# # 3
# my_shopping_card=[]


# # 4
# l=[2,1,3,4,7,8,5]
# print(l[2])


# # 5
# l=[2,3,4,5,6,7,8]

# k=l[::-1][0]
# print(k)


# # 6
# k=l[:3]
# print(k)



# # 7
# k=l[4:8]
# print(k)



# # 8
# l=['olma','nok','limon','qulupnay','malina']
# m=input("meva:")
# if m in l:
#     print(f"{m} mening sevimli mevalaim ichida bor")
# else :
#     print("Yo'q")


# # 9
# l=['olma','nok','limon','qulupnay','malina']
# l.append('uzum')
# print(l)


# # 10
# l=['olma','nok','limon','qulupnay','malina']
# l.insert(1,'mango')
# print(l)


# # 11
# l=['olma','nok','limon','qulupnay','malina']
# l[0]='kivi'
# print(l)


# # 12
# l=['olma','nok','limon','qulupnay','malina']

# l.pop(len(l)-1)

# print(l)


# # 13
# l.remove('olma')
# print(l)



# # 14
# l.clear()
# print(l)


# # 15
# ism=['Arif','Asror','Muhammadali','Javoxir']
# yosh=[22,19,19,19]
# ism.extend(yosh)
# print(ism)



# # 16
# l=['olma','nok','limon','qulupnay','malina']
# b=l.copy()
# b[0]=25
# print(l,b,sep="\n")



# # 17

# l=['olma','nok','limon','qulupnay','malina']
# for i in range(len(l)):
#     print(l[i])


# # 18

# l=[2,3,4,5,6,1,7,8]
# s=0
# l1=0
# while s<len(l):
#     l1=l[s]
#     s+=1
#     if l1<6:
#         print(l1)


# # 19

# s=['arif','asror','odil','sardor','komil','jaxon']
# for i in s:
#     if 'a' in i:
#         print(i)

# # 20

# num=[1,3,6,3,8,9,4,2,5,7,13,11,1,42,16]
# m=[]
# for i in range(len(num)):
    
#     if num[i]%2==0:
#         m.append(num[i])
# print(m)


# # 21

# num=[1,3,6,3,8,9,4,2,5,7,13,11,1,42,16]
# s=0
# for i in range(len(num)):
#     s+=num[i]
# print(s)


# # 22

# num=[1,3,6,3,8,9,4,2,5,7,13,11,1,42,16,5]
# max=0
# min=0
# for i in range(len(num)):
#     for j in range(len(num)):
#         if num[i]<num[j]:
#             num[i]=num[j]
# print(num[j])


# # 23

# meva=['olma','anor','banan','olcha','banan','gilos','banan']
# cnt=0
# for i in meva:
#     if i=='banan':
#         cnt+=1
# print(cnt)



