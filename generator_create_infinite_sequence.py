"""
Module for generating infinite even numbers and saving them to a file.
Demonstrates generators and context managers.
"""

from typing import Generator

def infinite_even_generator() -> Generator[int, None, None]:
    """Infinite generator that yields even numbers starting from 0."""

    number = 0

    while True:

        yield number
        number += 2


def save_even_numbers(file_path: str, limit: int = 100) -> None:
    """
        Saves a limited sequence of even numbers to a text file.

        :param file_path: Path to the output file.
        :param limit: How many numbers to generate before stopping.
        """

    evens = infinite_even_generator()
    count = 0

    try:
        with open(file_path, 'w', encoding = 'utf-8') as file:
            for even_num in evens:
                if count >= limit:
                    break

                file.write(str(even_num))
                count += 1

        print(f"Success! {count} even numbers saved to '{file_path}'.")

    except OSError as err:
        print(f"File error: {err}")



if __name__ == "__main__":
    RESULT_FILE = "even_numbers.txt"
    MAX_COUNT = 100

    save_even_numbers(RESULT_FILE, MAX_COUNT)
