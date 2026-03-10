"""A module for creating a calculator using closures."""
from collections.abc import Callable

def  create_calculator(operator: str) -> Callable[[int, int], int | float | str]:
    """
    Creates and returns a function to perform a specific arithmetic operation.
    Uses closure to preserve the operator.
    """

    def multiply_by_two(num1: int, num2: int) -> float|str:
        """Performs calculations on two numbers."""

        if operator == "+":
            return num1 + num2
        if operator == "-":
            return num1 - num2
        if operator == "*":
            return num1 * num2
        if operator == "/":
            if num2 == 0:
                return "Illegal division by zero operation"
            if num2 != 0:
                return num1 / num2
        return "An invalid operator was entered"

    return multiply_by_two

if __name__ == "__main__":

    print(f"Addition (10 + 5): {create_calculator(operator="+")(10, 5)}")
    print(f"Subtraction (20 - 7): {create_calculator(operator="-")(21, 7)}")
    print(f"Multiplication (4 * 8): {create_calculator(operator="*")(4, 8)}")
    print(f"Division (15 / 3): {create_calculator(operator="/")(9, 3)}")
    print(f"Division by zero: {create_calculator(operator="/")(10, 0)}")
