"""
This module demonstrates basic asynchronous programming patterns in Python.
It simulates concurrent web page downloads using asyncio.sleep to mimic
network latency and asyncio.gather to manage multiple tasks simultaneously.
"""
import asyncio
import random
import time


async def download_page(url: str) -> tuple:
    """
    Simulates downloading a web page asynchronously.
    Args:
    url (str): The URL of the page to "download".
    Returns:
    tuple: A tuple containing the URL and the time taken to load.
    """
    load_time = random.uniform(1, 5)
    await asyncio.sleep(load_time)

    print(f"Downloading {url} | Time: {load_time:.2f} seconds")
    return url, load_time


async def main(urls: list) -> list:
    """
    Coordinates the concurrent download of multiple URLs.
    Args:
    urls (list): A list of strings representing the URLs to be processed.
    Returns:
    list: A list of tuples, where each tuple contains a URL and its load time.
    """
    print(f"Start downloading {len(urls)} pages...\n")

    tasks = [download_page(url) for url in urls]

    results = await asyncio.gather(*tasks)

    return results


if __name__ == "__main__":

    list_of_urls = [f"https://example.com{i}" for i in range(1, 11)]

    start_time = time.perf_counter()
    asyncio.run(main(list_of_urls))
    end_time = time.perf_counter()

    print(f"Downloaded pages total time: {end_time - start_time:.2f} seconds")
