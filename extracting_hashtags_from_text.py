"""
This module provides a utility to extract hashtags from text.
"""
import re


def find_hashtags(txt: str) -> list:
    """
    Extract all hashtags from the given text.
    A hashtag is defined as a '#' symbol followed by alphanumeric
    characters or underscores.
    """
    pattern = re.compile(r"#\w+")

    return pattern.findall(txt)


if __name__ == '__main__':

    TEXT = "Привіт! #python і #coding - це круто. #2026"
    print(find_hashtags(TEXT))
