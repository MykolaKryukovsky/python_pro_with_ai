"""
A module to demonstrate dynamic class creation.
"""
from typing import Any, Dict, Callable, Type

def say_hello(_self) -> str:
    """Returns a greeting."""
    return "Hello!"


def say_goodbye(_self) -> str:
    """Returns a farewell."""
    return "Goodbye!"

def create_class(class_name: Any, methods_class: Dict[str, Callable[[Any], str]]) -> Type:
    """
    Creates a class with the given name and methods.

    :param class_name: Class name (string)
    :param methods: Dictionary {method_name: function}
    :return: New class
    """
    return type(class_name, (object,), methods_class)




if __name__ == "__main__":

    methods = {
        "say_hello": say_hello,
        "say_goodbye": say_goodbye
    }

    DynamicRobot = create_class("Robot", methods)

    bot = DynamicRobot()

    print(bot.say_hello())
    print(bot.say_goodbye())
