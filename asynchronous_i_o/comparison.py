"""
Performance comparison of Synchronous, Multithreading,
Multiprocessing, and Asynchronous modes for 500 I/O tasks.
"""
import asyncio
import time
import concurrent.futures
from concurrent.futures.process import BrokenProcessPool
from typing import Any

import requests
import aiohttp


URL = "https://httpbin.org"
NUM_REQUESTS = 500


def sync_mode() -> None:
    """Executes requests one by one (scaled simulation)."""
    print("Starting Synchronous mode (testing 10, estimating 500)...")
    test_count = 10
    start = time.perf_counter()
    try:
        for _ in range(test_count):
            requests.get(URL, timeout=10)
        end = time.perf_counter()
        avg = (end - start) / test_count
        print(f"Sync mode: ~{avg * NUM_REQUESTS:.2f}s (estimated)")
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
        print(f"Network issue during Sync mode: {e}")
    except requests.exceptions.RequestException as e:
        print(f"General requests error: {e}")


def fetch_sync(url: str) -> None|object:
    """
    A named function for pickle compatibility with specific error handling.
    """
    try:
        response = requests.get(url, timeout=15)
        return response.status_code
    except requests.exceptions.ConnectionError:
        print(f"Connection error for {url}")
        return None
    except requests.exceptions.Timeout:
        print(f"Timeout for {url}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request error for {url}: {e}")
        return None


def threading_mode() -> None:
    """Executes requests using a pool of threads."""
    print("\nStarting Multithreading mode (50 workers)...")
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = list(executor.map(fetch_sync, [URL] * NUM_REQUESTS))
    end = time.perf_counter()
    success = len([r for r in results if r == 200])
    print(f"Multithreading: {end - start:.2f}s (Success: {success}/{NUM_REQUESTS})")


def multiprocessing_mode() -> None:
    """Executes requests using multiple CPU cores with error handling."""
    print("\nStarting Multiprocessing mode...")
    start = time.perf_counter()
    try:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = list(executor.map(fetch_sync, [URL] * NUM_REQUESTS))
        end = time.perf_counter()
        success = len([r for r in results if r == 200])
        print(f"Multiprocessing: {end - start:.2f}s (Success: {success}/{NUM_REQUESTS})")
    except BrokenProcessPool:
        print("Critical: Multiprocessing pool is broken. A child process terminated abruptly.")
    except requests.exceptions.RequestException as e:
        print(f"Network error during processing: {e}")
    except OSError as e:
        print(f"System error: Could not create process: {e}")

async def fetch(session: Any, url: str) -> None|object:
    """Asynchronously sends a GET request and returns binary content."""
    try:
        async with session.get(url, timeout=15) as response:
            await response.read()
            return response.status
    except asyncio.TimeoutError:
        print(f"⏱  Timeout error for {url}")
        return None
    except aiohttp.ClientConnectorError as e:
        print(f"Connection error for {url}: {e}")
        return None
    except aiohttp.ClientError as e:
        print(f"HTTP client error for {url}: {e}")
        return None


async def async_mode() -> None:
    """Executes requests concurrently using an event loop."""
    print("\nStarting Asynchronous mode...")
    start = time.perf_counter()
    connector = aiohttp.TCPConnector(limit=100)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [fetch(session, URL) for _ in range(NUM_REQUESTS)]
        results = await asyncio.gather(*tasks)
    end = time.perf_counter()
    success = len([r for r in results if r == 200])
    print(f"Asynchronous: {end - start:.2f}s (Success: {success}/{NUM_REQUESTS})")


if __name__ == "__main__":

    sync_mode()
    threading_mode()
    multiprocessing_mode()
    asyncio.run(async_mode())
