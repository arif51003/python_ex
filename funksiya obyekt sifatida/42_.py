# from typing import Callable

# def applay(func,n):
#     res=n
#     for fun in func:
#         res=fun(res)
        
#     return res

# f1=lambda x:x**2
# f2=lambda x:x*3
# print(applay([f1,f2],5))
# n=int(input())
# l=list(map(int,input().split()))
# mx=max(l)
# l.remove(mx)
# print(max(l))

# a,b,c=map(int,input().split())
# if a % 2==1 :
#   a=a+1
# if b%2==1:
#   b=b+1
# if c%2==1:
#   c=c+1
# print(int((c/2)+(a/2)+(b/2)))

# n=int(input())
# s=0
# k=0
# while n>0:
#   s+=n%10
#   n=n//10
# print(s)
  
  
# n=int(input())
# l=list(map(int,input().split()))
# for i in l:
#     if l.count(i)==1:
#         print(i,end=' ')
 
 
# n=int(input())
# for i in range(n+1):
#   if i+(i%100)==n:
#     print(i)

s=input()
s1=s[::-1]
s1=s1.replace('hs','sh')
s1=s1.replace('hc','ch')
s1=s1.replace('gn','ng')
print(s1)
