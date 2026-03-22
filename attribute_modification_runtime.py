"""
A module for demonstrating the dynamic change of class attributes.
"""
class MutableClass:
    """
    A class that allows adding and removing attributes dynamically
    with the help of add_attribute and remove_attribute methods.
    """

    name: str = ""

    def add_attribute(self, name_at: str, value: str) -> None:
        """Adds a new object attribute."""
        setattr(self, name_at, value)

    def remove_attribute(self, name_at: str) -> None:
        """Removes an attribute from an object."""
        if hasattr(self, name_at):
            delattr(self, name_at)


if __name__ == '__main__':

    obj = MutableClass()

    obj.add_attribute("name", "Python")
    print(obj.name)

    obj.remove_attribute("name")
    print(obj.name)
