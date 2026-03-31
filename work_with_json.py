"""
A module for creating and storing book data in JSON format.
"""
import json
import os

FILENAME = 'books.json'


def create_books_json() -> None:
    """Creates a list of books and saves it to a JSON file."""

    books = [
        {
            "назва": "Кобзар",
            "автор": "Тарас Шевченко",
            "рік_видання": 1840,
            "наявність": True
        },
        {
            "назва": "1984",
            "автор": "Джордж Орвелл",
            "рік_видання": 1949,
            "наявність": False
        },
        {
            "назва": "Маленький принц",
            "автор": "Антуан де Сент-Екзюпері",
            "рік_видання": 1943,
            "наявність": True
        }
    ]

    with open(FILENAME, 'w', encoding='utf-8') as f:

        json.dump(books, f, indent=4, ensure_ascii=False)

    print(f"Файл {FILENAME} успішно створено.")


def load_books() -> list:
    """
    Loads a list of books from a file.
    If the file does not exist, returns an empty list.
    """

    if not os.path.exists(FILENAME):
        return []

    with open(FILENAME, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_books(books: list) -> None:
    """Saves a list of books to a file."""

    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(books, f, indent=4, ensure_ascii=False)


def show_available_books() -> None:
    """Only prints books that are available to the terminal."""

    books = load_books()

    print("Доступні книги (наявність: True)")

    available = [b for b in books if b.get('наявність') is True]

    if not available:
        print("На жаль, доступних книг немає.")

    for book in available:
        print(f" '{book['назва']}' — {book['автор']} ({book['рік_видання']})")


def add_new_book(title: str, author: str, year: str, is_available: bool) -> None:
    """Adds a new book to the JSON file."""

    books = load_books()

    new_book = {
        "назва": title,
        "автор": author,
        "рік_видання": year,
        "наявність": is_available
    }

    books.append(new_book)

    save_books(books)

    print(f"Книгу '{title}' успішно додано!")


if __name__ == "__main__":

    create_books_json()

    show_available_books()

    add_new_book("Відьмак", "Анджей Сапковський", 1986, True)

    show_available_books()
