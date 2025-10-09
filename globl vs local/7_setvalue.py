a=7
def set_value():
    global a
    a=9
    print(a)
    def reset():
        global a
        a=a+6
    reset()
set_value()
print(a)