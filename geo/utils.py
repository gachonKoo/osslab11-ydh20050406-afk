import math

def pythagoras(a, b):
    """Return the hypotenuse of a right triangle."""
    c = math.sqrt(a**2 + b**2)
    return c

def circle(r):
    """Return the area of a circle with radius r."""
    area = math.pi * r**2
    return area
