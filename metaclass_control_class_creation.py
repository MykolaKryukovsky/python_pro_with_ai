"""
A module for implementing the Singleton pattern using a metaclass.
It guarantees the creation of only one instance for each class.
"""

class SingletonMeta(type):
    """Metaclass for creating a Singleton."""

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in type(cls)._instances:
            instance = super().__call__(*args, **kwargs)
            type(cls)._instances[cls] = instance
        return type(cls)._instances[cls]

# pylint: disable=too-few-public-methods
class Singleton(metaclass=SingletonMeta):
    """Singleton class."""

    def __init__(self):
        print("Creating instance")


if __name__ == '__main__':


    obj1 = Singleton()
    obj2 = Singleton()
    print(obj1 is obj2)
