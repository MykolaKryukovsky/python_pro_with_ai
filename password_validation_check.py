"""
This module provides a utility to validate password strength.
"""
import re


def is_password_strong(password: str) -> bool:
    """
    Check if a password meets complexity requirements.
    Criteria:
    Minimum 8 characters.
    At least one lowercase letter.
    At least one uppercase letter.
    At least one digit.
    At least one special character (@, #, $, %, &, +, =, !).
    """
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%&+=!]).{8,}$'
    return bool(re.match(pattern, password))


if __name__ == '__main__':

    print(is_password_strong("Weak123"))
    print(is_password_strong("strong@Pass123"))
    print(is_password_strong("12345678"))
