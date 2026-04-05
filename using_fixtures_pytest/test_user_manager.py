"""
Unit tests for the UserManager class.
"""
# pylint: disable=redefined-outer-name
import pytest
from .user_manager import UserManager


@pytest.fixture()
def user_manager():
    """
    Fixture that provides a UserManager instance with two pre-registered users.
    """
    um = UserManager()
    um.add_user('Alice', 25)
    um.add_user('Bob', 40)

    return um

def test_add_user(user_manager):
    """
    Test adding a new user to the manager.
    """
    user_manager.add_user('Chack', 35)
    users = user_manager.get_all_users()

    assert len(users) == 3
    assert users[-1]['name'] == 'Chack'

def test_get_remove_user(user_manager):
    """
    Test removing a user by their name.
    """
    user_manager.remove_user('Alice')
    users = user_manager.get_all_users()

    assert len(users) == 1
    assert users[0]['name'] == 'Bob'

def test_get_all_users(user_manager):
    """
    Test retrieving the list of all registered users.
    """
    users = user_manager.get_all_users()

    assert len(users) == 2
    assert users[0]['name'] == 'Alice'
    assert users[1]['name'] == 'Bob'

def test_skip_if_few_users(user_manager):
    """
    Test that skips if the number of users is less than three.
    """
    users_count = len(user_manager.get_all_users())

    if users_count < 3:
        pytest.skip(f"Skip: {users_count} total users, minimum 3 required")

    assert "Alice" in [u['name'] for u in user_manager.get_all_users()]
