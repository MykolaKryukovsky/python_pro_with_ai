"""
Module for processing file operations such as reading and writing.
"""
import os


class FileProcessor:
    """
    A utility class to handle basic file system operations.
    """

    @staticmethod
    def write_to_file(file_path: str, data: str) -> None:
        """
        Writes the provided string data to a specified file.
        """
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(data)

    @staticmethod
    def read_from_file(file_path: str) -> str:
        """
        Reads and returns the content of a file. Raises FileNotFoundError if missing.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл {file_path} не знайдено.")
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
