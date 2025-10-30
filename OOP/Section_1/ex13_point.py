import math 
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def distance(self,x1,y1):
        return math.sqrt(((self.x)-x1)**2+((self.y)-y1)**2)
point1=Point(3,5)

print(point1.distance(5,4))