"""
This module provides a connection manager for MongoDB.
It handles connection establishment and validation using ping command.
"""
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError


# pylint: disable=too-few-public-methods
class MongoConnector:
    """
    A utility class to manage MongoDB connections using pymongo.
    Attributes:
    uri (str): The MongoDB connection string.
    client (Optional[MongoClient]): The MongoClient instance after connection.
    """

    def __init__(self, uri= "mongodb://localhost:27017/") -> None:
        self.uri = uri
        self.client = None

    def connect(self) -> MongoClient|None:
        """
        Establishes a connection to the MongoDB server and validates it with a ping.
        Returns:
        Optional[MongoClient]: A connected MongoClient instance if successful,
        None otherwise.
        Raises:
        ConnectionFailure: If the server is unreachable.
        ServerSelectionTimeoutError: If the connection attempt times out.
        """
        try:
            self.client = MongoClient(self.uri, serverSelectionTimeoutMS=2000)
            self.client.admin.command('ping')
            print("Connected to MongoDB")
            return self.client
        except (ConnectionFailure, ServerSelectionTimeoutError) as e:
            print(f"Could not connect to MongoDB: {e}")
            return None
