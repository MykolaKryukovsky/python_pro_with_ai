"""
Module for mathematical operations with doctests.
"""
import doctest


def is_even(num: int) -> bool:
    """
    Перевіряє, чи є число парним
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    >>> is_even(0)
    True
    """
    return num % 2 == 0

def factorial(num: int) -> int:
    """
    Повертає факторіал числа
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(3)
    6
    """
    if num < 0:
        raise ValueError("num must be non-negative")
    if num == 0:
        return 1
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


if __name__ == '__main__':

    doctest.testmod()
