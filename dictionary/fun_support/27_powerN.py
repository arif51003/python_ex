def is_powerN(k,n):
    for i in range(0,k):
        if k==n**i:
            return True
    return False
print(is_powerN(32,3))