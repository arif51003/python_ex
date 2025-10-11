def filter_3and5(lst:list):
    return list(filter(lambda x:x%3==0 or x%5==0,lst))
a=[2,4,5,6,9,10,12,13]
print(filter_3and5(a))