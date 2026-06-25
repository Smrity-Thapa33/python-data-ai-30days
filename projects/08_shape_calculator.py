"""
Assignment 4 — Shape Calculator
=================================
Week 2 · Dlytica Data and AI Foundations Track
Topics: Classes & Objects, Instance Methods, @staticmethod, @classmethod
"""

import math

class Circle:
    shapes_created = 0                       
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius
        Circle.shapes_created += 1

    def area(self):
        """Return area rounded to 2 decimal places."""
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        """Return circumference rounded to 2 decimal places."""
        return round(2 * math.pi * self.radius, 2)

    @staticmethod
    def cm_to_inch(cm):
        """Convert centimetres to inches."""
        return round(cm * 0.3937, 3)

    @staticmethod
    def is_valid_dimension(val):
        """Return True if val is a positive number."""
        return val > 0

    @classmethod
    def total_created(cls):
        return f"Circles created: {cls.shapes_created}"

    def __str__(self):
        return f"Circle(r={self.radius})"


class Rectangle:
    shapes_created = 0                      

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive.")
        self.width  = width
        self.height = height
        Rectangle.shapes_created += 1

    def area(self):
        return round(self.width * self.height, 2)

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def is_square(self):
        """Return True if width equals height."""
        return self.width == self.height

    @staticmethod
    def cm_to_inch(cm):
        return round(cm * 0.3937, 3)

    @staticmethod
    def is_valid_dimension(val):
        return val > 0

    @classmethod
    def total_created(cls):
        return f"Rectangles created: {cls.shapes_created}"

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"


print("=" * 45)
print("          SHAPE CALCULATOR")
print("=" * 45)

c1 = Circle(5)
c2 = Circle(3)
c3 = Circle(7)
r1 = Rectangle(4, 6)
r2 = Rectangle(5, 5)

print(f"\n  {c1}")
print(f"  Area      : {c1.area()}")
print(f"  Perimeter : {c1.perimeter()}")

print(f"\n  {r1}")
print(f"  Area      : {r1.area()}")
print(f"  Perimeter : {r1.perimeter()}")
print(f"  Is square : {r1.is_square()}")

print(f"\n  {r2}")
print(f"  Is square : {r2.is_square()}")

print("\n-- Static Methods --")
print(f"  10 cm in inches            : {Circle.cm_to_inch(10)}")
print(f"  is_valid_dimension(-2)     : {Rectangle.is_valid_dimension(-2)}")
print(f"  is_valid_dimension(5)      : {Rectangle.is_valid_dimension(5)}")

print("\n-- Shape Counts --")
print(f"  {Circle.total_created()}")
print(f"  {Rectangle.total_created()}")

print("\n-- Testing ValueError (invalid dimensions) --")
try:
    Circle(-3)
except ValueError as e:
    print(f"Circle(-3)      → {e}")

try:
    Rectangle(0, 5)
except ValueError as e:
    print(f"Rectangle(0,5)  → {e}")

print("=" * 45)