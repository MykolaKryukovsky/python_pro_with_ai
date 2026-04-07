"""
Module for text processing using regular expressions.
This module provides utility functions to extract and manipulate specific
data patterns such as credit card numbers, social media tags, prices,
and words of specific lengths.
"""
import re


def find_credit_cards(txt: str) -> list:
    """
    Search for credit card numbers in the text.
    Supports formats: 16 digits straight, or separated by spaces/hyphens
    every 4 digits (e.g., 1234-5678-1234-5678).
    """
    pattern = r'\b\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b'

    return re.findall(pattern, txt)


def extract_social_tags(txt: str) -> list:
    """
    Extract hashtags (#) and mentions (@) from the text.
    Uses negative lookbehind to ensure @mentions are not part of an email address.
    """
    pattern = r'(?<![\w])(?:#\w+|@\w+)'

    return re.findall(pattern, txt)

def mask_card(txt: str) -> str:
    """
    Hide the first 12 digits of a credit card number, leaving only the last 4.
    Example: 1234-5678-1234-5678 -> ****-****-****-5678.
    """
    pattern = r'\b(\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?)(\d{4})\b'

    return re.sub(pattern, r'****-****-****-\2', txt)

def find_prices(txt: str) -> list:
    """
    Find prices with currency symbols or codes ($, USD, грн).
    Supports currency both before and after the amount, including optional decimals.
    """
    pattern = r'(?:\$|USD|грн)\s?\d+(?:\.\d{2})?|\d+(?:\.\d{2})?\s?(?:\$|USD|грн)'

    return re.findall(pattern, txt)

def find_words_by_length(txt: str, length: int) -> list:
    """
    Find all words in the text that have a specific number of characters.
    Supports Latin and Cyrillic alphabets.
    """
    pattern = rf'\b[a-zA-Zа-яА-ЯіїєґІЇЄҐ]{{{length}}}\b'

    return re.findall(pattern, txt)


if  __name__ == '__main__':

    TEXT_CARDS = ("Мои карты: 4444-5555-6666-7777, "
        "а также 1234 5678 1234 5678 и старая 1111222233334444"
    )
    print(find_credit_cards(TEXT_CARDS))

    print(mask_card("Оплата картой 4444-5555-6666-7777"))

    TEXT_TAGS = """
    Привіт @alex_99! Подивись мій новий пост про #python та #програмування. 
    Якщо є питання, пиши на alex@gmail.com.
    """
    TAGS = extract_social_tags(TEXT_TAGS )
    print(TAGS)

    TEXT_PRICES = "Книга стоит $10.50, а журнал 150 грн. Есть еще VIP за USD 500."
    print(find_prices(TEXT_PRICES))

    TEXT_WORDS = "Apple, банан, груша та ківі — це фрукти."
    print(find_words_by_length(TEXT_WORDS, 5))
