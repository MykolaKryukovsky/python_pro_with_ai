"""
This module provides a utility to validate email addresses.
"""
import re


def is_valid_email(email):
    """
    Validate if the given string follows a standard email format.
    Rules:
    Local part cannot start or end with a dot.
    Domain part must have at least one dot and a suffix of 2-6 letters.
    Only alphanumeric characters and dots are allowed in the local part.
    """
    pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9.]*[a-zA-Z0-9])?@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}$'
    return re.match(pattern, email) is not None


if __name__ == '__main__':
    print(is_valid_email("test.user@mail.com"))
    print(is_valid_email(".test@mail.com"))
    print(is_valid_email("test@domain.c"))
