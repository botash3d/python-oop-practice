import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def distance_to_point2(self,other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

point_1 = Point(0,0)
point_2 = Point(3,4)
print(point_1.distance_to_point2(point_2))