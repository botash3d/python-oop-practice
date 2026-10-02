class Rectangle:
    def __init__(self,width:float,height:float):
        self.width=width
        self.height=height

    def rect_area(self):
        self.area=self.width*self.height
        return self.area

    def rect_perimeter(self):
        self.perimeter=2*(self.width+self.height)
        return self.perimeter

    def __str__(self):
        return f"Area of rect is: {self.rect_area():.2f} cm² \nPerimeter of rect is: {self.rect_perimeter():.2f} cm"

rect_1=Rectangle(10.5,12.7)
rect_2=Rectangle(12.8,19.6)
print(rect_1)
print(rect_2)