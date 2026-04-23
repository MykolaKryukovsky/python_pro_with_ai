"""
A module for parallel calculation of the sum of numbers.
Breaks a large range of numbers into parts and calculates the sum
each part in a separate process to speed up work.
"""
import multiprocessing
import time
from typing import List


def sum_chunk(numbers: List[int]) -> int:
    """
    Calculates the sum of the transferred list of numbers.
    Args:
    numbers (List[int]): List of integers.
    Returns:
    int: Sum of numbers.
    """
    return sum(numbers)


def main():
    """
    Main entry point of the script.
    Generates data, splits it into chunks, and processes them in parallel.
    """
    count = 10_000_000
    data = list(range(1, count + 1))

    num_processes = multiprocessing.cpu_count()

    chunk_size = len(data) // num_processes

    chunks = [
        data[i: i + chunk_size]
        for i in range(0, len(data), chunk_size)
    ]

    print(f"Summing {count} numbers using {num_processes} cores...")
    start_time = time.perf_counter()

    with multiprocessing.Pool(processes=num_processes) as pool:
        partial_sums = pool.map(sum_chunk, chunks)

    total_sum = sum(partial_sums)

    end_time = time.perf_counter()

    print(f"Result: {total_sum}")
    print(f"Execution time: {end_time - start_time:.2f} seconds.")


if __name__ == "__main__":

    main()
