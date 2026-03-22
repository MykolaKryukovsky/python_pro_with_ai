"""
Module for introspection and content analysis of other modules.
"""
import inspect
import math

def analyze_module(module: object) -> None:
    """Lists all classes and functions in the specified module."""

    all_members = inspect.getmembers(module)

    classes = []
    functions = []

    for name, member in all_members:
        if inspect.isclass(member):
            classes.append(name)
        elif inspect.isfunction(member) or inspect.isbuiltin(member):
            functions.append(name)


    print(f"\nAnalysis: {getattr(module, '__name__', str(module))}")
    print(f"Classes: {classes}")
    print(f"Functions: {functions}")


if __name__ == "__main__":

    analyze_module(math.acos)
    analyze_module(math.asin)
    analyze_module(math.atan)
    analyze_module("math")
