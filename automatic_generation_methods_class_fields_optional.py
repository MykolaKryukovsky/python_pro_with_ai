"""
Module for automatic generation of getter and setter methods using a metaclass.
"""
from typing import Any, Callable, Type

class AutoMethodMeta(type):
    """
    A metaclass that automatically creates get_<attr> and set_<attr>
    methods for each class attribute.
    """

    def __new__(mcs, name: str, bases: tuple, dct: dict) -> Type:

        attributes = [attr for attr in dct if not attr.startswith("__")]

        for attr in attributes:

            def make_getter(field: str) -> Callable[[Any], Any]:
                return lambda self: getattr(self, field)

            def make_setter(field: str) -> Callable[[Any, Any], None]:
                return lambda self, value: setattr(self, field, value)

            dct[f"get_{attr}"] = make_getter(attr)
            dct[f"set_{attr}"] = make_setter(attr)

        return super().__new__(mcs, name, bases, dct)


class Person(metaclass=AutoMethodMeta):
    """
    A class that automatically receives getter and setter methods for its fields.
    """
    name = "John"
    age = 30


if __name__ == "__main__":

    p = Person()

    print(f"Name: {p.get_name()}")

    p.set_age(31)
    print(f"New age: {p.get_age()}")
