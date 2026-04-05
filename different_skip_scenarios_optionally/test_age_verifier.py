"""
Unit tests for the AgeVerifier class using pytest.
"""
import pytest
from .age_verifier import AgeVerifier


class TestAgeVerifier:
    """
    Test suite for verifying age-related logic in the AgeVerifier class.
    """

    @pytest.mark.parametrize("age, expected", [
        (18, True),
        (25, True),
        (17, False),
        (0, False),

        pytest.param(-5, False,
                     marks=pytest.mark.skip(reason="Вік не може бути від'ємним")),

        pytest.param(121, True, marks=pytest.mark.skipif(True,
                                                reason="Малоймовірний вік (>120)")),

        pytest.param(150, True, marks=pytest.mark.skipif(True,
                                                reason="Малоймовірний вік (>120)"))
    ])
    def test_is_adult_parametrized(self, age: int, expected: bool) -> None:
        """
        Test age verification with various inputs using parametrization.
        """
        assert AgeVerifier.is_adult(age) == expected

    @pytest.mark.skip(reason="Тест в розробці або дані некоректні")
    def test_invalid_age_manual_skip(self) -> None:
        """
        Manually skipped test for invalid age handling.
        """
        assert AgeVerifier.is_adult(-1) is False

    @pytest.mark.skipif(True, reason="Демонстрація пропуску за умовою")
    def test_extreme_age_condition(self) -> None:
        """
        Test extreme age values with a conditional skip.
        """
        assert AgeVerifier.is_adult(200) is True
