"""Module for safe file processing with automatic backup and rollback."""
import os
import shutil


class SafeFileProcessor:
    """
        Context manager that creates a backup before processing.
        Rolls back to the original file if an error occurs.
    """

    __slots__ = ('file_path', 'backup_path')

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.backup_path = f"{file_path}.bak"

    def __enter__(self) -> str:

        if os.path.exists(self.file_path):
            shutil.copy(self.file_path, self.backup_path)

        return self.file_path

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:

        if exc_type is None:

            if os.path.exists(self.backup_path):
                os.remove(self.backup_path)
            print("Processing successful. Backup removed.")
            return True

        if os.path.exists(self.backup_path):

            shutil.move(self.backup_path, self.file_path)
            print(f"Error occurred: {exc_val}. File restored from backup.")

        return False


if __name__ == "__main__":

    TARGET_FILE = "important_data.txt"

    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write("Original secret data")
    try:
        with SafeFileProcessor(TARGET_FILE) as path:
            print(f"Processing {path}...")
            with open(path, "a", encoding="utf-8") as f:
                f.write("\nNew experimental data")
    except (ValueError, OSError) as err:
        print(f"Main loop caught: {err}")
