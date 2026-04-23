"""
Parallel calculation of factorial of large numbers.
Distributes range of numbers between processes to speed up calculations.
"""
import multiprocessing
import functools
import time
import sys
import math
from typing import List, Tuple, Generator, Callable, Any


sys.set_int_max_str_digits(0)


def log_computation(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator for measuring the computation time of each section."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end: float = time.time()
        print(f"[LOG] Секція {args[0]} обчислена за {end - start:.4f} сек.")
        return result

    return wrapper


class FactorialCalculator:
    """Class for parallel factorial calculation via OOP."""

    def __init__(self, n: int, num_processes: int = 10) -> None:
        self.n = n
        self.num_processes = num_processes

    def get_info(self) -> str:
        """Returns info about the current task."""
        return f"Task: {self.n}!, Processes: {self.num_processes}"

    @staticmethod
    @log_computation
    def multiply_range(range_tuple: Tuple[int, int]) -> int:
        """Calculates the product of numbers in the given range [start, end]."""
        start, end = range_tuple
        result = 1
        for i in range(start, end + 1):
            result *= i
        return result

    def format_scientific(self, large_number: int) -> str:
        """
        Converts a giant number to scientific notation (mantissa * 10^exponent).
        Using logarithms to avoid OverflowError with floats.
        """
        if large_number == 0:
            return "0"

        log_n = math.log10(large_number)
        exponent = int(log_n)
        mantissa = 10 ** (log_n - exponent)

        return f"{mantissa:.4f} * 10^{exponent}"

    def get_ranges_gen(self) -> Generator[Tuple[int, int], None, None]:
        """A generator that divides n into equal ranges for processes."""
        step = self.n // self.num_processes

        ranges = [
            (i * step + 1, (i + 1) * step if i < self.num_processes - 1 else self.n)
            for i in range(self.num_processes)
            if (i * step + 1) <= ((i + 1) * step if i < self.num_processes - 1 else self.n)
        ]
        yield from ranges

    def compute(self) -> int:
        """Starts parallel computing."""
        ranges: List[Tuple[int, int]] = list(self.get_ranges_gen())

        print(f"Обчислення {self.n}! на {len(ranges)} процесах...")

        with multiprocessing.Pool(processes=self.num_processes) as pool:
            partial_results: List[int] = pool.map(self.multiply_range, ranges)

        print("Збирання фінального результату...")
        final_result: int = functools.reduce(lambda x, y: x * y, partial_results)
        return final_result


if __name__ == "__main__":

    NUMBER = 50000
    PROCESSES = 10

    calculator = FactorialCalculator(NUMBER, PROCESSES)

    start_time = time.time()
    total_factorial = calculator.compute()
    end_time = time.time()

    print(f"\nОбчислення завершено за {end_time - start_time:.2f} сек.")
    print(f"Результат (наукова нотація): {calculator.format_scientific(total_factorial)}")
    print(f"Кількість цифр у результаті: {len(str(total_factorial))}")
