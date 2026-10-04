class Circle:
    PI = 3.14159

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return self.PI*self.radius**2

    def circumference(self):
        return 2*self.PI*self.radius

circle1 = Circle(10.5)
print(circle1.area())
print(circle1.circumference())
Circle.PI=3
#since value of pi changed , circumeference and radius also changed
print(circle1.area())
print(circle1.circumference())
