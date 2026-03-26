"""Module for memory-efficient running average calculation using generators."""

from typing import Generator


def running_average_generator(file_path: str) -> Generator[float, None, None]:
    """
    Reads numbers from a file one by one and yields the current average.

    :param file_path: Path to the file containing numeric data (one per line).
    :yield: The calculated average up to the current element.
    """

    total_sum = 0.0
    count = 0

    try:
        with open(file_path, mode="r", encoding = 'utf-8') as file:
            for line in file:
                clean_line = line.strip()
                if  not clean_line:
                    continue

                try:
                    value = float(clean_line)
                    total_sum += value
                    count += 1
                    yield total_sum / count
                except ValueError:
                    continue

    except OSError as err:
        print(f"File error: {err}")




if __name__ == "__main__":

    DATA_FILE = "performance_metrics.txt"

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write("10.5\n20.0\n30.5\n\n40.0")

    averages = running_average_generator(DATA_FILE)

    print(f"{'Value Index':<12} | {'Current Average':>15}")
    print("-" * 30)

    for i, avg in enumerate(averages, 1):
        print(f"{i:<12} | {avg:>15.2f}")
