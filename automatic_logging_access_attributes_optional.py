"""
Module for automatic attribute access logging using a metaclass.
"""
from typing import Any, Type

class LoggingMeta(type):
    """
    A metaclass that injects logging behavior into attribute access
    and modification for the created class.
    """

    def __new__(mcs, name: str, bases: tuple, dct: dict) -> Type:
        """
        Intercepts class creation to add custom __getattribute__
        and __setattr__ methods.
        """

        def __getattribute__(self, item: str) -> None:
            """Logs every time an attribute is accessed."""

            print(f"Logging: accessed '{item}'")
            return object.__getattribute__(self, item)

        def __setattr__(self, key: str, value: Any) -> None :
            """Logs every time an attribute is modified."""

            print(f"Logging: modified '{key}'")
            return object.__setattr__(self, key, value)

        dct['__getattribute__'] = __getattribute__
        dct['__setattr__'] = __setattr__

        return super().__new__(mcs, name, bases, dct)


class MyClass(metaclass=LoggingMeta):
    """
    A sample class that demonstrates automatic logging via LoggingMeta.
    """

    def __init__(self, name):

        self.name = name


if __name__ == "__main__":

    obj = MyClass("Python")
    print(obj.name)
    obj.name = "New Python"
    print(obj.name)
