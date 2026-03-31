"""
A module for creating an XML file with product data.
"""
import xml.etree.ElementTree as ET
import os


def create_products_xml():
    """Creates an XML file with a predefined list of products."""

    shop = ET.Element("shop")

    products_data = [
        {"name": "Хліб", "price": "25", "quantity": "50"},
        {"name": "Молоко", "price": "40", "quantity": "30"},
        {"name": "Яблука", "price": "35", "quantity": "100"}
    ]

    for item in products_data:
        product = ET.SubElement(shop, "product")
        name = ET.SubElement(product, "name")
        name.text = item["name"]
        price = ET.SubElement(product, "price")
        price.text = item["price"]
        quantity = ET.SubElement(product, "quantity")
        quantity.text = item["quantity"]

        tree = ET.ElementTree(shop)
        ET.indent(tree, space="    ", level=0)

        try:
            with open("products.xml", "wb") as f:
                tree.write(f, encoding="utf-8", xml_declaration=True)
            print("Файл products.xml успішно створено.")
        except PermissionError:
            print("Ошибка: Не удалось создать файл. Доступ запрещен.")


def update_product_quantity(file_name, target_name, new_quantity):
    """
    Reads XML, displays a list of products,
    changes the quantity of one of them and saves.
    """

    try:
        val_qty = int(new_quantity)
        if val_qty < 0:
            print("Ошибка: Количество не может быть отрицательным.")
            return
    except ValueError:
        print(f"Ошибка: '{new_quantity}' не является числом.")
        return

    if not os.path.exists(file_name):
        print(f"Ошибка: Файл {file_name} не найден.")
        return

    try:
        tree = ET.parse(file_name)
        root = tree.getroot()

        print("--- Текущий список товаров ---")
        found = False

        for product in root.findall("product"):
            name = product.find("name")
            quantity = product.find("quantity")

            if name is not None and quantity is not None:
                name = name.text
                quantity = quantity.text
                print(f"Товар: {name:10} | Количество: {quantity}")

            if name == target_name:
                product.find("quantity").text = str(new_quantity)
                found = True
                break

        if found:
            ET.indent(tree, space="    ")
            tree.write(file_name, encoding="utf-8", xml_declaration=True)
            print(f"\nОбновлено: Количество товара '{target_name}' изменено на {new_quantity}.")
        else:
            print(f"\nТовар '{target_name}' не найден в файле.")

    except ET.ParseError:
        print("Ошибка: Не удалось прочитать XML. Файл поврежден.")
    except PermissionError:
        print("Ошибка: Нет доступа к файлу (возможно, он открыт в другой программе).")
