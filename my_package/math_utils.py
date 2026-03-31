"""
This module contains functions for factorial calculation.
"""
import math


def factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer.
    It uses an iterative approach to avoid the RecursionError error.
    """
    if n < 0:
        raise ValueError("The factorial is defined only for non-negative numbers.")
    return math.factorial(n)


def gcd(a: int, b: int) -> int:
    """
    Finds the greatest common divisor of two integers.
    Uses the standard math library for maximum speed.
    """
    return math.gcd(a, b)
