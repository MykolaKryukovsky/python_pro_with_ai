"""
A module for managing user subscriptions.
"""
from zmq import SUBSCRIBE

subscribers = []

def subscribe(subscriber: str) -> None:
    """Adds the customer to the list of subscribers and confirms the action."""
    subscribers.append(subscriber)

    def confirm_subscription() -> None:
        """Displays a message about a successful subscription."""
        if subscriber in subscribers:
            print(f"Підписка підтверджена для {subscriber} ")

    confirm_subscription()


def unsubscribe(subscriber: str) -> None:
    """Removes the user from the subscriber list, if they are there."""
    if subscriber in subscribers:
        subscribers.remove(subscriber)
        print(f"{subscriber} успішно відписаний(на) ")
    else:
        print(f"{subscriber} не мав(ла) підписки ")


if __name__ == "__main__":

    name1 = input("Введіть ім'я щоб отримати підписку: ")
    subscribe(name1)

    name2 = input("Введіть ім'я щоб отримати підписку: ")
    subscribe(name2)

    print(f"Поточні підписники: {subscribers}")

    name3 = input("Введіть ім'я щоб відмінити підписку: ")

    unsubscribe(name3)
    print(f"Список після відписки: {subscribers}")
