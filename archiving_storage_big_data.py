"""Module for managing ZIP archives using a custom context manager."""

import zipfile
import os
from typing import Optional, Type

class ZipManager:
    """Context manager for creating and adding files to a ZIP archive."""

    __slots__ = ('archive_path', 'zip_file')

    def __init__(self, archive_path: str) -> None:
        self.archive_path = archive_path
        self.zip_file: Optional[zipfile.ZipFile] = None

    def __enter__(self) -> zipfile.ZipFile:
        self.zip_file = zipfile.ZipFile(self.archive_path,
                mode="r", compression=zipfile.ZIP_DEFLATED
        )

        return self.zip_file

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[object]
    ) -> bool:

        if self.zip_file:
            self.zip_file.close()
            print(f"Archive '{self.archive_path}' closed successfully.")

        return False



if __name__ == "__main__":

    ARCHIVE_NAME = "my_files.zip"
    FILES_TO_ADD = ["test_file.txt", "data.json"]

    for name in FILES_TO_ADD:
        with open(name, "w", encoding="utf-8") as file:
            file.write(f"Contents of {name}\n")
        try:
            with ZipManager(ARCHIVE_NAME) as archive:
                for file in FILES_TO_ADD:
                    if os.path.exists(file):
                        archive.write(file)
                        print(f"Added file '{file}' to archive.")
                    else:
                        print(f"File '{file}' does not exist.")

        except OSError as err:
            print(f"Archive error: {err}")
