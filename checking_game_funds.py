"""
A module for processing banking transactions and insufficient funds errors.
"""
class InsufficientFundsException(Exception):
    """Exception thrown when attempting to withdraw an amount greater than the balance."""

    def __init__(self, required_amount: float, current_balance: float,
                 currency: str = "UAH", transaction_type: str = "purchase"):
        self.required_amount = required_amount
        self.current_balance = current_balance
        self.currency = currency
        self.transaction_type = transaction_type

        message = (f"Insufficient funds for transaction '{transaction_type}': "
                   f"required {required_amount} {currency}, "
                   f"your balance is {current_balance} {currency}."
        )

        super().__init__(message)


class BankAccount:
    """Custom class for handling bank account information."""

    def __init__(self, owner: str, balance: float, currency: str = "UAH"):
        self.owner = owner
        self.balance = balance
        self.currency = currency

    def deposit(self, amount: float, currency: str = "UAH"):
        """Adds funds to the account balance."""

        self.currency = currency
        self.balance += amount
        print(f"💰 Deposited {amount} {self.currency}. New balance: {self.balance}")

    def process_transaction(self, amount: float, t_type: str):
        """Checks balance and executes transaction or throws exception."""

        print(f"\nTransaction attempt ({t_type}): {amount} {self.currency} ---")

        if amount > self.balance:
            raise InsufficientFundsException(
                required_amount = amount,
                current_balance = self.balance,
                currency = self.currency,
                transaction_type = t_type
            )

        self.balance -= amount
        print(f"✅ Operation successful! New balance: {self.balance} {self.currency}")



if __name__ == "__main__":

    my_account = BankAccount("Sylvester", 1000.0)

    operations = [
        (250.0, "Gold"),
        (1500.0, "Mana"),
        (100.0, "Health")
    ]

    for am, t_tp in operations:
        try:
            my_account.process_transaction(am, t_tp)
        except InsufficientFundsException as e:
            print(f"❌REFUSAL: {e}")
            missing = e.required_amount - e.current_balance
            print(f"Tip: Top up your account with {missing} {e.currency}.")

    my_account.deposit(1500, "UAH")

    am, t_tp = operations[1]

    try:
        my_account.process_transaction(am, t_tp)
    except InsufficientFundsException as e:
        print(f"❌REFUSAL: {e}")
        missing = e.required_amount - e.current_balance
        print(f"Tip: Top up your account with {missing} {e.currency}.")
