"""
This module provides a utility to reformat dates in text.
"""
import re


def reformat_date(txt):
    """
    Change date format from DD/MM/YYYY to YYYY-MM-DD.
    Uses capture groups to rearrange day, month, and year segments.
    """
    pattern = r'\b(\d{2})/(\d{2})/(\d{4})\b'
    return re.sub(pattern, r'\3-\2-\1', txt)


if __name__ == '__main__':

    TEXT = "Сьогодні 07/04/2026, а завтра буде 08/04/2026."
    NEW_TEXT = reformat_date(TEXT)
    print(NEW_TEXT)
