class Area:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    @classmethod
    def squer(cls,a):
        return cls(a,a)
    
    def __str__(self):
        return f"{self.a*self.b}"     
    
a=Area.squer(5)
print(a)