"""
This module manages customer orders in MongoDB.
It handles stock verification, total sum calculation, and order placement.
"""
from datetime import datetime
from typing import List, Dict, Any, Optional
from bson.objectid import ObjectId
from pymongo.synchronous.database import Database
from database.mg_data.product_manager import ProductManager


# pylint: disable=too-few-public-methods
class OrderManager:
    """
    Manages order creation and inventory deduction.
    Attributes:
    collection: MongoDB collection for orders.
    products_manager: Instance of ProductManager to handle stock updates.
    """

    def __init__(self, db: Database, products_manager: ProductManager) -> None:
        self.collection = db['orders']
        self.products_manager = products_manager

    def create_dynamic_order(self, customer_name:
                            str, items: List[Dict[str, Any]]
    ) -> Optional[ObjectId]:
        """
        Creates an order, calculates total price, and updates stock levels.
        Args:
            customer_name (str): Name of the customer.
            items (List[Dict]): List of items with 'name' and 'quantity'.
        Returns:
            Optional[ObjectId]: The ID of the created order if successful,
                                None otherwise.
        """
        total_sum = 0.0
        order_sum = []

        for item in items:

            product = self.products_manager.collection.find_one({"name": item["name"]})

            if product and product["stock"] >= item["quantity"]:
                price = product["price"]
                total_sum += price * item["quantity"]

                order_sum.append({
                    "name": item["name"],
                    "quantity": item["quantity"],
                    "price_at_purchase": price
                })
                self.products_manager.update_stock(item["name"], -item["quantity"])
            else:
                print(f"Error! {item['name']} is not available")
                return None

        order_doc = {
            "order_number": self.collection.count_documents({}) + 1,
            "customer": customer_name,
            "products": order_sum,
            "total_sum": total_sum,
            "order_date": datetime.now()
        }

        result = self.collection.insert_one(order_doc)
        print(f"Order successfully created. ID: {result.inserted_id} ")

        return result.inserted_id
