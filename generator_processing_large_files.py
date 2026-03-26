"""
Module for memory-efficient text file filtering using generators.
This script scans large files for a keyword and saves matches to a new file.
"""
import os
from typing import Generator


def get_filtered_lines(file_path: str, keyword: str) -> Generator[str, None, None]:
    """
    Reads a file line by line and yields lines containing the keyword.

    :param file_path: Path to the source text file.
    :param keyword: The string to search for within each line.
    :yield: Cleaned string containing the keyword.
    """
    with open(file_path, mode='r', encoding='utf-8') as file:
        for line in file:
            if keyword in line:
                yield line.strip()


def save_matches(input_path: str, output_path: str, keyword: str) -> None:
    """
    Processes the filtered lines and writes them to the destination file.

    :param input_path: Path to the large log file.
    :param output_path: Path where filtered results will be stored.
    :param keyword: The keyword to filter by.
    """
    line_generator = get_filtered_lines(input_path, keyword)
    match_count = 0

    try:
        with open(output_path, mode='w', encoding='utf-8') as out_file:
            for match in line_generator:
                out_file.write(f"{match}\n")
                match_count += 1

        print(f"Success! {match_count} matches saved to '{output_path}'.")

    except PermissionError:
        print(f"Error: Permission denied when writing to '{output_path}'.")
    except OSError as err:
        print(f"System error occurred: {err}")


if __name__ == "__main__":

    LOG_FILE = "server.log"
    RESULT_FILE = "filtered_results.txt"
    SEARCH_TERM = "ERROR"

    if os.path.exists(LOG_FILE):
        save_matches(LOG_FILE, RESULT_FILE, SEARCH_TERM)
    else:
        print(f"Error: Source file '{LOG_FILE}' not found.")
