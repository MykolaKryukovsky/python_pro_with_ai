"""
Module for handling product prices with rounding and arithmetic operations.
"""

class Price:
    """Represents a price with two decimal places precision."""

    def __init__(self, cost: float, ) -> None:
        self.cost = round(float(cost), 2)

    @classmethod
    def from_float(cls, cost: float) -> Price:
        """Alternative constructor to create Price from a float."""
        return cls(cost)


    @property
    def price(self) -> float:
        """Getter for the cost."""
        return round(float(self.cost), 2)

    @price.setter
    def price(self, cost: float) -> None:
        if cost < 0:
            raise ValueError("Price cannot be negative")
        self.cost = cost

    def __add__(self, other: Price) -> Price:
        return Price(self.cost + other.cost)

    def __sub__(self, other: Price) -> Price:
        result = self.cost - other.cost
        return Price(max(0.0, result))

    def __eq__(self, other: Price) -> bool:
        return self.cost == other.cost

    def __gt__(self, other: Price) -> bool:
        return self.cost > other.cost

    def __lt__(self, other: Price) -> bool:
        return self.cost < other.cost

    def __repr__(self) -> str:
        return f"Price({self.cost:.2f})"



class PaymentGateway:
    """
      Service for processing financial transactions using Price objects.
      """

    def __init__(self, balance: Price) -> None:
        self.balance = balance

    def process_payment(self, amount: Price) -> bool:
        """
        Deducts amount from balance if funds are sufficient.
        """

        if self.balance < amount:
            print(f"Payment failed: Insufficient funds. Balance: {self.balance}")
            return False

        self.balance = self.balance - amount

        print(f"Payment successful! Remaining balance: {self.balance}")

        return True


if __name__ == "__main__":

    wallet = PaymentGateway(Price(1000.00))

    affordable_price = Price.from_float(800.50)
    wallet.process_payment(affordable_price)

    expensive_price = Price(350.00)
    wallet.process_payment(expensive_price)
