"""
Program for calculation of average arithmetic numbers from a file.
"""
class FileEmpty(Exception):
    """" Raised when the file is empty."""
    def __init__(self, message = 'File was empty'):
        self.message = message
        super().__init__(self.message)


def calculate_average(filename: str):
    """Reads numbers from a file and displays their average value."""

    try:
        with open(filename, 'r', encoding='utf8') as file:

            lines = file.readlines()

            numbers = []

            if not lines:
                raise FileEmpty()

            for line in lines:
                line = line.strip()
                if line:
                    numbers.append(float(line))

            if not numbers:
                raise ZeroDivisionError("Error: There is no numeric data in the file.")

            average = sum(numbers) / len(numbers)

            print(f"Read lines: {len(numbers)} \nNumbers: {numbers}")

            if len(numbers) == 1:
                print("Only one number in the file. The average the number itself.")

            print(f"Arithmetic average: {average:.2f}")

    except FileNotFoundError:
        print(f"Error: File at '{filename}' not found.")
    except ValueError:
        print("Error: The file contains non-numeric data or is damaged.")



if __name__ == '__main__':

    calculate_average('numbers.txt')
