try:
    a=int(input())
    b=int(input())
    print(a/b)
except ZeroDivisionError:
    print("nolga bolip bolmaydi")
except ValueError:
    print("son kiriting")