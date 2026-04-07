"""
This module provides utilities to find and normalize phone numbers in text.
"""
import re


def find_all_phones(text: str) -> list:
    """
    Find phone numbers in various formats and normalize them.
    Extracts numbers with optional country codes, parentheses, and separators.
    Normalizes them by removing all non-digit characters except for the leading '+'.
    """
    pattern = r'(\+?\d{1,3})?[\s.-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{2}[\s.-]?\d{2,4}'
    raw_numbers = [match.group().strip() for match in re.finditer(pattern, text)]

    normalized = []

    for number in raw_numbers:
        clean_num = re.sub(r'[^\d+]', '', number)
        normalized.append(clean_num)

    return normalized


if __name__ == '__main__':

    TEST_TEXT = """
        Україна: +380 67 123 45 67 або 067-123-45-67
        США: +1 (123) 456-7890 або 123.456.7890
        Простий: 1234567890
    """

    print(find_all_phones(TEST_TEXT))
