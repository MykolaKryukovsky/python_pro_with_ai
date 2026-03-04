"""
Calculates the area of circle given its radius.
Uses the formula: S = π * r²
Args:
radius (float): The radius of the circle.
Must be a non-negative number.
Returns:
float: The area of the circle.
"""

import math


def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle given a radius.

    Arguments:
    radius (float): The radius of the circle.

    Return:
    float: The area of the circle.
    """

    return round(math.pi * radius ** 2, 2)


while True:
    try:
        radius_circle = float(input("Enter the radius of the circle: "))
        print(calculate_circle_area(radius_circle))
        break
    except ValueError:
        print("Error! This is not a number. Try again.")
