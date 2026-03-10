"""
Модуль для демонстрації перекриття областей видимості (LEGB).
Цей скрипт демонструє різницю між вбудованими та локальними функціями.

ВІДПОВІДЬ НА ПЕРШЕ ЗАПИТАННЯ:
Діє правило пошуку імен LEGB (Local -> Enclosing -> Global -> Built-in)
коли для нової функції використовується імья що вже існує в built-in області,
то Python знаходить нову функцію раніше (в Global, Enclosing або Local області) і використовує її.
Вбудована функція стає "затіненою" (shadowed).

ВІДПОВІДЬ НА ДРУГЕ ЗАПИТАННЯ:
Для цього потрібно явно звернутися до модуля builtins,
де зберігаються всі стандартні функції Python.
"""

import builtins


def sum() -> None:
    """
    gave the function a name
    that is already reserved in Python for built-in functions
    :return: None
    """
    print("This is my custom sum function!")



if __name__ == "__main__":

    numbers = [2, 4, 6, 8, 10]

    my_sum = sum

    print(builtins.sum(numbers))
    my_sum()
    print(builtins.sum(numbers))
