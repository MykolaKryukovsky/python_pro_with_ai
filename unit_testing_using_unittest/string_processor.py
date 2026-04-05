"""
Module for processing and manipulating strings.
"""


class StringProcessor:
    """
    A utility class for various string operations.
    """

    def reverse_string(self, s: str) -> str:
        """
        Return the reversed version of the input string.
        """
        return s[::-1]

    def capitalize_string(self, s: str) -> str:
        """
        Capitalize the first letter of the input string.
        """
        return s.capitalize()

    def count_vowels(self, s: str) -> int:
        """
        Count the number of vowels in a string, supporting English and Ukrainian.
        """
        vowels = "aeiouyAEIOUYаеєиіїоуюяАЕЄИІЇОУЮЯ"
        return sum(1 for char in s if char in vowels)
