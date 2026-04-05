"""
Module for managing bank account operations and cloud synchronization.
"""
from typing import Any


class BankAccount:
    """
    A class representing a bank account with basic financial operations.
    """

    def __init__(self, balance: float) -> None:
        self.balance = balance


    def deposit(self, amount: float) -> None:
        """
        Add a positive amount to the account balance.
        """
        if amount <= 0:
            raise ValueError("The top-up amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Deduct an amount from the balance. Raises OverflowError if insufficient funds.
        """
        if amount > self.balance:
            raise OverflowError("Not enough money in the account")
        self.balance -= amount

    def get_balance(self) -> float:
        """
        Return the current account balance.
        """
        return self.balance

    def sync_with_cloud(self, api_client: Any) -> bool:
        """
        Synchronize the account status with a remote cloud service.
        """
        response = api_client.get_remote_balance()

        if response == "success":
            return True
        return False
