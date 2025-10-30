class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return f"{self.name} {self.age} yoshda"
    def __repr__(self):
        return f"{self.name} {self.age} yoshda"
    
per=Person("Arif",22)
per2=Person("Asror",19)

