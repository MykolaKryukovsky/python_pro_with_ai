"""
A module for dynamically creating properties in a class.
"""
from typing import Any

class DynamicProperties:
    """A class that allows adding properties at runtime."""

    def add_property(self, name: str, value: str) -> None:
        """Dynamically creates a getter and setter for a new property."""

        name_st = f"_{name}"
        setattr(self, name_st, value)

        def getter(instance: Any) -> Any:
            """Getter function for the dynamic property."""
            return getattr(instance, name_st)

        def setter(instance: Any, value_v: Any) -> None:
            """Setter function for the dynamic property."""
            setattr(instance, name_st, value_v)

        setattr(self.__class__, name, property(getter, setter))


if __name__ == "__main__":

    obj = DynamicProperties()
    obj.add_property('name', 'default_name')

    print(obj.name)

    obj.name = "Python"

    print(obj.name)
