import math

class Circle():
    def __init__ (self, radius):
        self.radius = radius
        
    def calculateCircleArea(self):
        return math.pi * self.radius**2
    
    def calculateCirclePerimeter(self):
        return 2 * math.pi *self.radius
    
radius = float(input('Input the area of the circle:'))
    
circle = Circle (3)

area = circle.calculateCircleArea()

perimeter = circle.calculateCirclePerimeter ()

print ('Area of the circle:', area)
print ('Perimeter of the circle:', perimeter)