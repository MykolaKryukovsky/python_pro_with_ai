"""
This module provides utilities for analyzing web server log files.
It extracts IPv4 addresses and calculates request statistics.
"""
import re
from collections import Counter


def analyze_web_log(log_text: str) -> Counter:
    """
    Extracts valid IPv4 addresses from log text and counts their occurrences.
    Args:
    log_text: A string containing web server logs.
    Returns:
    A Counter object mapping IP addresses to the number of requests.
    """
    ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

    all_ips = re.findall(ip_pattern, log_text)

    valid_ips = [
        ip for ip in all_ips
        if all(0 <= int(part) <= 255 for part in ip.split('.'))
    ]

    ip_stats = Counter(valid_ips)

    return ip_stats


if '__main__' == __name__:

    LOG_DATA = """
    192.168.1.1 - - [10/Oct/2023:13:55:36] "GET /home HTTP/1.1" 200
    10.0.0.5 - - [10/Oct/2023:13:55:38] "POST /login HTTP/1.1" 401
    192.168.1.1 - - [10/Oct/2023:13:56:01] "GET /about HTTP/1.1" 200
    172.16.0.1 - - [10/Oct/2023:13:56:10] "GET /contact HTTP/1.1" 200
    10.0.0.5 - - [10/Oct/2023:13:56:15] "GET /home HTTP/1.1" 200
    """

    STATS = analyze_web_log(LOG_DATA)

    print("Статистика запитів за IP:")

    for ip, count in STATS.most_common():
        print(f"IP: {ip:15} | Запитів: {count}")
