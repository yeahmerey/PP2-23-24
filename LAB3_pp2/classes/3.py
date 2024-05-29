class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = int(length)
        self.width = int(width)

    def area(self):
        print(self.width * self.length)


rect1 = Rectangle(input(), input())
print(rect1.length, rect1.width)
rect1.area()