def get_prime(*args):
    
        for i in range (*args):
            for j in range(2,int((args)**0.5)):
                if i%j!=0:
                    return True
            
            
class Prime:
    def __init__(self,*args):
        self.args=args
        
    def get_pr(self):
        l=[]
        if get_prime(self.args):
            l.append(self.args)
        return l
    
    
                                            