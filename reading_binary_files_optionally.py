"""Module for memory-efficient binary file reading in chunks."""

import os


def process_binary_file(file_path: str, chunk_size: int = 1024) -> int:
    """
    Reads a binary file in chunks and counts the total bytes processed.

    :param file_path: Path to the binary file.
    :param chunk_size: Number of bytes to read in one iteration.
    :return: Total number of bytes read.
    """

    total_bytes = 0

    try:
        with open(file_path, 'rb') as bin_file:
            while True:
                chunk = bin_file.read(chunk_size)

                if not chunk:
                    break

                total_bytes += len(chunk)

        return total_bytes

    except OSError as err:
        print(f"Error occurred: {err}")
        return 0





if __name__ == "__main__":

    TEST_FILE = "test_data.bin"

    with open(TEST_FILE, "wb") as f:
        f.write(os.urandom(5000))  # 5000 випадкових байтів

    READ_SIZE = 1024
    result = process_binary_file(TEST_FILE, chunk_size = READ_SIZE)

    if result > 0:
        print(f"Successfully processed {result} bytes using {READ_SIZE}-byte chunks.")

    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
