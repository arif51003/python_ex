class Product:
    def __init__(self,name,narx,soni):
        self.name=name
        self.narx=narx
        self.soni=soni
        self.tarix=[]
    def add(self,amount):
        self.soni+=amount
        self.tarix.append(f"{amount} ta qoshildi")
    def cell(self,amount):
        self.soni-=amount
        if amount>self.soni:
            self.soni=0
            
            self.tarix(f"sotib bolmaydi")
        
        else:
            self.tarix(f"{amount} ta sotildi {self.soni} ta qoldi")
    def __str__(self):
        return f"{self.name} soni:{self.soni}"
papka=Product(
    "sumka",25,9
)


print(papka)

papka.cell(4)
print(papka)



       