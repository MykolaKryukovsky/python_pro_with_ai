"""
Module for managing user data.
"""


class UserManager:
    """"A class for managing users"""

    def __init__(self) -> None:
        self.users = []

    def add_user(self, name: str, age: int) -> None:
        """
        Add a new user with a name and age to the list.
        """
        self.users.append({"name": name, "age": age})

    def remove_user(self, name: str) -> None:
        """
        Remove all users with the specified name from the list.
        """
        self.users = [u for u in self.users if u ["name"] != name]

    def get_all_users(self) -> list:
        """
        Return the full list of currently stored users.
        """
        return self.users
