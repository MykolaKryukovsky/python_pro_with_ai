"""
A script for capturing the content of a web site and saving files.
"""
import requests
from bs4 import BeautifulSoup


def save_page_to_file(url: str, filename: str) -> None:
    """
    It searches for the URL instead of the page and writes it to the file.
    """
    try:
        response = requests.get(url, timeout = 10)

        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        for script_or_style in soup(["script", "style", "header", "footer", "nav"]):
            script_or_style.decompose()

        clean_text = soup.get_text(separator = '\n')

        lines = [line.strip() for line in clean_text.splitlines() if line.strip()]
        final_content = "\n".join(lines)

        with open(filename, 'w', encoding = "utf-8") as f:
            f.write(final_content)

    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Comment: Turn over the Internet or make sure the URL is correct.")
    except requests.exceptions.Timeout:
        print("Recovery hour has expired.")
    except Exception as err: # pylint: disable=broad-exception-caught
        print(f"Another error occurred:: {err}")


if __name__ == "__main__":

    TARGET_URL = "https://www.google.com"
    OUTPUT_FILE = "content.txt"

    save_page_to_file(TARGET_URL, OUTPUT_FILE)
