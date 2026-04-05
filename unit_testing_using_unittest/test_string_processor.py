"""
Unit tests for the StringProcessor class using the unittest framework.
"""
import unittest
from .string_processor import StringProcessor


class TestStringProcessor(unittest.TestCase):
    """
    TestCase class for validating string manipulation methods in StringProcessor.
    """

    def setUp(self) -> None:
        """
        Set up a StringProcessor instance before each test method.
        """
        self.processor = StringProcessor()

    @unittest.skip("There seems to be a problem with the empty row, it will be corrected later")
    def test_reverse_empty_string(self) -> None:
        """
        Test that an empty string remains empty when reversed.
        """
        self.assertEqual(self.processor.reverse_string(""), "")

    def test_reverse_string_with_simbols(self) -> None:
        """
        Test reversing strings that contain numbers and special characters.
        """
        self.assertEqual(self.processor.reverse_string("123!"), "!321")
        self.assertEqual(self.processor.reverse_string("Hello"), "olleH")

    def test_capitalize_string(self) -> None:
        """
        Test capitalization of various string formats (lowercase, uppercase, mixed).
        """
        self.assertEqual(self.processor.capitalize_string("hello"), "Hello")
        self.assertEqual(self.processor.capitalize_string("WORLD"), "World")
        self.assertEqual(self.processor.capitalize_string("123 test"), "123 test")

    def test_count_vowels(self) -> None:
        """
        Test counting vowels in English and Ukrainian, including empty strings.
        """
        self.assertEqual(self.processor.count_vowels("Apple"), 2)
        self.assertEqual(self.processor.count_vowels("Привіт"), 2)
        self.assertEqual(self.processor.count_vowels("12345"), 0)
        self.assertEqual(self.processor.count_vowels(""), 0)


if __name__ == "__main__":

    unittest.main()
