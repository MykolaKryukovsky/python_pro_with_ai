"""
A module for working with user data and email validation.
"""
import re

class User:
    """
    Represents a system user with data validation.
    """

    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    @property
    def first_name(self) -> str:
        """Returns the first name of the user."""

        return f"{self.__first_name}"

    @first_name.setter
    def first_name(self, f_name: str) -> None:
        """Sets the first name, cleaning it from extra spaces."""

        if not f_name.strip():
            raise ValueError("Surname cannot be empty!")

        self.__first_name = f_name

    @property
    def last_name(self) -> str:
        """Returns the last name of the user."""

        return f"{self.__last_name}"

    @last_name.setter
    def last_name(self, l_name: str) -> None:
        """Sets the last name, cleaning it from extra spaces."""

        if not l_name.strip():
            raise ValueError("Name cannot be empty!")

        self.__last_name = l_name

    @property
    def email(self) -> str:
        """Returns the email address."""

        return f"{self.__email}"

    @staticmethod
    def is_valid_email(mail: str) -> bool:
        """
        Checks the format of an email address using a regular expression.

        Arguments:
        mail (str): A string with a postal address.

        Returns:
        bool: True if the format is correct, otherwise False.
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, mail))

    @email.setter
    def email(self, mail: str) -> None:
        """Sets up email with pre-validation."""

        if not self.is_valid_email(mail):
            raise ValueError(f"Invalid email address {mail}")

        self.__email = mail

    def __repr__(self) -> str:
        return f"User: {self.first_name} {self.last_name} {self.email}"



if __name__ == "__main__":

    user = User("Arnold", "Schwarzenegger", "arnoschwarz@gmail.com")

    print(user)
    print(user.first_name)
    print(user.last_name)
    print(user.email)
