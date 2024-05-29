import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        return self.x, self.y

    def move(self, x1, y1):
        self.x += x1
        self.y += y1

    def dist(self, second):
        x2 = math.sqrt((second.x - self.x) * (second.x - self.x))
        y2 = math.sqrt((second.y - self.y) * (second.y - self.y))
        return x2, y2

    def printDistance(self, x):
        print(self.dist(x))
        
    
    def printShow(self):
        print(self.show())
    
first = Point(1, 2)
second = Point(3, 2)

first.printShow()
first.move(2, 2)
first.printShow()
first.printDistance(second)