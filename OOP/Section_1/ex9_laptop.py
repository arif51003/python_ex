class Laptop():
    def __init__(self,brand,ram,price):
        self.brand=brand
        self.ram=ram
        self.price=price
        
    def __str__(self):
        return f"{self.brand} {self.ram}GB "
    
l=Laptop(
    brand="Lenovo",
    ram=16,
    price=450
)


print(l)