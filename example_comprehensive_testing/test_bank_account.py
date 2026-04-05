"""
Unit tests for the BankAccount class using pytest and mocks.
"""
# pylint: disable=redefined-outer-name
from unittest.mock import Mock
import pytest
from .bank_account import BankAccount


@pytest.fixture
def account():
    """
    Fixture to provide a BankAccount instance with an initial balance of 100.0.
    """
    return BankAccount(balance=100.0)


@pytest.mark.parametrize("deposit_amount, withdraw_amount, expected_balance", [
    (50, 20, 130.0),
    (100, 50, 150.0),
    (0.01, 0.01, 100.0),
])
def test_bank_operations(account: BankAccount, deposit_amount: float,
                         withdraw_amount: float, expected_balance: float) -> None:
    """
    Test combined deposit and withdraw operations with various amounts.
    """
    account.deposit(deposit_amount)
    account.withdraw(withdraw_amount)
    assert account.get_balance() == expected_balance


def test_sync_with_cloud_mock(account: BankAccount) -> None:
    """
    Test cloud synchronization using a mock API client.
    """
    mock_api = Mock()
    mock_api.get_remote_balance.return_value = "success"

    result = account.sync_with_cloud(mock_api)

    assert result is True
    mock_api.get_remote_balance.assert_called_once()


def test_withdraw_skip_if_empty() -> None:
    """
    Test that skips execution if the account balance is zero.
    """
    empty_account = BankAccount(balance=0)

    if empty_account.get_balance() == 0:
        pytest.skip("Рахунок порожній, тестування зняття неможливе")

    empty_account.withdraw(10)
