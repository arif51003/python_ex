person: dict={
    "Name":"Eshmat",
    "age":47,
    "city":"Samarqand"
}

# print(person.get("name"))

# person["occupation"]="pensiyada"

# person.update({"age":70})

# person["hobbies"]=["football","chess"]
# print(person)

# for k in person.keys():
#     print(k)

#########################
# num={i:i**2 for i in range(1,6)}

# print(num)

# frut=["olma","limon","banana"]
# dic={len(frut[i]):frut[i] for i in range(len(frut))}
# print(dic)





# list1=[2,4,6]
# list2=['makdab','universitet','kocha']
# dic={list1[i]:list2[i] for i in range(len(list1))}
# print(dic)



# dic1={4: 'olma', 5: 'limon', 6: 'banana'}
# dic2={2: 'makdab', 4: 'universitet', 7: 'kocha'}
# dic1.update(dic2)
# print(dic1)

# student={
#     "Eshmat":{
#         "math":45,
#         "sicence":63

#     },
#     "toshmat":{
#         "math":54,
#         "science":76
#     }
# }

# s=0
# for key, val in student.items():
#     s=0
#     for key1 , val1 in val.items():
#         s+=val1
#     print(key,s/len(val))



# s=input()

# frec=dict()
# k=0
# for i in s:
#     if i in frec:
#         frec[i]+=1
#     else:
#         frec[i]=1
# print(frec)

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

