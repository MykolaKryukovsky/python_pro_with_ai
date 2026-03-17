"""
Console calculator module.
Provides functionality for basic arithmetic operations.
"""
class  UnknownOperationError(Exception):
    """Exception for unrecognized math operations."""

    def __init__(self, operation, message="Operation not supported"):
        self.operation = operation
        self.message = f"{message}: '{operation}'"
        super().__init__(self.message)


class Calculator:
    """A class for performing calculations and processing user input."""

    def __init__(self) -> None:
        self.operations = {
            '+': self.add, '-': self.sub,
            '*': self.mul, '/': self.truediv
        }

    @staticmethod
    def add(num1: float, num2: float) -> float:
        """Returns the sum of two numbers."""
        return round((num1 + num2), 2)

    @staticmethod
    def sub(num1: float, num2: float) -> float:
        """Returns the difference of two numbers."""
        return round((num1 - num2), 2)

    @staticmethod
    def mul(num1: float, num2: float) -> float:
        """Returns the product of two numbers."""
        return round((num1 * num2), 2)

    @staticmethod
    def truediv(num1: float, num2: float) -> float:
        """Returns the quotient of two numbers with zero check."""
        if num2 == 0:
            raise ZeroDivisionError("Division by zero!")
        return round((num1 / num2), 2)


    def calculate(self) -> None:
        """Starts the user interaction cycle."""

        print("Console calculator (decimal numbers supported) ")
        print("Available operations: +, -, *, / (to exit type 'x')")

        while True:
            try:
                opr = input("Enter operation: ").strip().lower()

                if opr == 'x':
                    break

                if opr not in self.operations:
                    raise UnknownOperationError(opr)

                num1 = float(input("First number: "))
                num2 = float(input("Second number: "))

                result = self.operations[opr](num1, num2)

                print(f"Result: {result}")

            except ValueError as e:
                print(f"Error: The input is not a number: {e}")
            except ZeroDivisionError as e:
                print(f"Error: {e}")
            except UnknownOperationError as e:
                print(f"Error: {e}")
            except OverflowError as e:
                print(f"Error: The result is too large to calculate (overflow): {e}")



if __name__ == "__main__":

    calculator = Calculator()
    calculator.calculate()
