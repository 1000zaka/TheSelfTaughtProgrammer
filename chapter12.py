"""
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())
"""

# No.1
class Apple:
    def __init__(self, color, weight, taste, area):
        self.color = color
        self.weight = weight
        self.taste = taste
        self.area = area

# No.2
class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        import math
        return self.radius * self.radius * math.pi

circle = Circle(4)
print(circle.area())


# No.3
class Triangle:
    def __init__(self, b, h):
        self.bottom = b
        self.high = h

    def area(self):
         return self.bottom * self.high / 2
triangle = Triangle(10, 2)
print(triangle.area())

# No.4
class Hexagon:
    def __init__(self, a, b, c, d, e, f):
        self.side1 = a
        self.side2 = b
        self.side3 = c
        self.side4 = d
        self.side5 = e
        self.side6 = f

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6

hexagon = Hexagon(6, 6, 3, 3, 6, 6)
print(hexagon.calculate_perimeter())