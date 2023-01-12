import math

class shape:
    
    def __init__(self, length, width, radius):
        self.length = length
        self.width = width
        self.radius = radius

class rectangle(shape):
    
    def area(self):
        area = self.length * self.width
        return area

class square(shape):
     def area(self):
        area = self.length * self.length
        return area

class circle(shape):
    def area(self):
        return self.radius*self.radius * math.pi

rect_area = rectangle(2, 3, 4)
square_area = square(2, 3, 4)
circle_area = circle(2, 3, 4)

print(square_area.area)