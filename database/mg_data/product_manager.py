"""
This module manages product inventory in MongoDB.
It includes functionality for adding, updating, and indexing products.
"""
from datetime import datetime
from typing import List, Dict, Any, Optional
from pymongo.database import Database
from pymongo.results import DeleteResult


class ProductManager:
    """
    A class to manage product-related operations in MongoDB.
    Attributes:
        collection: The MongoDB collection for products.
    """
    def __init__(self, db: Database) -> None:
        self.collection = db['products']

    def add_one_product(self, name: str, price: float, category: str, stock: int) -> Any:
        """
        Adds a single product to the database.
        Args:
            name (str): Product name.
            price (float): Product price.
            category (str): Product category.
            stock (int): Initial stock quantity.
        Returns:
            Any: The ID of the inserted product.
        """
        product =  {
            "name": name,
            "price": price,
            "category": category,
            "stock": stock,
            "added_at": datetime.now() # Добавим дату поступления
        }
        result = self.collection.insert_one(product)
        print(f"Product {name} added to database. ID: {result.inserted_id}")
        return result.inserted_id

    def add_many_products(self, products_list: List[Dict[str, Any]]) -> Optional[List[Any]]:
        """
        Adds multiple products to the database.
        Args:
            products_list (List[Dict]): A list of product dictionaries.
        Returns:
            Optional[List[Any]]: List of inserted IDs or None if input list is empty.
        """
        if not products_list:
            return None
        result = self.collection.insert_many(products_list)
        print(f"Added {len(products_list)} products to database. ID: {result.inserted_ids}")
        return result.inserted_ids

    def update_stock(self, product_name: str, quantity: int) -> None:
        """
        Updates the stock quantity of a product using increment.
        Args:
            product_name (str): Name of the product to update.
            quantity (int): Amount to add (positive) or subtract (negative).
        """
        self.collection.update_one({"name": product_name}, {"$inc": {"stock": quantity}})
        print(f"Updated {product_name} quantity to {quantity} products.")

    def remove_out_of_stock(self) -> DeleteResult:
        """
        Removes all products with stock less than or equal to zero.
        Returns:
            DeleteResult: The result of the deletion operation.
        """
        return self.collection.delete_many({"stock": {"$lte": 0}})

    def create_category_index(self) -> str:
        """
        Creates an ascending index on the 'category' field for faster queries.
        Returns:
            str: The name of the created index.
        """
        return self.collection.create_index([("category", 1)])
