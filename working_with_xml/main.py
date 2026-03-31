"""
Main entry point for the product management and notification system.
This script demonstrates the usage of adapters and data conversion modules.
"""
# pylint: disable=import-error

import format_conversion_csv_json_xml
import information_store_products
import pattern_adapter_notified


sms_service = pattern_adapter_notified.SMSService()
email_service = pattern_adapter_notified.EmailService()
push_service = pattern_adapter_notified.PushService()

sms_adapter = pattern_adapter_notified.SMSAdapter(sms_service, "+380123456789")
email_adapter = pattern_adapter_notified.EmailAdapter(email_service, "user@example.com")
push_adapter = pattern_adapter_notified.PushAdapter(push_service, "device123")

MESSAGE = "Привіт! Це тестове повідомлення."

sms_adapter.send_message(MESSAGE)
email_adapter.send_message(MESSAGE)
push_adapter.send_message(MESSAGE)

information_store_products.create_products_xml()
information_store_products.update_product_quantity("products.xml", "Молоко", 55)

format_conversion_csv_json_xml.DataConverter.xml_to_json("products.xml", "products2.json")
