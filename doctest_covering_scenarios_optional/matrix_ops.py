"""
Module for performing matrix operations like multiplication and transposition.
"""
import doctest
from typing import List


def matrix_multiply(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    """
    Множить дві матриці. Кількість стовпців першої має дорівнювати кількості рядків другої.

    Приклади:
    >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]

    Складніший випадок (матриця 2x3 на 3x2):
    >>> matrix_multiply([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    [[58, 64], [139, 154]]

    Множення на нульову матрицю:
    >>> matrix_multiply([[1, 2]], [[0], [0]])
    [[0]]
    """
    if not matrix1 or not matrix2:
        return []

    rows_a = len(matrix1)
    cols_a = len(matrix1[0])
    cols_b = len(matrix2[0])

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Транспонує матрицю (рядки стають стовпцями).

    Приклади:
    >>> transpose_matrix([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]

    Транспонування прямокутної матриці (3x2 -> 2x3):
    >>> transpose_matrix([[1, 2], [3, 4], [5, 6]])
    [[1, 3, 5], [2, 4, 6]]

    Транспонування вектора-рядка:
    >>> transpose_matrix([[1, 2, 3]])
    [[1], [2], [3]]
    """
    return [list(row) for row in zip(*matrix)]


if __name__ == "__main__":

    results = doctest.testmod()

    if results.failed == 0:
        print(f"Усі {results.attempted} тестів пройдено успішно!")
