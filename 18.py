"""  Create a class triangle with 3 variables side1, side2, side3. Initialize the variables with constructor.
 It also has the variables angle1, angle2, angle3. Create a class equilateral triangle and find the area of
 the triangle using calArea() function. Find the tangent of all angles using find angles method.
 Create a class scalene which is a child of triangle class. Find out the perimeter of the triangle using 
calPerimeter() function. Find out the area of the triangle using calArea() function. Use the math package
 for the computation. Print the area as a whole number.
 """


import math

class Triangle:

    # Constructor
    def __init__(self, side1, side2, side3, angle1, angle2, angle3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3


class Equilateral(Triangle):

    # Calculate area
    def calArea(self):
        area = (math.sqrt(3) / 4) * self.side1 ** 2
        print("Area of Equilateral Triangle:", round(area))

    # Find tangent of all angles
    def findAngles(self):
        print("Tan of angle 1:", math.tan(math.radians(self.angle1)))
        print("Tan of angle 2:", math.tan(math.radians(self.angle2)))
        print("Tan of angle 3:", math.tan(math.radians(self.angle3)))


class Scalene(Triangle):

    # Calculate perimeter
    def calPerimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        print("Perimeter of Scalene Triangle:", perimeter)

    # Calculate area using Heron's formula
    def calArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2

        area = math.sqrt(
            s * (s - self.side1) *
            (s - self.side2) *
            (s - self.side3)
        )

        print("Area of Scalene Triangle:", round(area))


# Equilateral Triangle object
e1 = Equilateral(6, 6, 6, 60, 60, 60)

print("EQUILATERAL TRIANGLE")
e1.calArea()
e1.findAngles()


# Scalene Triangle object
s1 = Scalene(5, 6, 7, 50, 60, 70)

print("\nSCALENE TRIANGLE")
s1.calPerimeter()
s1.calArea()