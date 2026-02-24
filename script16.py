
class Rectangle:
    count = 1
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath

    def calculate_area(self):
        area = self.length * self.breath
        return area


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        area = self.base * self.height
        return area


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = self.radius * 3.14
        return area

def print_area(shape):
    return shape.calculate_area()


print(print_area(shape = Rectangle(5, 10)))
c1 = Rectangle(10, 20)
Rectangle.count = 10
print(Rectangle.count)
print(c1.count)
