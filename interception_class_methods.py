"""
A module for implementing the Proxy pattern.
"""
import logging
from typing import Any

# pylint: disable=too-few-public-methods
class MyClass:
    """A simple class for demonstration."""

    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    @staticmethod
    def greet(name: str) -> str:
        """Static greeting method."""
        return f"Hello, {name}!"

# pylint: disable=too-few-public-methods
class Proxy:
    """Proxy class for call interception."""

    def __init__(self, target_obj: Any) -> None:
        self.target_obj = target_obj

    def __getattr__(self, name: str) -> Any:
        """Intercepts access to attributes and methods."""

        attr = getattr(self.target_obj, name)

        if callable(attr):
            def wrapper(*args, **kwargs):

                logging.info("Method '%s' called with %s %s", name, args, kwargs)

                return attr(*args, **kwargs)

            return wrapper

        return attr

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - [PROXY LOG] - %(message)s')

    obj = MyClass("SomeName")
    proxy = Proxy(obj)

    print(proxy.greet("Alice"))
