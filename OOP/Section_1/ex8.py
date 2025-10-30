class Game:
    def __init__(self,level,players,eleksir,gold,gem):
        
        self.level=level
        self.eleksir=eleksir
        self.players=players
        self.gold=gold
        self.gem=gem
        
    @classmethod 
    def sbros(cls,n=1,p=5,e=60,g=60,ge=5):
        return cls(n,p,e,g,ge)
    def __str__(self):
        return f"Level {self.level} player:{self.players} eleksir:{self.eleksir} gold:{self.gold} gem:{self.gem}"

play=Game.sbros()
    
    
print(play)