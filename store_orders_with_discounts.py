"""
Module for calculating orders
with promotional and VIP discounts.
"""
DISCOUNT = 0.1

def create_order(price: float, is_vip: bool = False) -> float:
    """
    Calculates the price with a standard discount
    and allows you to apply a VIP discount.
    """

    final_price = price * (1 - DISCOUNT)
    print(f"Price after standard discount: {round(final_price, 2)}")

    def apply_additional_discount(vip_discount: float) -> None:
        """
        Adds an additional discount by changing
        a variable in an external function.
        """

        nonlocal final_price

        final_price = final_price * (1 - vip_discount)
        print("VIP discount applied ")

    if is_vip:
        apply_additional_discount(DISCOUNT)
    else:
        print("VIP discount not applied ")

    print(f"Final price to be paid: {round(final_price, 2)}")
    return round(final_price, 2)


if __name__ == "__main__":

    product_price = float(input("Enter product price: "))

    create_order(product_price, is_vip=False)

    create_order(product_price, is_vip=True)
