import math


class Shape:
    def __init__(self,area) :
        pass      

class Rectangle (Shape):
    def __init__(self, length,width):
       self.length = length
       self.width = width
       return {self.length}*{self.width}

class Circle (Shape):
    def __init__(self, radius):
        self.radius = radius
        return math.pi*{self.radius**2}