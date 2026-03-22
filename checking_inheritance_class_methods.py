"""
A module for analyzing inheritance of classes and their methods.
"""
# pylint: disable=too-few-public-methods
class Parent:
    """Base class to demonstrate inheritance."""

    def parent_method(self) -> None:
        """Base class method."""

# pylint: disable=too-few-public-methods
class Child(Parent):
    """Child class of base class Parent."""

    def child_method(self) -> None:
        """Child class method."""


def analyze_inheritance(cls):
    """
    Parses a class, prints the name of its parent and a list of inherited methods.
    """

    all_parents = [base.__name__ for base in cls.__bases__]

    oll_staff = dir(cls)

    own_staff = cls.__dict__.keys()

    inherited_methods = []

    for method in oll_staff:
        if method not in own_staff:
            attr = getattr(cls, method)
            if callable(attr) and not method.startswith("__"):
                inherited_methods.append(method)

    print(f"Class {cls.__name__} inherits  methods: {inherited_methods} from {all_parents}" )



if __name__ == "__main__":

    analyze_inheritance(Child)
