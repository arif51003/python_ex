class Meva:
    def __init__(self,nomi,rangi):
        
        self.nomi=nomi
        self.rangi=rangi
        
    @classmethod
    def get_list(cls,l:list):
        nomi,rangi=l
        return Meva(nomi,rangi)
    
    def __str__(self):
        return f"{self.nomi} {self.rangi}"
    
a=Meva.get_list(["olma","qizil"])

print(a)