"""
Module for working with student data in CSV format.
"""
import  csv

FILENAME = 'students.csv'


def create_csv_file() -> None:
    """Creates an initial data file."""
    data = [
        ['Ім\'я', 'Вік', 'Оцінка'],
        ['Петро', '21', '90'],
        ['Марина', '22', '85'],
        ['Андрей', '20', '88']
    ]

    with open(FILENAME, 'w', encoding = 'utf-8', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

    print(f'File {FILENAME} created.')


def read_csv_file() -> None:
    """Reads data and outputs the average score."""
    scores = []

    with open(FILENAME, 'r', encoding = 'utf-8', newline = '') as csvfile:
        reader = csv.DictReader(csvfile)

        print(",".join(reader.fieldnames))

        for row in reader:

            print(f'{row["Ім\'я"]},{row["Вік"]},{row["Оцінка"]}')

            scores.append(int(row['Оцінка']))

    if scores:
        average = sum(scores) / len(scores)

        print(f'Середня оцінка студентів: {average:.1f}')


def add_student(name: str, age: str, score: str) -> None:
    """Adds a student to the database."""
    with open(FILENAME, 'a', encoding = 'utf-8', newline ='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, age, score])

    print(f"Студента {name} додано до списку.")


if __name__ == '__main__':

    create_csv_file()
    read_csv_file()
    add_student('Таня', 23, '95')
    read_csv_file()
