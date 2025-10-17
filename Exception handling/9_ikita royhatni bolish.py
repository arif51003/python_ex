a=[13,76,98,23,7]
b=[2,5,0,9]
c=[]
lenmx=max(len(a),len(b))
for i in range(0,lenmx):
    try:
        c.append(int(a[i]/b[i]))
    except ZeroDivisionError:
        print("nolga bolib bolmadi")
        continue

    except IndexError:
        print("royhat uzunligi mos emas")
        break

print(c)