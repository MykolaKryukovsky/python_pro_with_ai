"""
A module for caching function results through closures.
"""
from collections.abc import Callable


def memoize(function: Callable) -> Callable:
    """
    Creates a cache for the results of a function.
    Uses a lock to store the cache dictionary.
    """

    cache = {}

    def wrapper(n: int) -> int:
        """Checks for cached results before calculating."""

        if n not in cache:

            cache[n] = function(n)
            print(f"[Cache] Saved result for: {n}")

        return cache[n]

    return wrapper


@memoize
def fibonacci(n: int) -> int:
    """Recursive calculation of Fibonacci numbers."""

    if n <= 1:

        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":

    NUMBER = 10

    print(f"Calculating Fibonacci({NUMBER})...")
    result = fibonacci(NUMBER)
    print(f"Result: {result}")


    print("\nRecall (result should be instant):")
    result_fast = fibonacci(NUMBER)
    print(f"Result: {result_fast}")
