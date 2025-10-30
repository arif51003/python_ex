class Book:
    def __init__(self,name,author):
        self.name=name
        self.author=author
        
    def __str__(self):
        return f"nomi:{self.name} autor:{self.author}"
    
    @classmethod
    def defult_create(cls):
        
        return Book("Unknown","Unknown")
    
book1=Book("Molxona","Jorj Oruel")

print(book1.defult_create())