"""
This module provides a utility to strip HTML tags from text content.
"""
import re


def remove_html_tags(text: str) -> str:
    """
    Remove all HTML tags from the provided string using regular expressions.
    It targets anything between '<' and '>' characters and replaces it with
    an empty string.
    """
    clean_text = re.sub(r'<[^>]*>', '', text)

    return clean_text


if __name__ == '__main__':

    HTML_CONTENT = "<h1>Вітаю!</h1><p>Це текст із <a href='#'>посиланням</a>.</p>"
    print(remove_html_tags(HTML_CONTENT))
