class Cicle:
    def __init__(self,radius):
        self.radius=radius
    
    @classmethod
    def diametr(cls,diametr):
        return Cicle(radius=diametr/2)
    def __str__(self):
        return f"{self.radius}"
    
    @staticmethod
    def juft(n):
        return n % 2==0
    
c1=Cicle.diametr(5)

print(Cicle.juft(4))
