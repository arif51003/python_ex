class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    @classmethod
    def newborn(cls,name):
        return cls(name,age=0 )
    
    
    def __str__(self):
        return f"{self.name} {self.age}"
    
    

a=Person.newborn("Asror")
print(a)