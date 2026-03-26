"""
Module for filtering web server logs based on HTTP status codes.
Extracts 4XX and 5XX errors using memory-efficient generators.
"""

import os
from typing import Generator

def error_log_generator(file_path: str) -> Generator[int, None, None]:
    """
        Reads a log file line by line and yields lines with 4XX or 5XX status codes.

        :param file_path: Path to the server log file.
        :yield: A single log line representing an error.
        """

    with open(file_path, "r", encoding = "utf-8") as file:
        for line in file:
            parts = line.split()

            for part in parts:
                if part.isdigit() and len(part) == 3:
                    if part.startswith(('4', '5')):
                        yield line.strip()
                        break


def save_errors_to_file(input_log: str, output_log: str) -> None:
    """
        Filters logs and saves error lines to a new file.

        :param input_log: Source log file path.
        :param output_log: Path for the filtered error log.
        """

    errors = error_log_generator(input_log)
    count = 0

    try:
        with open(output_log, "w", encoding = "utf-8") as out_f:
            for error_line in errors:
                out_f.write(str(error_line))
                count += 1

        print(f"Success! {count} error entries saved to '{output_log}'.")

    except OSError as err:
        print(f"File processing error: {err}")



if __name__ == "__main__":

    SOURCE_LOG = "access.log"
    ERROR_REPORT = "error_report.txt"

    if os.path.exists(ERROR_REPORT):
        save_errors_to_file(SOURCE_LOG, ERROR_REPORT)
    else:
        print(f"Error: log file '{SOURCE_LOG}' not found.")
