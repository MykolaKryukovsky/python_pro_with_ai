"""
A module for analyzing the content of other modules and objects.
"""
from typing import Any

class Calculator:
    """A simple class for demonstration."""

    @staticmethod
    def add(a, b):
        """returns the sum of two numbers"""
        return a + b

    @staticmethod
    def subtract(a, b):
        """returns the difference of two numbers"""
        return a - b


def call_function(obj1: Any, method_name: str, *args: Any) -> Any :
    """
    Calls an object's method by its string name with arbitrary arguments.
    """

    try:

        method = getattr(obj1, method_name)

        if callable(method):
            return method(*args)

        raise TypeError(f"'{method_name}' is not a callable method.")

    except AttributeError:
        print(f"❌ Error: Method '{method_name}' not found in object.")
        return None



if __name__ == "__main__":

    calc = Calculator()

    print(call_function(calc, "add", 10, 5))
    print(call_function(calc, "subtract", 10, 5))
