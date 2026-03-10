"""
Module for managing store products using currying.
"""
from collections.abc import Callable

def create_product(name: str, quantity: int) -> Callable[[float], str]:
    """
    Creates a product and returns a function to set its price.

    :param name: Product name.
    :param quantity: Quantity.
    :return: Function that takes a price and returns a description of the product.
    """

    def set_price(price: float) -> str:
        """Sets the price for a previously created product."""

        total_cost = price * quantity

        return (f"Product: {name} | Price per piece: {price:.2f} | "
                f"Quantity: {quantity} | Total cost: {total_cost:.2f}")

    return set_price


if __name__ == "__main__":

    computer = create_product("Artline Gaming A21", 10)
    smartphone = create_product("Samsung Galaxy S25 Ultra", 20)

    print(computer(150000))
    print(smartphone(60000))
