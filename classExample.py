class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distance(self,other):
        final_x = (self.x - other.x)**2
        final_y = (self.y - other.y)**2
        return (final_x-final_y)*0.5
    
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    
c = Coordinate(5,3)
origin = Coordinate(0,0)

print(c.distance(origin))
print("----")
print(Coordinate.distance(c,origin))
print("----")
print(origin)
print("----")
print(c)