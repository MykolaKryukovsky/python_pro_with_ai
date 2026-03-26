"""Module for managing JSON configuration files using a context manager."""

import json
import os
from typing import Dict, Any


class ConfigManager:
    """Context manager for automatic reading and writing of JSON config files."""

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.data: Dict[str, Any] = {}

    def __enter__(self) -> Dict[str, Any]:

        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as file:
                    self.data = json.load(file)
            except (json.JSONDecodeError, OSError):
                self.data = {}

        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):

        if exc_type is None:
            try:
                with open(self.file_path, 'w', encoding='utf-8') as f:
                    json.dump(self.data, f, indent=4, ensure_ascii=False)
                print(f"Configuration saved to '{self.file_path}'.")
            except OSError as err:
                print(f"Error saving config: {err}")
        else:
            print(f"Changes not saved due to error: {exc_val}")




if __name__ == "__main__":

    CONFIG_FILE = "settings.json"

    with ConfigManager(CONFIG_FILE) as config:

        current_theme = config.get("theme", "light")
        print(f"Current theme: {current_theme}")

        config["theme"] = "dark"
        config["language"] = "uk"
        config["version"] = 1.2

        print("Settings updated in memory...")
