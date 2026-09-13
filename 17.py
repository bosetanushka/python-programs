import math

class Shape:

    # Constructor
    def __init__(self, radius):
        self.radius = radius

    # Calculate area of circle
    def calArea(self):
        area = math.pi * self.radius * self.radius
        print("Area of Circle:", area)


class Sphere(Shape):

    # Calculate volume of sphere
    def calVolume(self):
        volume = (4 / 3) * math.pi * self.radius ** 3
        print("Volume of Sphere:", volume)


# Create Sphere object
s1 = Sphere(5)

# Calculate area
s1.calArea()

# Calculate volume
s1.calVolume()