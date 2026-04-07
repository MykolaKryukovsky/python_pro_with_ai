"""
This module provides a utility to extract valid IPv4 addresses from text.
"""
import re


def find_ipv4_addresses(txt):
    """
    Extract all valid IPv4 addresses from the given text.
    The function finds sequences of four numbers separated by dots
    and validates that each number is within the range 0-255.
    """
    pattern = r'\b(?:(?:\d{1,3}\.){3}\d{1,3})\b'
    candidates = re.findall(pattern, txt)

    valid_ips = [
        ip for ip in candidates
        if all(0 <= int(part) <= 255 for part in ip.split('.'))
    ]

    return valid_ips


if __name__ == '__main__':

    TEXT = "Сервер 1: 192.168.1.1, Сервер 2: 10.0.0.255, Помилка: 999.1.1.1"
    print(find_ipv4_addresses(TEXT))
