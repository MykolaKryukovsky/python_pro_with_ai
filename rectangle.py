"""
A module for working with rectangles.
Contains the Rectangle class with methods
for calculating area and perimeter.
"""

class Rectangle:
    """
    A class for representing a geometric rectangle.

    Allows storing side dimensions and calculating area or perimeter.
    """

    def __init__(self, width: float, height: float) -> None:
        """Initializes a rectangle with the given width and height."""
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculates and returns the area of a rectangle."""
        return round(self.width * self.height, 2)

    def perimeter(self) -> float:
        """Calculates the perimeter of a rectangle."""
        return round(2 * (self.width + self.height), 2)

    def s_square(self) -> bool:
        """Checks whether a shape is a square."""
        return self.width == self.height

    def resize(self, new_width, new_height):
        """Sets new values for width and height """
        self.width = new_width
        self.height = new_height


if __name__ == "__main__":

    r1 = Rectangle(10, 5)

    assert r1.area() == 50, "Test 1"
    assert r1.perimeter() == 30, "Test 2"
    if not r1.s_square():
        print("This is not a square")
    r1.resize(12, 12)
    if r1.s_square():
        print("This is a square")
