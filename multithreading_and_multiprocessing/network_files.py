"""
Module for multithreaded download of files using sessions.
Demonstrates the work of the threading module and the requests library for
acceleration of network operations (I/O-bound tasks).
"""
import threading
import time
import requests


URL = "https://google.com"


def download_file(session: requests.Session, thread_number: int) -> None:
    """
    Downloads the file at the specified URL and saves it locally.
    Args:
    thread_number (int): Sequence number of the thread used for the file name.
    Returns:
    None
    """
    filename = f"file_{thread_number}"
    print(f"Downloading {thread_number}")

    try:
        response = session.get(URL, timeout=10)
        response.raise_for_status()
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"[{thread_number}] File {filename} downloaded.")
    except requests.exceptions.ConnectionError:
        print(f"[{thread_number}] Error: Connection failed (check your internet).")
    except requests.exceptions.Timeout:
        print(f"[{thread_number}] Error: Timeout reached (server too slow).")
    except requests.exceptions.HTTPError as err:
        print(f"[{thread_number}] HTTP Error occurred: {err}")
    except requests.exceptions.RequestException as e:
        print(f"[{thread_number}] Error request: {e}")


def main():
    """
    Main entry point to initialize session and manage threads.
    """
    with requests.Session() as s:

        threads = []

        start_time = time.time()

        for i in range(1, 11):
            thread = threading.Thread(target=download_file, args=(s, i))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        end_time = time.time()

        print(f"Total time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":

    main()
