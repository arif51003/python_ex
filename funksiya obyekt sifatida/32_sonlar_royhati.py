lst=[2,4,6,7,8,9]
b=list(map(lambda x:"even" if x%2==0 else "odd",lst))
print(b)