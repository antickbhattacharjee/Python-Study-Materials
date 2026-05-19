# Abstraction using python

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
# Create objects of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)
# Calculate and print the area of Circle and Rectangle
print("Area of Circle:", circle.area())
print("Area of Rectangle:", rectangle.area())

