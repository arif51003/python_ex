# l=[i for i in range(5,501)]
# print(l)

# s=[j for j in range(0,-101,-1)]
# print(s)

# g=[p for p in range(100,-101,-2)]
# print(g)


# n=input("Yoqtirgan mevam:")
# l=['olma','nok','behi','banan']
# if n in l:
#     print("bor")
# else:
#     print("yo'q")


# l=['olma','nok','behi','banan']
# l.append('uzum')
# l.insert(1,"mango")


# l=['arif','asror','salom','eshmat','world','for','clear']
# for i in l:
#     if 'a' in i:
#         print(i)


# l=[2,4,5,7,8,3,6]
# s=0
# for i in l:
#     s+=i
# print(s)


# l=[2,4,5,7,8,3,6]
# max=0
# for i in range(len(l)):
#     for j in  range(len(l)):
#         if l[i]>l[j]:
#             l[j]=l[i]
# print(l[j])


# l=['olma','banan','nok','behi','banan','banan']
# cnt=0
# for i in l:
#     if i=='banan':
#         cnt+=1
# print(cnt)



# print([i**2 for i in range(1,11)])


# words=['salom',"video","hi","hello","men"]
# res=[word for word in words if len(word)<5]
# print(res)



# num=[2,5,3,5,1,6,7,8,3]
# f=[]
# for i in num:
#     if not i in f:
#         f.append(i)
# print(f)

st=["salom","hi","line","linux"]
s=" ".join(st)
print(s)