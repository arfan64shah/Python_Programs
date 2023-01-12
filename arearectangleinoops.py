class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.width * self.length
        return area
rect_area = rectangle(4, 5)

print("The area of the Rectangle is ",rect_area.area())