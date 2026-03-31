"""
The main module of the application.
Demonstrates work with local utilities for mathematics and time.
"""
import math_utils # pylint: disable=import-error
import string_utils # pylint: disable=import-error

print(math_utils.factorial(6))

print(math_utils.gcd(7, 21))

print(string_utils.to_uppercase('hello world'))

print(string_utils.trim_spaces(' hello world '))
