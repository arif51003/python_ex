class Bank:
    def __init__(self,name,hisob):
        self.name=name
        self.hisob=hisob
    def __str__(self):
        return f"{self.name}ning hisobi {self.hisob}$"
    
first=Bank("Arif",500)
second=Bank("Asror",200)
