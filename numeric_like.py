"""
A module for working with two-dimensional vectors.
Provides a Vector class with support for arithmetic and length comparison.
"""
import math

class Vector:
    """
    A class for working with two-dimensional vectors.

    Supports calculation of length, arithmetic operations
    and comparison of vectors based on their modules.
    """

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def length(self) -> float:
        """Calculates the length (modulus) of a vector using the formula √(x² + y²)."""

        return round(math.sqrt(self.x**2 + self.y**2), 1)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector) -> Vector:
        return Vector(self.x * other.x, self.y * other.y)

    def __lt__(self, other: Vector) -> bool:
        return self.length() < other.length()

    def __eq__(self, other: Vector) -> bool:
        return self.length() == other.length()

    def __repr__(self):
        return f"({self.x}, {self.y})"



if __name__ == "__main__":

    v1 = Vector(4, 8)
    v2 = Vector(6, 12)

    print(f"Vector 1: {v1}, Length: {v1.length()}")
    print(f"Vector 1: {v2}, Length: {v2.length()}")
    print(f"Addition: {v1 + v2}")
    print(f"Subtraction: {v1 - v2}")
    print(f"Multiplication by 2: {v1 * v2}")
    print(f"v1 < v2: {v1 < v2}")
    print(f"v1 == v2: {v1 == v2}")
