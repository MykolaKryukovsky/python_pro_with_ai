"""
A module for object analysis and introspection demonstration.
"""
from typing import Any

class MyClass:
    """
    A class for demonstrating metaprogramming and introspection.
    """

    def __init__(self, value: str) -> None:
        self.value = value

    def say_hello(self) -> str:
        """Returns the greeting period."""

        return f"Hello, {self.value}"


def  analyze_object(ob1j: Any) -> None:
    """
    Performs introspection of the object and displays its attributes.
    """

    print(f"Type: {type(ob1j)}\n")

    attributes = dir(ob1j)

    for name in attributes:

        value = getattr(ob1j, name)
        print(f"Name: {name} | Type: {type(value).__name__}")




if __name__ == '__main__':

    obj = MyClass("World")

    analyze_object(obj)
