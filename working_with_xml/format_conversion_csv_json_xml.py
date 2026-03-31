"""
Module for data conversion between CSV, JSON and XML formats.
"""
# pylint: disable=too-few-public-methods

import csv
import json
import re
import xml.etree.ElementTree as ET


class DataConverter:
    """A class utility for converting various file formats."""

    @staticmethod
    def csv_to_json(csv_file, json_file):
        """Converts CSV file to JSON format."""

        with open(csv_file, 'r', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)

        with open(json_file, 'w', encoding="utf-8") as f:
            json.dump(data, f,  indent=4, ensure_ascii=False)

    @staticmethod
    def json_to_csv(json_file, csv_file):
        """Converts file JSON to CSV format."""
        with open(json_file, 'r', encoding="utf-8") as f:
            data = json.load(f)

        if not data:
            return

        with open(csv_file, 'w', encoding="utf-8", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def xml_to_json(xml_file, json_file):
        """Converts XML file to JSON format."""
        tree = ET.parse(xml_file)
        root = tree.getroot()

        items = []

        for child in root:
            item_dict = {sub_child.tag: sub_child.text for sub_child in child}
            items.append(item_dict)

        with open(json_file, 'w', encoding="utf-8") as f:
            json.dump(items, f, indent=4, ensure_ascii=False)

    @staticmethod
    def xml_to_csv(xml_file, csv_file):
        """Converts XML file to CSV format."""
        tree = ET.parse(xml_file)
        root = tree.getroot()

        items = []

        for child in root:
            item_dict = {sub_child.tag: sub_child.text for sub_child in child}
            items.append(item_dict)

        fieldnames = items[0].keys()

        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(items)

    @staticmethod
    def json_to_xml( json_file, xml_file):
        """Converts file JSON to XML format."""
        with open(json_file, 'r', encoding="utf-8") as f:
            data = json.load(f)

        root = ET.Element("root")

        for item in data:
            element = ET.SubElement(root, "item")

            for key, value in item.items():
                safe_key = DataConverter.clean_tag(key)
                child = ET.SubElement(element, safe_key)
                child.text = str(value)

        tree = ET.ElementTree(root)
        ET.indent(tree, space="    ")  # Делаем XML красивым

        with open(xml_file, "wb") as f:
            tree.write(f, encoding="utf-8", xml_declaration=True)

        print(f"Конвертация {json_file} -> {xml_file} завершена.")

    @staticmethod
    def csv_to_xml(csv_file, xml_file):
        """Converts CSV file to XML format."""
        with open(csv_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)

        root = ET.Element("root")

        for row in data:
            item = ET.SubElement(root, "item")

            for key, value in row.items():
                safe_key = DataConverter.clean_tag(key)
                child = ET.SubElement(item, safe_key)
                child.text = str(value)

        tree = ET.ElementTree(root)
        ET.indent(tree, space="    ")

        with open(xml_file, "wb") as f:
            tree.write(f, encoding="utf-8", xml_declaration=True)

        print(f"Конвертація {csv_file} -> {xml_file} успішно завершена.")

    @staticmethod
    def clean_tag(name):
        """Cleans the string so that it is a valid XML tag name."""
        clean_name = re.sub(r'[^a-zA-Zа-яА-Я0-0]', '_', name)

        if clean_name[0].isdigit():
            clean_name = "item_" + clean_name
        return clean_name
