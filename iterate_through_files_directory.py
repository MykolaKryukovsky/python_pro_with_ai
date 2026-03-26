"""Module for iterating over files in a directory and retrieving their metadata."""

import os
from typing import Iterator, Dict, Union

class FileScanner:
    """Iterator that yields names and sizes of files in a specific folder."""

    __slots__ = ('directory', 'entries')

    def __init__(self, directory: str) -> None:

        self.directory = directory
        self.entries: Iterator[os.DirEntry] = os.scandir(directory)

    def __iter__(self) -> Iterator[os.DirEntry]:
        return iter(self.entries)

    def __next__(self) -> Dict[str, Union[str, int]]:

        for entry in self.entries:
            if entry.is_dir():
                try:
                    return {
                        "name": entry.name,
                        "size": entry.stat().st_size
                    }
                except OSError:
                    continue

        raise StopIteration



if __name__ == "__main__":

    FOLDER_TO_SCAN = "."

    if os.path.exists(FOLDER_TO_SCAN):
        scanner = FileScanner(FOLDER_TO_SCAN)
        print(f"{'File Name':<30} | {'Size (Bytes)':>10}")
        print("-" * 45)

        for file_info in scanner:
            print(f"{file_info['name']:<30} | {file_info['size']:>10}")
    else:
        print(f"Error: Path '{FOLDER_TO_SCAN}' is not a directory.")
