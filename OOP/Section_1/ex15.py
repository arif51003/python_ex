class Aniqlovchi:
    def triangle(a,b,c):
        if a+b>c or a+c>b or b+c>a:
            return True
        return False
    
print(Aniqlovchi.triangle(3,4,5))