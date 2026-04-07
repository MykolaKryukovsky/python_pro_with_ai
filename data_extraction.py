"""
This module provides a utility to remove URLs from text.
"""
import re


def remove_urls(txt):
    """
    Remove URLs starting with http, https, www, or even schema-relative links
    from the given text.
    """
    pattern = r'https?://\S+|www\.\S+'
    return re.sub(pattern, '', txt).strip()



if  __name__ == '__main__':

    TEXT = "Мій сайт: https://example.com. Також заходьте на ://google.com для пошуку."
    print(remove_urls(TEXT))
