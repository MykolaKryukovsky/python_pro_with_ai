"""
A module with its own implementation of the functions my_len, my_sum and my_min.
These functions repeat the logic of built-in Python functions.
"""
from typing import Iterable, Any


def len(iterable: Iterable) -> int:
    """
    Calculates the number of elements in the iterable object.

    Accepts: any collection (list, tuple, str).
    Returns: an integer (int).
    """

    count = 0

    for _ in iterable:
        count += 1
    return count


def sum(iterable: Iterable) -> int:
    """A custom version of the sum() function. Adds elements to the original value."""

    total = 0

    for item in iterable:
        total += item
    return total


def min(iterable: Iterable) -> Any:
    """Finds the minimum element in the collection."""

    iterator = iter(iterable)

    try:
        current = next(iterator)
    except StopIteration as exc:
        raise ValueError("min() got an empty iterator ") from exc

    for item in iterator:
        if item < current:
            current = item

    return current



if __name__ == "__main__":

    TEST_DATA = [5, 7, 23, 12, 3, 8, 33, 52]

    S1 = sum(TEST_DATA)
    M1 = min(TEST_DATA)
    L1 = len(TEST_DATA)

    assert S1 == sum(TEST_DATA)
    assert M1 == min(TEST_DATA)
    assert L1 == len(TEST_DATA)

    print(S1)
    print(M1)
    print(L1)
