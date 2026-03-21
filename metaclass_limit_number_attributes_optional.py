"""
Module for limiting the number of class attributes using a metaclass.
"""
from typing import Any, Type

class LimitedAttributesMeta(type):
    """A metaclass that limits the number of custom attributes in a class."""

    def __new__(mcs, name: str, bases: tuple, dct: dict) -> Type:

        user_attributes = [attr for attr in dct if not attr.startswith("__")]

        if len(user_attributes) > 3:
            raise TypeError(f"Class {name} cannot have more than 3 attributes. "
                            f"Found: {len(user_attributes)}"
            )

        return super().__new__(mcs, name, bases, dct)



class LimitedClass(metaclass=LimitedAttributesMeta):
    """An example of a class that obeys the rules of LimitedAttributesMeta."""
    attr1 = 1
    attr2 = 2
    attr3 = 3
    attr4 = 4



if __name__ == "__main__":

    obj = LimitedClass()
