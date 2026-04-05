"""
Module for basic mathematical operations.
"""


def divide(a: int, b: int) -> float:
    """
    Divide two integers and return a float.
    Raises ZeroDivisionError if the divisor is zero.
    """
    if b == 0:
        raise ZeroDivisionError('Division by zero')

    return a / b
