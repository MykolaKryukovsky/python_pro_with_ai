"""
Module for age verification logic.
"""


# pylint: disable=too-few-public-methods
class AgeVerifier:
    """
    A utility class to verify age requirements.
    """

    @staticmethod
    def is_adult(age: int) -> bool:
        """
        Return True if the age is 18 or older.
        """
        return age >= 18
