"""
Module for working with fractions.
Contains the Fraction class with support for arithmetic operations.
"""
import math

class Fraction:
    """
    Represents a fractional number and supports basic arithmetic operations.

    Attributes:
    num (int): The numerator of the fraction.
    den (int): The denominator of the fraction.
    """

    def __init__(self, numerator: int, denominator: int) -> None:
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        common = math.gcd(numerator, denominator)
        sign = -1 if denominator < 0 else 1
        self.num = (numerator // common) * sign
        self.den = abs(denominator // common)

    def __repr__(self) -> str:
        """Returns the string representation of a fraction."""

        return f"{self.num}/{self.den}"

    def __add__(self, other: Fraction) -> Fraction:
        """Addition: a/b + c/d = (ad + bc) / bd"""

        self.num = self.num * other.den + other.num * self.den
        self.den = self.den * other.den
        return Fraction(self.num, self.den)

    def __sub__(self, other: Fraction) -> Fraction:
        """Subtraction: a/b - c/d = (ad - bc) / bd"""

        self.num = self.num * other.den - other.num * self.den
        self.den = self.den * other.den
        return Fraction(self.num, self.den)

    def __mul__(self, other: Fraction) -> Fraction:
        """Multiplication: a/b * c/d = (ac) / (bd)"""

        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other: Fraction) -> Fraction:
        """Division: a/b / c/d = (ad) / (bc)"""

        return Fraction(self.num * other.den, self.den * other.num)



if __name__ == "__main__":

    f1 = Fraction(10, 20)
    f2 = Fraction(20, 30)

    print(f"Fraction 1: {f1}")
    print(f"Fraction 2: {f2}")
    print(f"Addition: {f1 + f2}")
    print(f"Subtraction: {f1 - f2}")
    print(f"Multiplication: {f1 * f2}")
    print(f"Division: {f1 / f2}")
