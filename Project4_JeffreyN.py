# Authors: Jeffrey Ni 
# Assignment: Project #4
# Completed (or last revision):  05/08/2023

# Task 1
class Pair:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<{self.x}, {self.y}>"

    def __add__(self, other):
        return Pair(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Pair(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Pair(self.x * self.y - other.x * other.y, self.x * other.x - self.y * other.y)


def main():
    p1 = Pair(3, 2)
    p2 = Pair(1, 5)
    p3 = Pair(4, 3)

    result1 = p1 + p2
    result2 = p1 * p2
    result3 = p1 / p2
    result4 = p1 + p2 * p3
    result5 = p1 * p2 / p3 + p1

    print("p1=", p1)
    print("p2=", p2)
    print("p3=", p3)
    print("p1 + p2=", result1)
    print("p1 * p2=", result2)
    print("p1 / p2=", result3)
    print("p1 + p2 * p3=", result4)
    print("p1 * p2 / p3 + p1=", result5)

    p1 = Pair(1, 3)
    p2 = Pair(2, 5)
    p3 = Pair(7, 2)

    result1 = p1 + p2
    result2 = p1 * p2
    result3 = p1 / p2
    result4 = p1 + p2 * p3
    result5 = p1 * p2 / p3 + p1

    print("p1=", p1)
    print("p2=", p2)
    print("p3=", p3)
    print("p1 + p2=", result1)
    print("p1 * p2=", result2)
    print("p1 / p2=", result3)
    print("p1 + p2 * p3=", result4)
    print("p1 * p2 / p3 + p1=", result5)
    
if __name__ == '__main__':
    main()
'''
Results:
p1= <3, 2>
p2= <1, 5>
p3= <4, 3>
p1 + p2= <4, 7>
p1 * p2= <3, 10>
p1 / p2= <1, -7>
p1 + p2 * p3= <7, 17>
p1 * p2 / p3 + p1= <21, -16>
p1= <1, 3>
p2= <2, 5>
p3= <7, 2>
p1 + p2= <3, 8>
p1 * p2= <2, 15>
p1 / p2= <-7, -13>
p1 + p2 * p3= <15, 13>
p1 * p2 / p3 + p1= <17, -13>
'''

# Task 2
import turtle

class Polygon:
    def __init__(self):
        self.pointList = []

    def addPoint(self, point):
        self.pointList.append(point)

    def getPoint(self, index):
        return self.pointList[index]

    def displaySides(self):
        return len(self.pointList)

    def draw(self):
        turtle.penup()
        turtle.goto(self.pointList[0])
        turtle.pendown()
        for point in self.pointList[1:]:
            turtle.goto(point)
        turtle.goto(self.pointList[0])
        
class Rectangle(Polygon):
    def __init__(self, lowerleft, upperright):
        super().__init__()
        self.addPoint(lowerleft)
        self.addPoint((lowerleft[0], upperright[1]))
        self.addPoint(upperright)
        self.addPoint((upperright[0], lowerleft[1]))

    def getLowerLeft(self):
        return self.getPoint(0)

    def getUpperRight(self):
        return self.getPoint(2)
def main():
    pentagon = Polygon()
    pentagon.addPoint((0, 0))
    pentagon.addPoint((0, 100))
    pentagon.addPoint((100, 100))
    pentagon.addPoint((150, 50))
    pentagon.addPoint((100, 0))

    print("# of sides:", pentagon.displaySides())
    pentagon.draw()

    rectangle = Rectangle((200, 0), (400, 100))

    print("Lower left points:", rectangle.getLowerLeft())
    print("Upper right points:", rectangle.getUpperRight())
    print("# of sides:", rectangle.displaySides())

    turtle.penup()
    turtle.goto(350, 50)
    turtle.pendown()
    rectangle.draw()

    turtle.done()


if __name__ == '__main__':
    main()
'''
Results:
# of sides: 5
Lower left points: (200, 0)
Upper right points: (400, 100)
# of sides: 4
'''