class Battery:
    def __init__(self,presentage):
            self.history=[]
            self.presentage=presentage
            if presentage>100:
                self.presentage=100
            elif presentage<0:
                self.presentage=0
                print("telefon o'chdi")
                
    
    def charger(self,min,num):
        if num <0:
            return
        self.presentage+=min*num
        
        if self.presentage>100:
            self.presentage=100
        self.history.append(f"{min} minut {num}% dan zaryad")
            
    def play(self,min,num):
        self.presentage=(self.presentage)-min*num
        if self.presentage<0:
            self.presentage=0
            
        self.history.append(f"{min} minut o'ynaldi {min*num} zaryad sarflandi ")
b=Battery(60)
b.charger(3,7)
b.play(5,3)
print(b.history)
print(b.presentage)