"""
Module for parallel downloading and image processing.
This script uses multiprocessing to load images simultaneously
through requests, applies the Pillow filter to them and saves the result.
Installation request: pip install requests Pillow
"""
import multiprocessing
import time
from io import BytesIO

import requests
from PIL import Image, ImageFilter


URLS = [
    "https://wallpaper.forfun.com/fetch/80/801085d444e6ae0c940cdcf061a24e73.jpeg",
    "https://wallpaper.forfun.com/"
    "fetch/b7/b7c2da33f42132b88e6d16e0ff6157d7.jpeg?w=1470&r=0.5625&f=webp",
    "https://wallpaper.forfun.com/"
    "fetch/b3/b3278a9304f88423e4cb2cdf863f2daf.jpeg?w=1470&r=0.5625&f=webp",
    "https://wallpaper.forfun.com/"
    "fetch/b9/b9cfd6f52a3278e2b3deaf98f8428938.jpeg?w=1470&r=0.5625&f=webp",
    "https://wallpaper.forfun.com/"
    "fetch/4a/4aabc9ed923539986e1e3f938f62751b.jpeg?w=1470&r=0.5625&f=webp",
    "https://wallpaper.forfun.com/"
    "fetch/5d/5d7ddab80051a404b0a1f23271556b5a.jpeg?w=1470&r=0.5625&f=webp"
]


def download_and_process(url: str) -> str:
    """
    Downloads the image from the link, applies a filter and saves it to disk.
    Args:
    url (str): Link to the image.
    Returns:
    str: Operation result message or error text.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img = img.filter(ImageFilter.DETAIL)
        img_id = url.split('/')[-3]
        filename = f'./{img_id}.jpg'
        img.save(filename)

        return f"Saved: image_{filename}"
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred {url}: {http_err}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"Connection error occurred {url}: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"Timeout error occurred {url}: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"Other error occurred {url}: {req_err}"


def main():
    """
    The main point of entry into the program.
    Initializes the process pool, distributes tasks by download
    and processed images, as well as displays the final report.
    """
    print(f"Downloading {len(URLS)} images")
    start_time = time.perf_counter()

    with multiprocessing.Pool() as pool:
        results = pool.map(download_and_process, URLS)
    for result in results:
        print(result)

    end_time = time.perf_counter()
    print(f"Total time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":

    main()
