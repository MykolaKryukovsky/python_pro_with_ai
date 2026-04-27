"""
This module demonstrates asynchronous HTTP requests using the aiohttp library.
It fetches content from multiple URLs concurrently and handles potential errors.
"""
import asyncio
import aiohttp


async def fetch_content(url: str, session: aiohttp.ClientSession) -> str:
    """
    Asynchronously sends an HTTP GET request to the specified URL.
    Args:
    session (aiohttp.ClientSession): The active session to use for the request.
    url (str): The URL to fetch.
    Returns:
    str: The page content or an error message if the request fails.
    """
    try:
        async with session.get(url, timeout=10) as response:
            if response.status == 200:
                counter = await response.text()
                return f"Successfully fetched content from {url} ({counter})"
            return f"Error fetching {url}: Status code: {response.status}"
    except aiohttp.ClientConnectorError:
        return f"Error connecting to {url}"
    except asyncio.TimeoutError:
        return f"Timeout connecting to {url}"


async def fetch_all(urls: list) -> list:
    """
    Downloads content from a list of URLs concurrently
    Args:
    urls (list): A list of URL strings.
    Returns:
    list: A list of responses or error messages.
    """
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_content(url, session) for url in urls]
        results = await asyncio.gather(*tasks)

        return results


async def main():
    """Entry point for the script."""
    urls = [
        "https://google.com",
        "https://python.org",
        "https://github.com",
        "https://invalid-url-test.com",
    ]
    print("Starting parallel fetch...")
    results = await fetch_all(urls)

    for res in results:
        print(res)


if __name__ == "__main__":

    asyncio.run(main())
