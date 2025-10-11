def choose(con):
    if con:
        return lambda x:x+10
    return lambda x:x-10
func=choose(True)
print(func(4))