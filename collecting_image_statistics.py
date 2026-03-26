"""Module for extracting metadata from images in a catalog."""
import os
import csv

from PIL import Image

class ImageScanner:
    """Class for extracting metadata from images in a catalog."""

    __slots__ = ('folder', 'scanner_iterator')

    def __init__(self, folder_path):
        self.folder = folder_path
        self.scanner_iterator = os.scandir(folder_path)

    def __iter__(self):
        return self

    def __next__(self):
        for item in self.scanner_iterator:
            if item.is_file() and item.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                try:
                    with Image.open(item.path) as img:
                        return {
                            "name": item.name,
                            "width": img.width,
                            "height": img.height,
                            "format": img.format,
                        }

                except (IOError, SyntaxError) as err:
                    print(f"Пропущен поврежденный файл {item.name}: {err}")
                    continue

        raise StopIteration


def run_metadata_collector(target_folder, output_csv):
    """
    Reads image metadata from the folder and saves them to a CSV file.

    :param target_folder: The path to the image folder.
    :param output_csv: Name or path to the resulting CSV file.
    """

    scanner = ImageScanner(target_folder)

    columns = ["name", "width", "height", "format"]
    count = 0

    try:
        with open(output_csv, 'w', newline='', encoding="utf") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=columns)

            writer.writeheader()

            for image_info in scanner:
                writer.writerow(image_info)
                count += 1
                print(f"[{count}] Added to the report: {image_info['name']}")

        print(f"\nDone! All processed images: {count}")

    except PermissionError:
        print(f"Access error: The file '{output_csv}' is open in another program.")
    except OSError as err:
        print(f"System error when working with file: {err}")



if __name__ == "__main__":

    PHOTOS = "images_folder"
    RESULT_FILE = "report.csv"

    if os.path.exists(PHOTOS):
        run_metadata_collector(PHOTOS, RESULT_FILE)
        print("Done! Check the file report.csv")
    else:
        print(f"Folder '{PHOTOS}' not found.")
