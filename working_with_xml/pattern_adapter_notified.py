"""
The system module is notified using the Adapter pattern.
"""
# pylint: disable=too-few-public-methods

from abc import ABC, abstractmethod


class MessageSender(ABC):
    """Abstract interface for sending messages."""
    @abstractmethod
    def send_message(self, message: str) -> None:
        """Method for overriding in adapters."""


class SMSService():
    """Third party service for sending SMS."""

    def send_sms(self, phone_number: str, message: str) -> None:
        """Logic of sending SMS with number validation."""

        if not phone_number.startswith("+"):
            raise ValueError("Неверный формат номера")
        print(f"[SMS] Отправка на номер {phone_number}: {message}")


class EmailService():
    """Third-party service for sending Email."""

    def send_email(self, email_address: str, message: str) -> None:
        """Logic of sending Email."""
        print(f"[Email] Отправка на адрес {email_address}: {message}")


class PushService:
    """Third-party service for push-notification."""

    def send_push(self, device_id, message) -> None:
        """Push sending logic."""
        print(f"[Push] Отправка на устройство {device_id}: {message}")


class SMSAdapter(MessageSender):
    """Adapter for SMSService."""

    def __init__(self, service: SMSService, phone_number: str) -> None:
        self.service = service
        self.phone_number = phone_number

    def send_message(self, message: str) -> None:

        self.service.send_sms(self.phone_number, message)


class EmailAdapter(MessageSender):
    """Adapter for EmailService."""

    def __init__(self, service: EmailService, email_address: str) -> None:
        self.service = service
        self.email_address = email_address

    def send_message(self, message: str) -> None:

        self.service.send_email(self.email_address, message)


class PushAdapter(MessageSender):
    """Adapter for PushService."""

    def __init__(self, service: PushService, device_id: str) -> None:
        self.service = service
        self.device_id = device_id

    def send_message(self, message: str) -> None:

        self.service.send_push(self.device_id, message)


class NotificationSystem:
    """Mailing management system."""

    def __init__(self, adapters: list[MessageSender]) -> None:
        self.adapters = adapters

    def send_to_all(self, text: str) -> None:
        """Message distribution through all connected adapters."""

        print(f"\n--- Начало рассылки: '{text}' ---")

        for adapter in self.adapters:
            service_name = adapter.__class__.__name__

            try:
                adapter.send_message(text)
            except (ValueError, RuntimeError) as err:
                print(f"[ОШИБКА] {service_name} не смог отправить: {err}")
            except Exception as err:  # pylint: disable=broad-exception-caught
                print(f"[КРИТИЧЕСКАЯ ОШИБКА] {service_name}: {err}")

        print("--- Рассылка завершена ---\n")
