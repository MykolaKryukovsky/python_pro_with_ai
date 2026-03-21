"""
Module for attribute type validation using a metaclass.
"""
from typing import Any, Type

class TypeCheckedMeta(type):
    """
    A metaclass that enforces type checking for class attributes.
    """

    def __new__(mcs, name: str, bases: tuple, dct: dict) -> Type:

        cls = super().__new__(mcs, name, bases, dct)

        annotations = getattr(cls, '__annotations__', {})

        def custom_setattr(self, key: str, value: Any) -> None :
            if key in annotations:
                expected_type = annotations[key]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Property '{key}' must be of type {expected_type.__name__}, "
                        f"but got {type(value).__name__} instead."
                    )
            object.__setattr__(self, key, value)

        cls.__setattr__ = custom_setattr
        return cls


class Person(metaclass=TypeCheckedMeta):
    """Class with type validation."""
    name: str = ""
    age: int = 0


if __name__ == "__main__":

    p = Person()
    p.name = "John"
    p.age = "30"
