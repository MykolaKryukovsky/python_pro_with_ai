"""
A module for working with binary numbers and bitwise operations.
"""

class BinaryNumber:
    """
    A class for representing integers with support for bitwise operations.

    Allows you to perform AND, OR, XOR and NOT operations on objects
    class, using the standard operators &, |, ^, ~.
    """

    def __init__(self, value: int) -> None:
        self.value = value

    def __and__(self, other: BinaryNumber) -> BinaryNumber:
        return BinaryNumber(self.value & other.value)

    def __or__(self, other: BinaryNumber) -> BinaryNumber:
        return BinaryNumber(self.value | other.value)

    def __xor__(self, other: BinaryNumber) -> BinaryNumber:
        return BinaryNumber(self.value ^ other.value)

    def __invert__(self) -> BinaryNumber:
        return BinaryNumber(~self.value)

    def __repr__(self) -> str:
        return f"BinaryNumber({self.value} [bin: {bin(self.value)}])"

    def __eq__(self, other: BinaryNumber) -> bool:
        return self.value == other.value




if __name__ == "__main__":

    X, Y = 12, 25

    b1 = BinaryNumber(X)
    b2 = BinaryNumber(Y)

    print(b1)
    print(b2)

    assert (b1 & b2) == BinaryNumber(X & Y)
    assert (b1 | b2) == BinaryNumber(X | Y)
    assert (b1 ^ b2) == BinaryNumber(X ^ Y)
    assert (~b1) == BinaryNumber(~X)
