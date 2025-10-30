import webcolor
import random

class Color:
    def __init__(self,red,blue,green):
        self.red=red
        self.blue=blue
        self.green=green
        
    @classmethod    
    def rand_color(cls):
        red=random.randint(0,255)
        green=random.randint(0,255)
        blue=random.randint(0,255)
        
        return cls(red,green,blue)
    
    def __str__(self):
        return f"({self.red, self.green, self.blue})"
    
    
r1=Color.rand_color()

print(type(r1))