class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color

class Cat:
    def __init__(self,name,color):
        self.name=name
        self.color=color

pet1=Dog("bobik","black")
pet2=Cat("gulcapcap","white")

print(isinstance(pet1,Dog))
