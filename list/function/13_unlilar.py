def unlilar(word:str):
    k=0
    l=['a','e','i','o','u']
    for i in range(len(word)):
        if word[i] in l:
            k+=1
    return k
res=unlilar('assalomualekum')
print(res)