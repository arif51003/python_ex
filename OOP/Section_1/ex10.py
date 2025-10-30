class Student:
    def __init__(self,ismi,grade):
        
        self.ismi=ismi
        self.grade=grade
        
    @classmethod
    def get_dict(cls,l:dict):
        ismi,grade=l.values()
        return Student(ismi,grade)
    
    def __str__(self):
        return f"{self.ismi} {self.grade}"
    
a=Student.get_dict({"name":"Arif","grade":22})

print(a)