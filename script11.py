# class Car:
#     def __init__(self, color = 'white', speed = 0):
#         self.color = color
#         self.speed = speed
#
# c1 = Car()
# print(c1.color, c1.speed)
# c2 = Car('blue', 200)
# print(c2.color, c2.speed)
#


class Rectangle:
    def __init__(self,  width = 5.0, height = 10.0 ):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

r1 = Rectangle()
print("Perimeter is ", r1.calculate_perimeter())
r2 = Rectangle(15, 20)
print("Perimeter is ", r2.calculate_perimeter())

