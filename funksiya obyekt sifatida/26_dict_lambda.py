def qimmati(dic:dict):
    return dict(map(lambda x:int(x[1])>1000,dic))

d={
    "olma":200,
    "nok":500,
    "limon":1000,
    "avokado":2000,
    "mango":1700
}
print(qimmati(d))