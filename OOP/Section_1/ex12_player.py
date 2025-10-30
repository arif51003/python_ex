class Player:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    
    def add_score(self,n):
        self.score+=n
        
    def __str__(self):
        return f"{self.name}  {self.score}"

player1=Player("Asror", 6)

print(player1)

player1.add_score(4)

print(player1)