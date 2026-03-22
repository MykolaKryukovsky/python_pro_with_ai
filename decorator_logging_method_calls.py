"""
A module for logging class methods.
Contains the log_methods decorator and an example of its use.
"""
from typing import Any, Callable, Type

def log_methods(cls: Type) -> Type:
    """A class decorator that logs calls to all of its methods."""

    for attr_name, attr_value in cls.__dict__.items():

        if callable(attr_value) and not attr_name.startswith("__"):

            def create_wrapper(method: Callable, name: str) -> Callable:

                def wrapper(self, *args: Any, **kwargs: Any) -> Any:

                    print(f"[MY LOG]: Call method {name}()")
                    print(f"Arguments: {args} {kwargs}")

                    return method(self, *args, **kwargs)

                wrapper.__name__ = method.__name__
                wrapper.__doc__ = method.__doc__

                return wrapper

            setattr(cls, attr_name, create_wrapper(attr_value, attr_name))

    return cls


@log_methods
class MyClass:
    """A class for performing basic arithmetic operations with logging."""

    def add(self, a, b):
        """Computes the sum of two integers."""
        return a + b

    def subtract(self, a, b):
        """Computes the difference of two integers."""
        return a - b



if __name__ == '__main__':

    obj = MyClass()
    obj.add(5, 3)
    obj.subtract(5, 3)
