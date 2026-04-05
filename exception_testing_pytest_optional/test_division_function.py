"""
Unit tests for the division function using pytest.
"""
import pytest
from .division_function import divide


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (20, 5, 4.0),
    (7, 2, 3.5),
    (0, 5, 0.0)
])
def test_divide_success(a: int, b: int, expected: float) -> None:
    """
    Test successful division cases with various integer inputs.
    """
    assert divide(a, b) == expected

def test_divide_zero_exception() -> None:
    """
    Test that dividing by zero raises a ZeroDivisionError.
    """
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
