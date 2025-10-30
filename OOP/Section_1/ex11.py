class List:
    def __init__(self,l):
        self.l=l
    @staticmethod    
    def juftmi(n):
        if n%2==0:
            return True
        return False
    
    def tekshiir(self):
        for i in self.l:
            if i.juftmi():
                return True
