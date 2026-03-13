"""
A module for working with multidimensional vectors (n-dimensional space).
"""
import math

class Vector:
    """
    Represents a vector in n-dimensional space.
    """

    def __init__(self, *coordinat: float) -> None:
        """
        Initializes a vector with an arbitrary number of coordinates.
        Example: v = Vector(1, 2, 3)
        """

        if not coordinat:
            raise ValueError("Vector must have at least one coordinate.")

        self._coordinates = tuple(coordinat)

    @property
    def coordinates_vector(self) -> tuple:
        """Returns a tuple of vector coordinates."""

        return self._coordinates

    def length(self) -> float:
        """
        Calculates the length (modulus) of an n-dimensional vector.
        Formula: sqrt(x1² + x2² + ... + xn²)
        """

        return round(math.sqrt(sum(x ** 2 for x in self._coordinates)), 1)

    def __add__(self, other: Vector) -> Vector:
        """Adding two vectors of the same dimension."""

        if len(other.coordinates_vector) != len(self._coordinates):
            raise ValueError("Vectors must have the same number of coordinates.")

        return Vector(*[a + b for a, b in zip(self._coordinates, other._coordinates)])

    def __sub__(self, other: Vector) -> Vector:
        """Subtracting two vectors of the same dimension."""

        if len(other.coordinates_vector) != len(self._coordinates):
            raise ValueError("Vectors must have the same number of coordinates.")

        return Vector(*[a - b for a, b in zip(self._coordinates, other._coordinates)])

    def __mul__(self, other: Vector) -> Vector:
        """Multiplying two vectors of the same dimension."""

        if len(other.coordinates_vector) != len(self._coordinates):
            raise ValueError("Vectors must have the same number of coordinates.")

        return Vector(*[a * b for a, b in zip(self._coordinates, other._coordinates)])

    def __repr__(self) -> str:

        return f"{self._coordinates}"



if __name__ == "__main__":

    V1 = Vector(3, 6, 3)
    V2 = Vector(1, 2, 4)
    V3 = Vector(1, 1, 3, 3, 1)

    print(f"V1: {V1}, Length: {V1.length()}")
    print(f"V2: {V2}, Length: {V2.length()}")
    print(f"V3: {V3}, Length: {V3.length()}")
    print(f"Adding:V1 + V2 {V1 + V2}")
    print(f"Subtracting: V1 - V2 {V1 - V2}")
    print(f"Multiplication: V1 * V2 {V1 * V2}")
    V4 = V1 * V2
    print(f"V4: {V4}, Length: {V4.length()}")
    print(f"Multiplication: V4 * V2 {V4 * V2}")
    try:
        print(f"Addition: V3 + V2 {V3 + V2}")
    except ValueError as exc:
        print(f"Error: {exc}")
